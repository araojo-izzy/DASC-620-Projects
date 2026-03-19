#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 22:44:37 2026

@author: izzy.araojo
"""

breakfast = ['apple', 'egg', 'ham', 'donut', 'bagels', 'sausage']
result  = list(filter(lambda x: len(x) > 3, breakfast)) 
#len(x)>3 tells says to include the items if their length is greater than 3

print(result)
