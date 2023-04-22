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


a1, b1 = np.genfromtxt('Brechung.txt', unpack=True, skip_header=1)

def Theorie(a,b):
    return np.sin(a)/np.sin(b)

def näherung(a,b):
    return np.arcsin(np.sin(a*np.pi/180)/b)*180/np.pi   


params = curve_fit(näherung,a1,b1)
#a_fit = params[0][0]
b_fit = params[0][0]
#h=np.linspace(0.0185,0.026,10)
plt.plot(a1, näherung(a1,b_fit) , 'b', linewidth = 1, label = 'Ausgleich', alpha=0.5)
plt.plot(a1,b1,'xr',linewidth=1, label='Messwerte' ,alpha=1)
#plt.plot(a1, Theorie(a1,b1) , 'orange', linewidth = 1, label = 'Theorie', alpha=0.5)

plt.xlabel(r'$\alpha_1 \, / \, \mathrm{°}$')
plt.ylabel(r'$\beta_1 \, / \, \mathrm{°}$')
plt.legend(loc="best")                  # legend position
plt.grid(True)                          # grid style
#plt.xlim(15, 85)
#plt.ylim(5, 45)
print('b=',b_fit)
#print('test', näherung(30))
plt.savefig('build/Brechung.pdf', bbox_inches = "tight")
plt.clf() 
