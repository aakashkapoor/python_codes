# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 18:05:41 2018

@author: Delol
"""
str1 = raw_input ("Enter the string")
dict1 = {}
for n in str1:
   
    keys = dict1.keys()
    if n in keys:
        dict1[n] += 1
    else:
        dict1[n] = 1
print dict1