#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 19:01:35 2026

@author: izzy.araojo
"""

import numpy as np
import pandas as pd
import math

#create numpy array of shape (3,5) w/ random values 1-100
arr = np.random.randint (1, 101, (3,5))
print(arr)

#create DataFrame w/ index a, b, c and columns 1, 2, 3, 4, 5
frame = pd.DataFrame(arr, index = ['a', 'b', 'c'], columns = [1, 2, 3, 4, 5])
print('DataFrame:')
print(frame)

#apply lambda funct to calc sq rt of each value
sqrt_frame = frame.map(lambda x: math.sqrt(x))
#DataFrame.applymap has been deprecated, need to use DataFrame.map instead
print('Square Root DataFrame:')
print(sqrt_frame)

#find sum of each row (axis = 1, across columns, gives one result per row)
print('Sum of Each Row:')
print(sqrt_frame.apply(lambda x: sum(x), axis = 1))
