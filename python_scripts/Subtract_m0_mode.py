import numpy as np
from scipy import integrate
from scipy.special import sph_harm,lpmv
from scipy.integrate import simps

#check orthogonality of Spherical harmonics
#th in [0, 2 pi] and ph in [0, pi]
def check_orthogonality(th, ph):
	l1=5
	m1=0
	l2=5
	m2=-0
	f=np.sin(ph)*sph_harm(-m1,l1,th,ph)*sph_harm(m2,l2,th,ph)
	return f
	

a=integrate.nquad(check_orthogonality, [[0, 2*np.pi],[0, np.pi]])
print a[0]


def f(th, ph):
	fx=1.0*sph_harm(-1,5,th,ph)+2.0*sph_harm(0,5,th,ph)+ 3.0*sph_harm(-2,3,th,ph)+ 4.0*sph_harm(-1,3,th,ph)
	return fx

x=integrate.nquad(lambda th, ph: f(th, ph)*sph_harm(2,3,th,ph)*np.sin(ph), [[0, 2*np.pi],[0, np.pi]])
print x

theta = np.linspace(0, 2*np.pi,200)
phi = np.linspace(0, np.pi,200)
fx = f(theta[:,None], phi)**sph_harm(2,3,theta[:,None],phi)*np.sin(phi)

g = simps(simps(fx, theta), phi)
print g 

