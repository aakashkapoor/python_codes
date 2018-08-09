# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 17:05:11 2018

@author: Delol
"""

string=raw_input("Enter string:")
count1=0
count2=0
for i in string:
    if i.isdigit():
        count1=count1+1
    elif i.isalpha():
        count2=count2+1
  
print("The number of digits is:")
print(count1)
print("The number of characters is:")
print(count2)