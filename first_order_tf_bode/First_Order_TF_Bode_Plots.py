# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 12:02:24 2021

@author: Aerial
"""

import matplotlib.pyplot as plt
import control as c
#Transfer fucntion G1 = 1 / s 
#Transfer function G2 = 1 / 0.1s+1
G1 = c.tf([1],[1,0])
G2 = c.tf([1],[0.1,1])
## Show G1 and G2 in console
print(G1)
print(G2)

#Use control lib to plot bode 
#Make sure you label your bode plots as well
c.bode(G1,dB=True,label='$1 / s$')
c.bode(G2,dB=True,label='$1 / 0.1*s+1$')

#Legend 
plt.savefig("First_Order_TF_Bode_Plots.png",dpi=400)
plt.legend()
plt.show()

