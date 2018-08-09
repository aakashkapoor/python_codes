# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 17:51:08 2018

@author: Delol
"""
items = input('Enter your list: ')



def centered_average(nums):
  items = len(nums)
  total = 0
  high = max(nums)
  low = min(nums)
  for num in nums:
    total += num
  aveg = (total -high-low) / (items-2)
  return aveg






print centered_average(items)