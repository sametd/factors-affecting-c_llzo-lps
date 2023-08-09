import matplotlib.pyplot as plt
import numpy as np

d_gga = np.array(
    [
        0,
        0.10,
        0.20,
        0.30,
        0.40,
        0.45,
#        0.46,
#        0.47,
#        0.48,
#        0.49,
        0.50,
#        0.51,
#        0.52,
#        0.53,
#        0.54,
        0.55,
        0.60,
        0.70,
        0.80,
        0.90,
        1,
    ]
)

energies_gga = np.array(
    [
        -366.82097347,  # 0
        -366.78767283,  # 0.10
        -366.69777925,  # 0.20
        -366.56822987,  # 0.30
        -366.43948770,  # 0.40
        -366.39865672,  # 0.45
#        -366.39321611,  # 0.46
#        -366.38871857,  # 0.47
#        -366.38519311,  # 0.48
#        -366.37960828,  # 0.49
        -366.35524414,  # 0.50
#        -366.35399240,  # 0.51
#        -366.35468726,  # 0.52
#        -366.38217172,  # 0.53
#        -366.38447552,  # 0.54
        -366.36366625,  # 0.55
        -366.41805082,  # 0.60
        -366.53347065,  # 0.70
        -366.66827289,  # 0.80
        -366.76642011,  # 0.90
        -366.80327169,  # 1
    ]
)

energies_gga -= energies_gga.min()

print(f"Barr = {energies_gga.max()}")

fig, ax = plt.subplots()




ax.scatter(d_gga, energies_gga,alpha=.7,c="orangered",label="GGA")

plt.xticks(np.arange(0,1.1,0.2))
plt.yticks(np.arange(0,2,0.1))
plt.xlabel('X',fontsize=13)
plt.ylabel('Energy (eV)',fontsize=13)
plt.ylim(-0.05,0.51)
plt.minorticks_on()
plt.tick_params(axis = 'both', which = 'major', labelsize = 13)
plt.legend(fontsize=13)
plt.tight_layout()
plt.savefig("LPS_polaron_barr.pdf", format="pdf", dpi=300,bbox_inches='tight')