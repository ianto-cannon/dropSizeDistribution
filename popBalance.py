import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"text.usetex": True})#,'font.size' : 12,})
fig, ax = plt.subplots(1, figsize=[4.5, 2.7])
ax.tick_params(which='both', direction='in', top=True, right=True)
daughters = 2
diss = 1
surf = 1 
dens = 1
dH = 0.725 * surf**(3/5) * dens**(-3/5) * diss**(-2/5)
diam = 8*dH
numVela = 1#0**-5
numGarr = 1#0**-5
lifeTiVela = lambda diam: diss**(-1/3) * diam**(2/3) / 14.8 / np.exp( -7.8 * surf / dens / diss**(2/3) / diam**5/3 )
lifeTiGarr = lambda diam: diss**(-1/3) * diam**(2/3)  
x=np.array([1,10])
ax.plot(x, 1024*x**(-10/3), c='k', label='$N=1024(d/d_H)^{-10/3}$')#, ls='dotted'
for i in range(100):
  if diam/dH<1: break
  if i==0: 
    lblGarr = '$\\tau=\\tau_d$'#=d^{2/3}/\\epsilon^{1/3}$'
    lblVela = '$\\tau=\\tau_{CT}$'#=d^{2/3}/(14.8\\epsilon^{1/3}\\exp(-7.8\\sigma/(\\rho\\epsilon^{2/3}d^{5/3}))$'
  else:
    lblVela=''
    lblGarr=''
  ax.plot(diam/dH, numGarr, 'o', mfc='None', mec='k', clip_on=False, label=lblGarr)#, mew=1.5)
  if numVela<1e5: ax.plot(diam/dH, numVela, 'o', mfc='k', mec='None', clip_on=False, label=lblVela)#, mew=1.5)
  print('num',numGarr)
  birthTiVela = lifeTiVela(diam)
  birthTiGarr = lifeTiGarr(diam)
  diam /= daughters**(1/3)
  numVela *= daughters**(1/3) * daughters * lifeTiVela(diam) / birthTiVela
  numGarr *= daughters**(1/3) * daughters * lifeTiGarr(diam) / birthTiGarr
  #numGarr *= daughters**(10/9) 
ax.set_xlabel('$d/d_H$')
ax.set_ylabel('$N$',rotation=0)
ax.set_xlim([1,10])
ax.set_ylim([1,10**5])
ax.set_xscale('log')
ax.set_yscale('log')
#ax.set_xticklabels([1,2,3,4,6,10])
ax.legend()
fname = 'popBalance.svg'
print('savin ',fname)
fig.savefig(fname, transparent=True, bbox_inches="tight")
