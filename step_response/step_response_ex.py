# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 12:45:53 2021

@author: Aerial
"""

import numpy as np
import control as ctrl
import matplotlib.pyplot as plt
import scipy.signal as signal
# TF = 3s / 5s^2 + 6s + 7
num = np.array([3])
denum = np.array([5, 6, 7])
TF = ctrl.tf(num, denum)
print('TF =', TF)

t, y = ctrl.step_response(TF)
plt.xlabel("t")
plt.ylabel("y")
plt.plot(t, y, color="orange")
