import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from numpy import sqrt
import pandas as pd
import scipy.constants as const
from scipy.optimize import curve_fit                        # Funktionsfit:     popt, pcov = curve_fit(func, xdata, ydata) 
from uncertainties import ufloat                            # Fehler:           fehlerwert =  ulfaot(x, err)
from uncertainties import unumpy as unp 
from uncertainties.unumpy import uarray                     # Array von Fehler: fehlerarray =  uarray(array, errarray)
from uncertainties.unumpy import (nominal_values as noms,   # Wert:             noms(fehlerwert) = x
                                  std_devs as stds)         # Abweichung:       stds(fehlerarray) = errarray


a1, a2 = np.genfromtxt('Reflexion.txt', unpack=True, skip_header=1)

def näherung(x,a):
    return a*x     


params = curve_fit(näherung,a1,a2)
a_fit = params[0][0]
#b_fit = params[0][1]
#h=np.linspace(0.0185,0.026,10)
plt.plot(a1,a2,'xr',linewidth=1, label='Messwerte' ,alpha=1)
plt.plot(a1, näherung(a1,a_fit), 'orange', linewidth = 1, label = 'Ausgleichskurve', alpha=0.5)

plt.xlabel(r'$\alpha_1 \, / \, \mathrm{°}$')
plt.ylabel(r'$\alpha_2 \, / \, \mathrm{°}$')
plt.legend(loc="best")                  # legend position
plt.grid(True)                          # grid style
plt.xlim(15, 85)
plt.ylim(15, 85)
print('a=',a_fit)
plt.savefig('build/Reflexion.pdf', bbox_inches = "tight")
plt.clf() 
