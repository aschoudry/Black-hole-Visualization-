import numpy as np
import matplotlib.pyplot as plt


t,ft=np.loadtxt("/home/aschoudhary/Streamline_project/data/Luminosity_query_over_time_radius_100_mo_mode_subtracted.ultra",unpack=True)

#tm,fm=np.loadtxt("/home/aschoudhary/Streamline_project/data/MoestaFig3_nospin_Eq4",unpack=True)

#t,ft=np.loadtxt("/home/aschoudhary/Streamline_project/data/Luminosity_query_over_time_radius_b0subtracted.ultra",unpack=True)

Y=np.log10(ft)*2.0176422162141026
#Ym=fm


t=(t*4.23*pow(10, -6)*pow(10,8))/(60*60) 
t=t-t[np.where(Y==max(Y))]
#plt.plot(Ym[0:88])
plt.plot(t,Y, 'r',label=r"$0^\circ \ inclination$")
#plt.plot(tm,fm,'k',label='from Moests data')
plt.xlim(-45.0, 15.0)
plt.ylim(-18.0,-14.4)
plt.xticks([-40,-20,0])
plt.yticks([-18, -17, -16, -15, -14])
plt.xlabel(r"$time \ [hours]$", fontsize=15)
plt.ylabel(r"$\log_{10}(L_{EM})[geo]$", fontsize=15)
plt.legend(loc='upper left')
plt.savefig("luminosity20thFeb2018m0.png")
plt.show()

#print np.where(Y==max(Y)), np.where(Ym==max(Ym))


