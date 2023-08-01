#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 16:17:11 2023

@author: stephaniecolon
"""


from scipy.optimize import fsolve 
import numpy as np
import matplotlib.pyplot as plt

"""
find x such that 0 = f(x)
"""

# right -hand -side
def f(x):
    return np.exp(x) - 4*x

# initial guess
x0 = 1

# solve statment assings solution to x
"""
when x0 is guessed, fsolve gives the x nearest to x0
"""
x = fsolve(f, x0)
print(x)

x_array = np.arange(1,10,0.5)
f_array = f(x_array)
plt.plot(x_array, f_array)




