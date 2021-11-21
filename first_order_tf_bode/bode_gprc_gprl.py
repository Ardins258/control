# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 09:59:28 2021

@author: Aerial
"""

import control as cl
import matplotlib.pyplot as plt

R = 1e3
L = 100e-3
C = 500e-6

plt.figure()
GPRC = cl.tf([1], [(R*C), 1])
cl.bode(GPRC)

plt.figure()
GPRL = cl.tf([L,0],[L,R])
cl.bode(GPRL)

