# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 18:36:03 2018

@author: Delol
"""

import string
#Include library for string operations

def checkPangram(vals):
        #Defination called for checking the pangram
	for val in vals:
        #For loop to check each values of alphabet
		if (val < 1):
            # If no total alphabets found
			return False
        
	return True
        #For the total alphabets found

chars = string.lowercase 
    # list of all lowercase letters so that each alphabet is treated equally
alphabet = {}

# this loop fills the alphabet dictionary with letters as keys and zeros as values
for char in chars:
	alphabet[char] = 0

inpStr = raw_input("Please enter the string you wanna check for pangram:> \n")


# analyze the input string after switching all of its letters to lowercase
for c in inpStr.lower():
    #for loop to check each letter in the input string that is converted to lower
	if c in chars:
        # checking the characters in full aphabet if found incremented by +1
		alphabet[c] += 1

vals = alphabet.values()

# call the check function and pass the list of values to it
pang = checkPangram(vals)
"""
If case used to display the final check result whether the input string satisfies or not.
"""
if (pang):
	print "it's a pangram"
else:
	print "not a pangram"