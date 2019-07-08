import numpy as np

epsilon = np.finfo(float).eps

c=2.99792458e10
G=6.67e-8
Msun=1.9892e33
me=9.11e-28
mn=1.674e-24
h=6.63e-27
sigma=5.6704e-5

rhodim=mn**4.0*c**3.0/(8.0*np.pi**2*(h/(2.0*np.pi))**3.0) #Dimensions of energy density
rdim=c/np.sqrt(rhodim*G) # Dimensions of radius
mdim=rdim*c**2.0/G # Dimensions of mass
Pdim=rhodim*c**2 # Dimensions of pressure