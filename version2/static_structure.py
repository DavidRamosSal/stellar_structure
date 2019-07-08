from Physical_Const import *
from RK4 import RK4step
from adaptive_step import *
from scipy import integrate, interpolate

def static(rho0,m0,r0,dr0,nu0,rhoarray,Parray,name,cutoff=0.0):
    """Builds a neutron star model from the initial values y0 and an interpolated EOS. The solver will start
    in r0 with an arbitrary stepsize dr0 and will stop when the
    pressure becomes negative. Returns the mass, pressure, density and nu profiles as functions of r. The parameter cutoff
    can be provided to stop the integration at the minimum energy density available in the EOS."""
    
    def PEoS(rho):
        logP=interpolate.interp1d(np.log10(rhoarray/rhodim),np.log10((Parray*c**2)/Pdim))
        return 10.0**logP(np.log10(rho))
    def rhoEoS(P):
        logrho=interpolate.interp1d(np.log10((Parray*c**2)/Pdim),np.log10((rhoarray/rhodim)))
        return 10.0**logrho(np.log10(P))

    
    def TOV(r,y):
        mns, pns, nuns= y
        dmdr=4.0*np.pi*r**2.0*rhoEoS(pns)
        if (1.0-(rhoEoS(pns)/rhoEoS(y0[1])))<(10*epsilon):
            dpdr=-4*np.pi*((pns+rhoEoS(y0[1]))*(rhoEoS(y0[1])/3+pns)/(1-(8*np.pi/3)*r**2*rhoEoS(y0[1])))*r
            #print('h')
        else:
            dpdr=-((4.0*np.pi*r**3.0*pns+mns)*(pns+rhoEoS(pns)))/(r*(r-2.0*mns))
        dnudr=-dpdr/(pns+rhoEoS(pns))
        #print('P',pns*Pdim,'rho',rhoEoS(pns)*rhodim)
        #print('r',r)
        return [dmdr,dpdr,dnudr]
    
    f=open('results/' + name + '/' +str(np.log10(rho0*rhodim))+'.dat','w+')
    #ms=[]; ps=[]; rhos=[]; nus=[]; rs=[]  # creating lists to save the solution
    f.write(str(m0)+'\t'+ str(PEoS(rho0))+'\t'+str(rho0)+'\t'+str(nu0)+'\t'+str(r0)+'\n')
    #ms.append(m0); ps.append(PEoS(rho0)); rhos.append(rho0); nus.append(nu0); rs.append(r0) 
    y0=[m0,PEoS(rho0),nu0]
    y=RK4step(TOV,r0,y0,dr0) # first step taken arbitrary (dr0)  
    dr=dr0
    r=r0+dr 
    f.write(str(y[0])+'\t'+ str(y[1])+'\t'+str(rhoEoS(y[1]))+'\t'+str(y[2])+'\t'+str(r)+'\n')
    #ms.append(y[0]); ps.append(y[1]); rhos.append(rhoEoS(y[1])); nus.append(y[2]); rs.append(r) 
    while y[1] > 0.0 and rhoEoS(y[1])*rhodim > cutoff and dr>10*epsilon:
        #print('h2')
        #print('P',y[1],'m',y[0],'r',r,'dr',dr)
        dr=stepsize(y,TOV(r,y))
        y=RK4step(TOV,r,y,dr)
        r=r+dr
        f.write(str(y[0])+'\t'+ str(y[1])+'\t'+str(rhoEoS(y[1]))+'\t'+str(y[2])+'\t'+str(r)+'\n')
        #ms.append(y[0]); ps.append(y[1]); rhos.append(rhoEoS(y[1])); nus.append(y[2]); rs.append(r)
    f.close()
    return np.array([y[0],r])

def MRrhoc(rhosc,m0,r0,dr0,rhoarray,Parray,name,cutoff=0.0):
    """Builds a family of neutron star models from an equation of state P(rho) and rho(P), given a range of central densities rhosc.
    Returns three lists with the values of Rstar (RR) and Mstar (MM) for the corresponding value of rhoc (rhorho)."""
    #psc=PEoS(rhosc/rhodim) #Range of central pressures
    #MM=[];RR=[];rhorho=[]
    f=open('results/'+name+'/'+'MRrhoc'+'.dat','w+')
    for rhoc in rhosc/rhodim:
        A = static(rhoc,m0,r0,dr0,0,rhoarray,Parray,name,cutoff)
        f.write(str(A[1]*rdim*1e-5)+'\t'+str(A[0]*mdim/Msun)+'\t'+str(rhoc*rhodim)+'\n')
        #RR.append(r[-1]*rdim*1e-5); MM.append(m[-1]*mdim/Msun); rhorho.append(rho[0]*rhodim)
    f.close()
    return None#[RR,MM,rhorho]