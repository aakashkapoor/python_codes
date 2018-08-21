# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 19:13:57 2018

@author: Delol
"""
"""
The below code iterates to every element and join each character in the beginning so as to obtain the reversed string.
"""

s = raw_input("Enter a string you want to reverse")
    #to enter a user defined string
def reverse(s):
    #Reverse method made for the reversal of string
  str1 = ""
  
  for i in s:
      #for loop for a key element search in user defined string
    str1 = i + str1
        # Concadination of str with i 
  return str1
    # return of the reversed string
    
print("The original string is:",s)

print("The reversed string is:",reverse(s))
 
