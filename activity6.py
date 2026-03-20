#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:58:44 2026

@author: izzy.araojo
"""

import numpy as np
import pandas as pd

#create numpy array of shape (3,5) w/ random values 1-100
arr = np.random.randint (1, 101, (3,5))
print(arr)

#create DataFrame w/ index a, b, c and columns 1, 2, 3, 4, 5
frame = pd.DataFrame(arr, index = ['a', 'b', 'c'], columns = [1, 2, 3, 4, 5])
print('DataFrame:')
print(frame)

#transpose DataFrame
frame = frame.T
print('Transposed DataFrame:')
print(frame)

#change all values less than 40 to 0
frame[frame < 40] = 0
print('Changed Values less than 40 to 0:')
print(frame)

