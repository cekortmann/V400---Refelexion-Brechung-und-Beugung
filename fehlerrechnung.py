import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from numpy import sqrt
import scipy.constants as const
from scipy.optimize import curve_fit                        # Funktionsfit:     popt, pcov = curve_fit(func, xdata, ydata) 
from uncertainties import ufloat                            # Fehler:           fehlerwert =  ulfaot(x, err)
from uncertainties import unumpy as unp 
from uncertainties.unumpy import uarray                     # Array von Fehler: fehlerarray =  uarray(array, errarray)
from uncertainties.unumpy import (nominal_values as noms,   # Wert:             noms(fehlerwert) = x
                                  std_devs as stds)  
from uncertainties.umath import sin
from uncertainties.umath import cos
from uncertainties.umath import asin



#Brechung
a=[10,20,30,40,50,60,70,80]
ua1= ufloat(10,1)
ua2= ufloat(20,1)
ua3= ufloat(30,1)
ua4= ufloat(40,1)
ua5= ufloat(50,1)
ua6= ufloat(60,1)
ua7= ufloat(70,1)
ua8= ufloat(80,1)

b=[6,13,20,26,31,35,39,41]
ub1= ufloat(6,1)
ub2= ufloat(13,1)
ub3= ufloat(20,1)
ub4= ufloat(26,1)
ub5= ufloat(31,1)
ub6= ufloat(35,1)
ub7= ufloat(39,1)
ub8= ufloat(41,1)

def Mittelwert1(x):
    return sum(x)/len(x)

def Mittelwert(a1,a2,a3,a4,a5,a6,a7,a8):
    return (a1+a2+a3+a4+a5+a6+a7+a8)/8

def Brechungsindex(a,b):
    return sin(a*np.pi/180)/sin(b*np.pi/180)

un1=Brechungsindex(ua1,ub1)
un2=Brechungsindex(ua2,ub2)
un3=Brechungsindex(ua3,ub3)
un4=Brechungsindex(ua4,ub4)
un5=Brechungsindex(ua5,ub5)
un6=Brechungsindex(ua6,ub6)
un7=Brechungsindex(ua7,ub7)
un8=Brechungsindex(ua8,ub8)

avga= Mittelwert(ua1,ua2,ua3,ua4,ua5,ua6,ua7,ua8)
avgb= Mittelwert(ub1,ub2,ub3,ub4,ub5,ub6,ub7,ub8)
avgn= Mittelwert(un1,un2,un3,un4,un5,un6,un7,un8)

#print('avg a',Mittelwert(ua1,ua2,ua3,ua4,ua5,ua6,ua7,ua8))
#print('avg b',Mittelwert(ub1,ub2,ub3,ub4,ub5,ub6,ub7,ub8))
#print('avg aa',Mittelwert1(a))
#print('avg bb',Mittelwert1(b))
#print('Brechungsindex aus avg', Brechungsindex(Mittelwert1(a),Mittelwert1(b)))
#print(Brechungsindex(avga,avgb))
#print('n1',un1)
#print('n2',un2)
#print('n3',un3)
#print('n4',un4)
#print('n5',un5)
#print('n6',un6)
#print('n7',un7)
#print('n8',un8)
#print('erst un',avgn)
#print('abweichung',avgn/1.49)

#print('n1',un1)
#print('Mittelwert aus avg', Brechungsindex(avga,avgb))

#Strahlenversatz
d=5.85
def Strahlenversatz(a,b):
    return 5.85*sin((a-b)*np.pi/180)/cos(b)

un1= ufloat(1.51,0.05)
bneu=[0,0,0,0,0,0,0,0]
i=0
while i<8:
    bneu[i]+=asin(sin(a[i]*np.pi/180)/un1)*180/np.pi
    i+=1

