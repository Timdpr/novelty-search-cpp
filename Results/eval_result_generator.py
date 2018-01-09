# -*- coding: utf-8 -*-
"""
Creates useful statistics and visualisations of results in evaluation files

Created on Sat Dec  2 08:30:56 2017
@author: tp275
"""
import numpy as np
import matplotlib.pyplot as plt

def getList(i):
    """
    Returns values in evaluations file as list
    i = 'evaluationsxxx' filename suffix eg. evaluations250.txt
    """
    input_text = open("evaluations" + str(i) + ".txt","r")
    
    text = input_text.read()
    text = text.split(" \n")
    text = text[:-1]
    
    evalList = []
    for s in text:
        evalList.append(int(s))
    return evalList


meanList = []
allList = []
devList = []

# archive size limits of tests (700 is actually off entirely)
testList = [0,5,10,15,20,25,30,40,50,75,100,250,500,700] #,250,500,700

for i in testList:
    evalList = getList(i) # get relevant eval. result file
#    ttest = scipy.stats.ttest_ind(evalList,offList)
    mean = np.mean(evalList)
    stDev = np.std(evalList)
    
    # toggle these for outlier removal
    # removes runs above or below 2 * standard dev.
#    evalList = [x for x in evalList if (x > mean - 2 * stDev)]
#    evalList = [x for x in evalList if (x < mean + 2 * stDev)]
#    mean = np.mean(evalList)
#    stDev = np.std(evalList)
    
    print("Archive size: " + str(i))
    print("Solved runs: " + str(len(evalList)) + "/40")
    print("Max. evaluations: " + str(max(evalList)))
    print("Min. evaluations: " + str(min(evalList)))
    print("Mean: " + str(mean))
    print("Standard deviation: " + str(stDev))
    print()
    
    for e in evalList:
        allList.append(e)
        
    meanList.append(mean)
    devList.append(stDev)

# Hist 1
plt.hist(allList, bins=50)
plt.xlabel("Mean evaluations")
plt.ylabel("Number of runs")
plt.xlim(0,500000)
plt.show()
plt.clf()

# Hist 2
plt.hist(allList, bins=100)
plt.xlabel("Mean evaluations")
plt.ylabel("Number of runs")
plt.xlim(0,200000)
plt.show()

# Graph 1
plt.figure(figsize=(6,4))
plt.scatter(testList, meanList)
plt.errorbar(testList, meanList, yerr=devList, fmt="none")
plt.plot(testList, meanList, 'r')
plt.xlabel("Archive size")
plt.ylabel("Mean evaluations")
plt.xlim(-5,105)
plt.ylim(-40000,125000)
plt.show()
plt.clf()

# Graph 2
plt.scatter(testList, meanList)
plt.errorbar(testList, meanList, yerr=devList, fmt="none")
plt.plot(testList, meanList, 'r')
plt.xlabel("Archive size")
plt.ylabel("Mean evaluations")
plt.xlim(-10,710)
plt.ylim(-40000,125000)
plt.show()
