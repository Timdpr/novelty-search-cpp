# -*- coding: utf-8 -*-
"""
Prints results and stats for the 100 run, 250 archive limit, 'how large
is the archive size on completion' test.

Created on Thu Jan  4 18:15:59 2018
@author: tp275
"""
import numpy as np

def getList():
    """
    Returns values in arcSizes file as list
    """
    input_text = open("arcSizes.txt","r")
    
    text = input_text.read()
    text = text.split(" \n")
    text = text[:-1]
    
    sizesList = []
    for s in text:
        sizesList.append(int(s))
    return sizesList
    
sizesList = getList()

print("Mean: " + str(np.mean(sizesList)))
print("Std. dev: " + str(np.std(sizesList)))
print("Min size: " + str(min(sizesList)))
print("Max size: " + str(max(sizesList)))

count = 0
for i in sizesList:
    if i >= 100:
        count += 1
print("Number of 100 or over: " + str(count))
