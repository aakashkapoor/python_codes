# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 18:30:04 2018

@author: Delol
"""

for itr1 in range(50): 
    # We get the range of noumbers ranging between 0 to 50.
    if itr1 % 3 == 0 and itr1 % 5 == 0:
        # We here check the condition that whether the number is divisible by both 3 & 5.
        print("fizzbuzz")
            # If condition satisfies then instead of number print fizzbuzz.
        
    elif itr1 % 3 == 0:
          # In this loop we check whether the number is divisible by 3.
        print("fizz")
            # If condition satisfies then instead of number print fizz.
        
    elif itr1 % 5 == 0:
           # In this loop we check whether the number is divisible by 5.
        print("buzz")
           # If condition satisfies then instead of number print buzz.
    else:
        print(itr1)
          #The regular non divisible number is displayed.
