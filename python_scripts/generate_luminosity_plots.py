import numpy as np
import matplotlib.pyplot as plt

#t_100, L_100 = np.loadtxt('/home/aschoudhary/Streamline_project/data/Luminosity_query_over_time_radius100.ultra', unpack=True)
t_150, L_150 = np.loadtxt('/home/aschoudhary/Streamline_project/data/Luminosity_query_over_time_radius150.ultra', unpack=True)
#t_200, L_200 = np.loadtxt('/home/aschoudhary/Streamline_project/data/Luminosity_query_over_time_radius200.ultra', unpack=True)


#plt.plot(t_100, L_100, 'r')
plt.plot(t_150, L_150, 'k')
#plt.plot(t_200, L_200, 'g')

plt.xlabel(r'$t$', fontsize=20, color='k')
plt.ylabel(r'$luminosity$', fontsize=20, color='k')
#plt.xlim(500, 2500)
plt.ylim(-200.5, 200.5)
#plt.savefig('/home/aschoudhary/Streamline_project/plots/luminosity_plots/luminosity_vs_time_r100.pdf')
plt.show()
