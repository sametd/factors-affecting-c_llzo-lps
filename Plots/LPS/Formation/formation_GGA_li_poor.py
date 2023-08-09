import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams

def findInterID(x,y,z):
  for i,j in enumerate(x):
    if(y[i]-z[i]<0.05):
      return(i)

#energy of the model structure (352 e-)
e_model = -370.6516 #OK

#energy of the charged li vacancy vLi^- (352 e-)
#e_v_li_0 = -363.8082 #OLD POSITIONS
e_v_li_0 = -364.05668264 #OK

#energy of the neutral li vacancy vLi^0 (351 e-)
#e_v_li_m1 = -365.5538 #OLD POSITIONS
e_v_li_m1 = -365.87031585 #OK

#energy of the charged li interstitial  Li_i+ (352 e-)
e_i_li_0 = -377.54846666 #OK

#energy of the neutral li interstitial Li_i0 (353 e-)
e_i_li_p1 = -373.4794 #OK

#energy of the p polaron p+ (351 e-)
e_p_pol = -372.4769 #ok

#energy of the e hole e- (353 e-)
e_e_hol = -366.7872 #OK

#energy of the neutral s vacancy (346 e-)
e_v_s_neut = -365.47113898

#energy of the s vacancy less 1 (345 e-)
e_v_s_m1 = -367.54065679

#energy of the s vacancy less 2 (344 e-)
e_v_s_m2 = -369.89643051

#S potential taken from materials project
#https://materialsproject.org/materials/mp-96?chemsys=S
mu_s = -4.127232

#Energy of the bulk Li (this is BCC, sym:229)
#BCC Li is -1.89214771 eV
# Kang et. al. figure 5a is -3.37 eV (Li-rich)
# Kang et. al. figure 5b is -4.16 eV (Li-rich)
m_li = -4.16



#vbm and cbm are taken from gga model (tetrahedron)
vbm = 1.961900
cbm = 4.279900

#100 equally distanced point between vbm and cbm for plotting purpose
x = np.linspace(vbm,cbm,100)

#Li vacancy charged (352 e-)
y = -x + (e_v_li_0 - e_model + m_li) + 0.291998 
#Li interstitial charged (352 e-)
z = +x + (e_i_li_0 - e_model - m_li) + 0.271998
#Li vacancy neutral (351 e-)
n = [e_v_li_m1 - e_model + m_li]*len(y)
#Li interstitial neutral (353 e-)
m = [e_i_li_p1 - e_model - m_li]*len(y)
#p polaron (351 e-)
p = +x + (e_p_pol - e_model) + 0.231998
#e hole (353 e-)
e = -x + (e_e_hol - e_model) + 0.271998
#S vacancy neutral (346 e-)
q = [e_v_s_neut - e_model + mu_s]*len(x)
#S vacancy less 1 (345 e-)
w = x + (e_v_s_m1 - e_model + mu_s)
#S vacancy less 2 (344 e-)
r = 2*x + (e_v_s_m2 - e_model + mu_s)


###PLOTS###
linewidth = 2.1
def plot_mins(data_arr,x,label,color):
    size = len(data_arr)
    vals = np.zeros((len(data_arr[0]),size))
    for i in range(len(data_arr)):
        vals[:,i] = data_arr[i]
    plot_vals = np.min(vals,axis=1)
    plt.plot(x,plot_vals,label=label,color=color,linewidth = linewidth)
x-=vbm

#Li Vacancy
plot_mins([y,n],x,"$\\rm V_{\\rm Li}^{\\rm q}$","dodgerblue")
#Li Interstitial
plot_mins([z,m],x,"$\\rm Li_{\\rm i}^{\\rm q}$","orangered")
#S Vacancy
plot_mins([q,w,r],x,"$\\rm V_{\\rm S}^{\\rm q}$","seagreen")
#p+
plt.plot(x,p,label='p+',color="mediumpurple",linewidth=linewidth)
#e-
plt.plot(x,e,label='e-',color="dimgray",linewidth=linewidth)

l = findInterID(x,y,z)
plt.vlines(x[l],0,5,color='#262728', zorder = 0, linestyle='--', label='Fermi level', linewidth = linewidth)
print(f"E_F={x[l]}")
print(f"Formation energy of e- =      {e[l]:.4f} eV")
print(f"Formation energy of p+ =      {p[l]:.4f} eV")
print(f"Formation energy of S_neut =  {q[l]:.4f} eV")
print(f"Formation energy of S_less1 = {w[l]:.4f} eV")
print(f"Formation energy of S_less2 = {r[l]:.4f} eV")

plt.ylim(0,2)
plt.xlim(0,2.5)
plt.xticks(np.arange(0,2.6,0.5))
plt.yticks(np.arange(0,2.1,0.5))
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
#plt.legend(fontsize="12",framealpha=1)
#TEXT
#li int
plt.text(2.07, 1.37, '$\\rm Li_{\\rm i}^{\\rm q}$',color="orangered",fontsize=13)
#li vac
plt.text(0.39, 0.38, '$\\rm V_{\\rm Li}^{\\rm q}$',color="dodgerblue",fontsize=13)
#e- polaron
plt.text(0.4, 1.79, '$\\rm e^{\\rm -}_{\\rm p}$',color="dimgray",fontsize=13)
#hole polaron
plt.text(1.12, 1.41, '$\\rm h^{\\rm +}_{\\rm p}$',color="mediumpurple",fontsize=13)
#s vac
plt.text(2.07, 1.09, '$\\rm V_{\\rm S}^{\\rm q}$',color="seagreen",fontsize=13)

plt.tight_layout()
plt.savefig("GGA/Li-Poor_GGA.pdf", format="pdf", dpi=300,bbox_inches='tight')

