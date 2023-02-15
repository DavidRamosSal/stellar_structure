import os
import numpy as np
from static_structure import static, MRrhoc

owd=os.getcwd()
path=os.chdir('equationsOfState/numerical')
EOSlist=[]
listOfEntries= os.scandir(path)
for entry in listOfEntries:
    if entry.path.endswith('dat'):
        EOSlist.append(entry.name)
os.chdir(owd)
os.mkdir('results')

for EOS in EOSlist:
    name=EOS[:-4]
    os.mkdir('results/'+name)
    rhoEOS,PEOS=np.loadtxt('equationsOfState/numerical/'+EOS,usecols=(2,1),unpack=True)
    if np.amin(rhoEOS)>1e+13:
        n=np.arange((1/32)*(31*np.log10(np.amin(rhoEOS))+np.log10(np.amax(rhoEOS))),np.log10(np.amax(rhoEOS)),0.01)
        print('H')
    else:
        n=np.arange(14.0,np.log10(np.amax(rhoEOS)),0.01)
    print(n)
    rhosc=10.0**n
    r0=0.0
    dr0=1e-6
    m0=0.0
    MRrhoc(rhosc,m0,r0,dr0,rhoEOS,PEOS,name,(1+0.3)*np.amin(rhoEOS))
