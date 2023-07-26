#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:40:23 2023

@author: stephaniecolon
"""

import netCDF4 as nc
dataset = nc.Dataset('wfs.t06z.ipe05.20230725_203500.nc')

print(dataset)
total_electron_content = dataset['tec'][:]
total_electron_content_units = dataset['tec'].units

print(total_electron_content)
print(total_electron_content_units)