import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


filepathbh1="/datarepo/dataforashok/Oct21_zero_inclination_poynting_data/blandford_znajeck_studies-giraffe-hr/separation_10p4__nonspinning__vertBfield/BH_diagnostics.ah1.gp"
filepathbh2="/datarepo/dataforashok/Oct21_zero_inclination_poynting_data/blandford_znajeck_studies-giraffe-hr/separation_10p4__nonspinning__vertBfield/BH_diagnostics.ah2.gp"
filepathbh3="/datarepo/dataforashok/Oct21_zero_inclination_poynting_data/blandford_znajeck_studies-giraffe-hr/separation_10p4__nonspinning__vertBfield/BH_diagnostics.ah3.gp"



x1,y1,z1 = np.loadtxt(filepathbh1,skiprows=42, usecols=(2,3,4) ,unpack=True)
x2,y2,z2 = np.loadtxt(filepathbh2,skiprows=42, usecols=(2,3,4) ,unpack=True)
x3,y3,z3 = np.loadtxt(filepathbh3,skiprows=42, usecols=(2,3,4) ,unpack=True)


mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x1, y1, z1, label='parametric curve')
#ax.plot(x2, y2, z2, label='parametric curve')
#ax.plot(x3, y3, z3, label='parametric curve')

ax.legend()

plt.show()



