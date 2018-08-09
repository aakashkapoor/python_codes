# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 19:03:07 2018

@author: Delol
"""
items = input('Enter your list: ')
def sum13(nums):
  items = len(nums)
  tot = 0

  if items==0:
    return 0

  for x in range(items):
    if nums[x]!=13:
      if nums[x-1]!=13:
        tot+=nums[x]

  return tot
print sum13(items)