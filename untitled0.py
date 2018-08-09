# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 18:15:15 2018

@author: Delol
"""


fp = open("test.txt", "r")

print fp.read()

fp.seek(0)
print fp.readline()

fp.seek(0)
print fp.readlines()

fp.close()

fp.write("ios\n")
fp.writelines(["we \n", "are\n", "in\t", "write\t", "lines"])
fp.close()
print "work done"


