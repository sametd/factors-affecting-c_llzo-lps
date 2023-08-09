import matplotlib.pyplot as plt
import numpy as np

d_gga = np.array([0,0.1,0.2,0.25,0.3,0.4,0.5,0.6,0.7,0.75,0.8,0.9,1])

energies_gga = np.array([-1367.3142,
                     -1367.1996,
                     -1366.9389,
                     -1366.7886,
                     -1366.6416,
                     -1366.4045,
                     -1366.3106,
                     -1366.3952,
                     -1366.6373,
                     -1366.7965,
                     -1366.9643,
                     -1367.2625,
                     -1367.3968])

energies_gga -= energies_gga.min()

print(f"Barr = {energies_gga.max()}")

fig, ax = plt.subplots()


#ax.grid(True, linestyle='-.')
#ax.tick_params(labelcolor='r', labelsize='medium', width=3)

d_hse = np.array([0,0.25,0.4,0.45,0.49,0.6,0.75,1])

energies_hse = np.array([-1614.93912852,
                     -1614.31590340,
                     -1613.79381550,
                     -1613.67604100,
                     -1613.61361982,
                     -1613.70708419,
                     -1614.28026343,
                     -1615.02863796])

energies_hse -= energies_hse.min()

print(f"Barr = {energies_hse.max()}")

ax.scatter(d_hse, energies_hse,alpha=.7,c="dodgerblue",label="HSE")
ax.scatter(d_gga, energies_gga,alpha=.7,c="orangered",label="GGA")

plt.xticks(np.arange(0,1.1,0.2))
plt.yticks(np.arange(0,2,0.2))
plt.xlabel('X',fontsize=13)
plt.ylabel('Energy (eV)',fontsize=13)
plt.ylim(-0.05,1.5)
plt.minorticks_on()
plt.tick_params(axis = 'both', which = 'major', labelsize = 13)
plt.legend(fontsize=13)
plt.tight_layout()
plt.savefig("LLZO_polaron_barr.pdf", format="pdf", dpi=300,bbox_inches='tight')