sv1=[Strahlenversatz(ua1, ub1),Strahlenversatz(ua2, ub2),Strahlenversatz(ua3, ub3),Strahlenversatz(ua4, ub4),Strahlenversatz(ua5, ub5),Strahlenversatz(ua6, ub6),Strahlenversatz(ua7, ub7),Strahlenversatz(ua8, ub8)]
sv2=[Strahlenversatz(ua1, bneu[0]),Strahlenversatz(ua2, bneu[1]),Strahlenversatz(ua3,  bneu[2]),Strahlenversatz(ua4, bneu[3]),Strahlenversatz(ua5,  bneu[4]),Strahlenversatz(ua6,  bneu[5]),Strahlenversatz(ua7,  bneu[6]),Strahlenversatz(ua8,  bneu[7])]

#for x in sv1:
#    print(x)

print('sv1',sv1)
print('sv2',sv2)
#print('bneu',bneu)

#Prisma
def delta(a1,a2,b1,b2):
    return (a1+a2)-(b1+b2)

a1 =unp.uarray([30,35,40,50,55],[1,1,1,1,1])
ra2= unp.uarray([73,65,57,46,41],[1,1,1,1,1])
ga2= unp.uarray([74,66,58,47,41],[1,1,1,1,1])

b1 = unp.uarray([0,0,0,0,0],[0,0,0,0,0])
rb2= unp.uarray([0,0,0,0,0],[0,0,0,0,0])
gb2= unp.uarray([0,0,0,0,0],[0,0,0,0,0])

i=0
##while i<5:
#    b1[i]+=asin(sin(a1[i]*np.pi/180)/1.51)*180/np.pi
#    i+=1
#n=0
#while n<5:
#    rb2[n]+=asin(sin(ra2[n]*np.pi/180)/1.51)*180/np.pi
#    gb2[n]+=asin(sin(ga2[n]*np.pi/180)/1.51)*180/np.pi
#    n+=1
#i=0
#while i<5:
#    print('rotes licht',i,delta(a1[i],ra2[i],b1[i],rb2[i]))
#    i+=1

#i=0
#while i<5:
#    print('grünes licht',i,delta(a1[i],ga2[i],b1[i],gb2[i]))
#    i+=1

#print(b1)
#print(rb2)
#print(gb2)

#Gitter
Gitterk= unp.uarray([1,2,3,4,5,6,7,8],[0,0,0,0,0,0,0,0])
d600= ufloat(1.67*10**(-6),0)
d300= ufloat(3.33*10**(-6),0)
d100= ufloat(1*10**(-5),0)
ug600phi= ufloat(19,1)
ur600phi= ufloat(23,1)
ug300phi= unp.uarray([9,18,28],[1,1,1])
ur300phi= unp.uarray([11,22,34],[1,1,1])
ug100phi= unp.uarray([3,6,9,12,15,19,22],[1,1,1,1,1,1,1])
ur100phi= unp.uarray([4,7,11,15,19,23,0],[1,1,1,1,1,1,0])


def Lambda(phi,d,k):
    t=1
    while t<=k:   
        return (d*sin(phi*np.pi/180)/k)
        t+=1
def Lambda2(phi,d,k,Gitterk):
    t=1
    while t-1<k:
        print('maximum',t,d*sin(phi[t-1]*np.pi/180)/Gitterk[t-1])
        t+=1
ug1300= ufloat(5.2,0.6)
ug2300= ufloat(5.15,0.28)
ug3300= ufloat(5.21,0.17)

ur1300= ufloat(6.4,0.6)
ur2300= ufloat(6.24,0.27)
ur3300= ufloat(6.21,0.16)

def Mittelwert3(a,b,c):
    return (a+b+c)/3
    

#print('lambda rot 600', Lambda(ur600phi,d600,1))
#print('lambda grün 600', Lambda(ug600phi,d600,1))

#print('lambda grün 300')
#print(Lambda2(ug300phi,d300,3,Gitterk))
#print('lambda rot 300')
#print(Lambda2(ur300phi,d300,3,Gitterk))
#print('mittelwert300grün',Mittelwert3(ug1300,ug2300,ug3300))
#print('mittelwert300rot',Mittelwert3(ur1300,ur2300,ur3300))
#print(Lambda2(ug100phi,d100,7,Gitterk))
#print(Lambda2(ur100phi,d100,6,Gitterk))