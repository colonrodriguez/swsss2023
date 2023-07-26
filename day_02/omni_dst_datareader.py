#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 15:47:02 2023

@author: stephaniecolon
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as datetime

f = open("omni_test.lst")               # open file
line1 = f.readline()                    # read line 1
line2 = f.readline()                    # read line 2
print(line1)
print(line2)
f.close()

with open("omni_test.lst") as f:
    for line in f:
        print(line)
        
# nLines = 3                              # number of lines with headers 
                                        # we don't need
with open("omniweb.gsfc.nasa.gov_staging_omni_min_def_Ms5LtiyPpM.lst.txt") as f:
    
    # """ PART 1: Skip first 3 lines """
    # for i in range(nLines):
    #     print(f.readline())
        
    # """ PART 2: read line 4 with headers """
    # header = f.readline() 
    # variables = header.split()
    
    """ PART 3: read data and convert to numerical values """
    year = []
    day = []
    hour = []
    minute = []
    dst = []
    for line in f:
        data = line.split()
        year.append(int(data[0]))
        day.append(int(data[1]))
        hour.append(int(data[2]))
        minute.append(int(data[3]))
        dst.append(int(data[4]))

minute_array = np.array(minute)
dst_array = np.array(dst)

datetime_list = []
for y, d, h, m in zip(year, day, hour, minute):
    timedelta = datetime.datetime(2013,1,1,0,0,0) + \
                datetime.timedelta(days = d-1, hours = h, minutes = m)
    datetime_list.append(timedelta)
    print(timedelta)
datetime_array = np.array(datetime_list)
print(datetime_array)

plt.plot(datetime_array, dst_array)
plt.title('Dst Index from March 16 - March 21, 2013')
plt.xlabel('UT (YY:MM:DD)')
plt.ylabel('Dst (nT)')
plt.xticks(rotation=45)
plt.show()


        