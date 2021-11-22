# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 00:14:27 2021

@author: pmjum
"""

import random
import matplotlib.pyplot as plt
import numpy as np

profits = {1:-2,15:-1.5,30:-1,40:-.5,50:0,70:1,90:2,99:3,100:5}
breakpoints = [1,15,30,40,50,70,90,99,100]

def rollMaintenance(profits,breakpoints,bonus=0):
    roll = random.randint(1,100)
    #print("rolled a ", roll)
    roll = max(min((roll + bonus),100),1)
    #print("new roll: ", roll)
    for point in breakpoints:
        if(roll <= point):
            return(profits[point])
        

def calculateAverageMaintenance(numDays, profits, breakpoints, baseMaintenance=1, bonus=0):
    totalProfit = 0
    for x in range(numDays):
        totalProfit += (baseMaintenance * rollMaintenance(profits, breakpoints, bonus))
        #print("new daily maintenance: ", totalProfit)
    return totalProfit / numDays

def runSims(numTrials, profits, breakpoints, numDays=7, baseMaintenance=1,bonus=0):
    profitResults = []
    numPositive = 0
    numNegative = 0
    for x in range(numTrials):
        trial = calculateAverageMaintenance(numDays, profits, breakpoints, baseMaintenance, bonus)
        profitResults.append(trial)
        if(trial > 0):
            numPositive += 1
        else:
            numNegative += 1
    return (profitResults,numPositive/numTrials,numNegative/numTrials)

def getCounts(profitResults,returnList=True):
    resultVals = list(set(profitResults))
    resultCounts = [profitResults.count(val) for val in resultVals]
    if(returnList):
        return(resultVals,resultCounts)
    else:
        return {resultVals[i]:resultCounts[i] for i in range(len(resultVals))}
    
results,percentPositive,percentNegative = runSims(10000,profits,breakpoints,bonus=0)
print("Percent Positive: ",percentPositive)
print("Percent Negative: ", percentNegative)
print("Standard Deviation: ", np.std(results))
print("Mean: ", np.mean(results))

(resultVals,resultCounts) = getCounts(results)
plt.bar(resultVals,resultCounts)
plt.show()


