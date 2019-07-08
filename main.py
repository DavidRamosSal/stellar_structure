import os
import numpy as np
from static_structure import static, MRrhoc

owd=os.getcwd()
path=os.chdir('EOS')
EOSlist=[]
with os.scandir(path) as listOfEntries:
    for entry in listOfEntries:
        if entry.path.endswith('dat'):
            EOSlist.append(entry.name)
os.chdir(owd)
os.mkdir('results')

for EOS in EOSlist:
    name=EOS[:-4]
    os.mkdir('results/'+name)
    rhoEOS,PEOS=np.loadtxt('EOS/'+EOS,usecols=(2,1),unpack=True)
    if np.amin(rhoEOS)<1e+14:
        n=np.arange(np.log10(np.amin(rhoH1)),np.log10(np.amax(rhoH1)),0.005)
    else:
        n=np.arange(1e+14,np.log10(np.amax(rhoH1)),0.005)
    rhosc=10.0**n
    r0=0.0
    dr0=1e-8
    m0=0.0
    MRrhoc(rhosc,m0,r0,dr0,rhoEOS,PEOS,name,(1+1e-3)*np.amin(rhoEOS))