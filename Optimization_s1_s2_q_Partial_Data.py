import numpy as np
import pandas as pd
from scipy.optimize import minimize


# This script determines q, s1, and s2 such that Z, P, and A are like experiment

#####      q= ?        x[0]
#####      s1_s2= ?    x[1]
#####      delta= ?    x[2]


# Specify the condition for which you want to optimize #
condition= 'S_0404'



df = pd.read_excel (r'Variable_Values_Partial_Data.xlsx',index_col=0)
Z_var = df.loc['Z'].at[condition]
P_var  = df.loc['P'].at[condition]
A_var  = df.loc['A'].at[condition]
DZ_var  = df.loc['DZ'].at[condition]
DP_var  = df.loc['DP'].at[condition]
DA_var  = df.loc['DA'].at[condition]



h=2.7
k=7

# s1= s1_s2 + deltas
def S1(x):
    q= x[0]
    s1_s2 = x[1]
    delta = x[2]
    s1= s1_s2 + delta
    return s1


# s2= s1_s2 - delta
def S2(x):
    q= x[0]
    s1_s2 = x[1]
    delta = x[2]
    s2= s1_s2 - delta
    return s2


def calcCF(x):
    q = x[0]
    s1_s2 = x[1]
    delta = x[2]
    s1= s1_s2 + delta
    s2= s1_s2 - delta
    
    xmax= h - ((h-s1)**2 - (q**2)/k**2)**(1/2)
    xmin= -h + ((h-s2)**2 - (q**2)/k**2)**(1/2)
    A=(xmax-xmin)/2

    T1=np.log((k*(h-s1)+q)/(k*(h-s1)-q))/k
    T2=(s1+s2)/q
    T3=np.log((k*(h-s2)+q)/(k*(h-s2)-q))/k
    T4=T2
    P=T1+T2+T3+T4

    I1= h*T1+((s1-h)/k)*np.sinh(k*T1)+(q/k**2)*(np.cosh(k*T1)-1)
    I2= ((s1-s2)/2)*T2
    I3= -h*T3+((-s2+h)/k)*np.sinh(k*T3)-(q/k**2)*(np.cosh(k*T3)-1)
    I4= I2
    av= (I1+ I2+ I3+ I4)/P
    Z= ((h-av)/h)/2
    
    CFZ= ((Z-Z_var)**2)/DZ_var**2
    CFP= ((P-P_var)**2)/DP_var**2
    CFA= ((A-A_var)**2)/DA_var**2
    CF= CFZ + CFP + CFA
#    PDF= np.exp(-CF/2)
    return CF


# minimize CF maximize PDF
def objective(x):
    return calcCF(x)


qGuess = 1
s1_s2Guess = 1
deltaGuess = 1

x0 = np.array([qGuess,s1_s2Guess,deltaGuess])

sol=minimize(objective,x0,method='SLSQP',options={'disp':True})

xOpt = sol.x


s1Opt = S1(xOpt)
s2Opt = S2(xOpt)

  

print('q: ' + str(xOpt[0]))
print('s1_s2: ' + str(xOpt[1]))
print('delta: ' + str(xOpt[2]))
print('s1: ' + str(s1Opt))
print('s2: ' + str(s2Opt))








 


