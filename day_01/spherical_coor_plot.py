#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 15:01:02 2023

@author: stephaniecolon
"""

""" A 3D plot script for spherical coordinates
"""

import numpy as np
import matplotlib.pyplot as plt

__author__ = 'Stephanie Colón-Rodríguez'
__email__ = 'stephcr@umich.edu'

""" Create arrays with the same length (num=100) to use as inputs for 
    the functions """
r_array = np.linspace(start=0, stop=1, num=100)
theta_array = (np.linspace(start=0, stop=360, num=100))*(np.pi/180)
phi_array = np.linspace(start=0, stop=360, num=100)*(np.pi/180)

""" Create Function that converts to cartesian coordinates"""
def spherical_conv(r, theta, phi):
    x = r*np.sin(phi)*np.cos(theta)
    y = r*np.sin(phi)*np.sin(theta)
    z = r*np.cos(phi)
    
    return(x,y,z)

""" Unit testing """
assert np.allclose(spherical_conv(1,0,0), (0,0,1)), \
    "error"
assert np.allclose(spherical_conv(1,np.pi,np.pi), (0,0,-1)), \
    "error"
assert np.allclose(spherical_conv(1,2*np.pi,2*np.pi), (0,0,1)), \
    "error"
assert np.allclose(spherical_conv(1,-1*np.pi,-2*np.pi), (0,0,1)), \
    "error"
assert np.allclose(spherical_conv(1,-2*np.pi,np.pi), (0,0,-1)), \
    "error"

""" For each element in the arrays, run the function """
for r,theta,phi in zip(r_array, theta_array, phi_array):
    print('x,y,z:', spherical_conv(r, theta, phi))

""" Plot """
fig = plt.figure()  # better control
axes = fig.gca(projection='3d')  # make 3d axes
x, y, z = spherical_conv(r_array, theta_array, phi_array)
axes.plot(x, y, z)
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_zlabel('z')
axes.set_title('3D Plot of Cartesian Coordinates')