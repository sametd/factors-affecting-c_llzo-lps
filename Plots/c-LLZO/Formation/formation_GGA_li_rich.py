import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams

def findInterID(x,y,z):
  for i,j in enumerate(x):
    if(y[i]-z[i]<0.1):
      return(i)


#model structure (1088 e-)
e_model = -1376.07316634
#charged Li vacancy (1088e-)
e_li_vacancy_charged = -1366.33876248
#charged Li interstitial (1088e-)
e_li_interstitial_charged =  -1385.99296763
#neutral Li interstitial (1089e-)
e_li_interstitial_neutral = -1377.33336312
#neutral O vacancy (1080e-)
e_o_vacancy_minus_2 = -1380.13885932
#O vacancy plus 1 (1081e-)
e_o_vacancy_minus_1 = -1372.54961563
#O vacancy plus 2 (1082e-)
e_o_vacancy = -1364.43923731
#polaron (1089e-)
e_polaron_1089 = -1367.31424519
### LI POTENTIAL ###
m_li = -1.89214771
d_m_li = -0.3242 #li rich
#d_m_li = -2.4242 #li poor
m_li += d_m_li
### O POTENTIAL ###
"""
E_water(g)   = -14.21986155 eV
ZPE_water(g) = 0.56         eV
TS_water(g)  = 0.67         eV

E_h2(g)      = -6.77016702  eV
ZPE_h2(g)    = 0.27         eV
TS_h2(g)     = 0.41         eV

mO2 = 4.92 + 2 * (E_water(g) + ZPE_water(g) + TS_water(g))
           - 2 * (E_h2(g)    + ZPE_h2(g)    + TS_h2(g))

mO = mO2 / 2 =  -4.9552
"""
m_o = -4.9552
d_m_o = -4.3061 #o poor
#d_m_o = -0.1061 #o rich
m_o += d_m_o
### VBM-CBM ###
VBM = 4.4669
CBM = 8.7634
BANDGAP = 4.2965
### CORRECTIONS ###
corr_li_vacancy_charged = 0.168375
corr_li_interstitial_charged = 0.175375
corr_o_vacancy_m1 = 0.131374
corr_o_vacancy_m2 = 0.581499
corr_polaron_1089 = 0.144375
######## PLOTTING ########
###DATA###
#100 equally distanced point between vbm and cbm for plotting purpose
x = np.linspace(VBM,CBM,100)
#Li vacancy charged (1088e-)
y = -x + (e_li_vacancy_charged - e_model + m_li) + corr_li_vacancy_charged
#Li interstitial charged (1088e-)
z = +x + (e_li_interstitial_charged - e_model - m_li) + corr_li_interstitial_charged
#Li interstitial neutral (1089e-)
m = [e_li_interstitial_neutral - e_model - m_li]*len(y)
#p polaron (1089e-)
p = -x + (e_polaron_1089 - e_model) + corr_polaron_1089
#O vacancy +2 (1080 e-)
w = 2*x + (e_o_vacancy_minus_2 - e_model + m_o) + corr_o_vacancy_m2
#O vacancy +1 (1081 e-)
q = x + (e_o_vacancy_minus_1 - e_model + m_o)  + corr_o_vacancy_m1
#O vacancy neutral (1082 e-)
n = [e_o_vacancy - e_model + m_o]*len(q)
###PLOTS###
linewidth = 2.1
def plot_mins(data_arr,x,label,color):
    size = len(data_arr)
    vals = np.zeros((len(data_arr[0]),size))
    for i in range(len(data_arr)):
        vals[:,i] = data_arr[i]
    plot_vals = np.min(vals,axis=1)
    plt.plot(x,plot_vals,label=label,color=color,linewidth = linewidth)
x-=VBM
#Li vacancy
plt.plot(x,y,label='$\\rm V_{\\rm Li}^{\\rm q}$',color="dodgerblue",linewidth = linewidth)
#electron polaron
plt.plot(x,p,label='$\\rm e^{\\rm -}_{\\rm p}$',color="dimgray",linewidth = linewidth)
#O vac
plot_mins([w,q,n],x,"$\\rm V_{\\rm O}^{\\rm q}$","yellowgreen")
#Li int
plot_mins([z,m],x,"$\\rm Li_{\\rm i}^{\\rm q}$","orangered")
plt.xlim([0,5])
plt.ylim([0,5])
l = findInterID(x,y,z)
print(w[l],q[l],n[l],p[l])
plt.vlines(x[l]+.014,0,5,color='#262728', zorder = 0, linestyle='--', label='Fermi level', linewidth = linewidth)
print(f'E_F = {x[l]+.014}')
plt.xlabel('$E_{\\rm F}$ - $E_{\\rm VBM}$ (eV)',fontsize=13)
plt.ylabel('Formation Energy (eV)',fontsize=13)
plt.minorticks_on()
plt.tick_params(axis = 'both', which = 'major', labelsize = 13)
plt.gca().set_aspect('equal')
ax = plt.gca()
#ax.set_facecolor('whitesmoke')
ratio = 1.0
xleft, xright = ax.get_xlim()
ybottom, ytop = ax.get_ylim()
ax.set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)
#TEXT
#li int
plt.text(4., 1.05, '$\\rm Li_{\\rm i}^{\\rm q}$',color="orangered",fontsize=13)
#li vac
plt.text(1.35, 1.9, '$\\rm V_{\\rm Li}^{\\rm q}$',color="dodgerblue",fontsize=13)
#polaron
plt.text(2., 2.5, '$\\rm e^{\\rm -}_{\\rm p}$',color="dimgray",fontsize=13)
#o vac
plt.text(4., 2.47, "$\\rm V_{\\rm O}^{\\rm q}$",color="yellowgreen",fontsize=13)
plt.tight_layout()
plt.savefig("GGA/Li-Rich-O-Poor_GGA.pdf", format="pdf", dpi=300,bbox_inches='tight')