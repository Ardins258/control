# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 13:11:17 2021

@author: Aerial
"""

import numpy as np
import matplotlib.pyplot as plt 
import control as c

#Open-loop transfer function
GOL = c.tf([1],[1,3])
print(GOL)

#Closed-loop transfer function
#Set different amounts for k
k = 1
GCL = c.tf([k],[1,3+k])

#definte T and Y axis 
tout = np.linspace(0,5,100)
tout,yout = c.step_response(GCL,tout)
#plot
plt.figure()
plt.plot(tout,yout)
plt.show
