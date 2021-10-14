# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 12:42:26 2021

@author: Aerial
"""
#Import lib
import numpy as np
import matplotlib.pyplot as plt
import control as c

#Define transfer function G and two compensators
G = c.tf([1],[1,0,0])
C1 = c.tf([1],[1,10])
C2 = c.tf([1,3],[1,10])

#show G C1 C2 in console
print(C1)
print(C2)
print(G)

#rlocus from control lib
c.rlocus(G)
c.rlocus(C1*G)
c.rlocus(C2*G)

