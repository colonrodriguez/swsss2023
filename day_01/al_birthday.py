#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 15:02:07 2023

@author: stephaniecolon
"""

#Import Libraries
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from swmfpy.web import get_omni_data
import numpy as np

#Set start and endtime based on my birthday is October 1 1999
start_time = datetime(1999, 10, 1)
end_time = datetime(1999, 10, 2)

#Obtain data for specified timeframe
data = get_omni_data(start_time, end_time)

#Plot AL as a function of time
x = data['times']
y = data['al']
plt.plot(x, y)
plt.xlabel('Datetime (Month-Day HH)')
plt.ylabel('Auroral Electrojet (nT)')
plt.title('AL during October 1st, 1999')
plt.xticks(rotation=45)
plt.show()