#!/usr/bin/env python
# coding: utf-8

# In[147]:


#%%
import numpy
import pandas as pd
import uuid
import random as r
from numpy import random as rand
from datetime import datetime
import networkx as nx
import matplotlib.pyplot as plt
import scipy
from sklearn.metrics.pairwise import cosine_similarity
import time
###questions###
"""
Is this even a Monte Carlo simulation?
Can the class include more things?
probability of a sales is not poisson, but sum of poisson for bin > 0...

Paralellize this code so you can run multiple simulations at once:
https://www.machinelearningplus.com/python/parallel-processing-python/
"""

###plot settings###
# plt.rcParams['figure.figsize'] = [20, 10]

# ###empty data structures###
salesProb=[]
basketSizeProb=[]

###create random probability distributions for ledger###
poissonX = rand.poisson(4,12) #generate list containing random sample from poisson distribution of 12 bins and lamba = 4
EpoissoX = sum(poissonX) #sum of list poissonX

for n in poissonX: 
    salesProb.append(1-(n/EpoissoX)) #list of  poissonX / sum(poissonX) (some random percentage...)

exponentialX = rand.poisson(1,12) #generate list containing random  sample from poisson distribution of 12 bins and lamba = 1
EexponentialX = sum(exponentialX) #sum of list of exponentialX

for n in exponentialX: 
    basketSizeProb.append(1-(n/EexponentialX)) #list of exponentialX/sum(exponentialX)  (some random percentage...)

###member and item lists###
# membership = r.randint(1000000,10000000,100) #generate list of 100 random numbers between 1,000,000 and 9,999,999 
items = ["None","Paper","Fox","Lamp","Potato","Fur","Love","Madness","Amtrack","Cinnamon","Entropy","Underpants","Manniquin"]
itemsNum = list(range(1,13))
###classes###
class randomLedgerEntry():
    def __init__(self):
        # self.members = membership
        self.items = itemsNum

    def skuGenerator(self,q):
        SkuName = r.choices(self.items,k=q,weights=salesProb)
        return SkuName
    
def entryGenerator1(x):
    q =r.choices(list(range(1,13)),weights = basketSizeProb)
    contents=x.skuGenerator(q[0])
    return contents

###assign class###
x=randomLedgerEntry()

###set ledger size###
transactionCount = 1000

###set attempts###
attempts = [range(100),range(1000),range(10000),range(100000),range(1000000)]

###empty dataframe for results###
simulationResults = pd.DataFrame()
print(salesProb)
print(basketSizeProb)
#%%


# In[ ]:



###Ledger Building functions###
print("Run started at: " + time.localtime())
def buildTransactionArray():
    ledgerList=[entryGenerator1(x) for z in range(transactionCount)]
    length = max(map(len, ledgerList))
    transactionArray=numpy.array([ledgerListi+[0]*(length-len(ledgerListi)) for ledgerListi in ledgerList])
    transactionMatrix = numpy.matrix(transactionArray)
    return transactionMatrix #this is n X m. we need an n X n adjacency matrix for a graph

#     return ledger
#%%
simStart = time.perf_counter()
for m in range(5):
    start = time.perf_counter()
    frequencyDf = pd.DataFrame(index = items)
    for n in attempts[m]:
        start1 = time.perf_counter()

        ###build the transaction ledger###
        Tmatrix = buildTransactionArray()
        number_list = numpy.array(Tmatrix)
        (unique, counts) = numpy.unique(number_list, return_counts=True)
        
        frequencies = dict(zip(*(unique, counts)))

        frequencyDf[str(n)] = frequencies.values()

    simulationResults["Attempt #" + str(n+1) + " Mean"] =  frequencyDf.mean(axis=1)
    simulationResults["Attempt #" + str(n+1) + " StndDev"] =  frequencyDf.std(axis=1)
    end = time.perf_counter()
    print("This loop took " + str(end - start) + " seconds to run.")

simEnd = time.perf_counter()
print("All sims took " + str(simEnd - simStart) + " seconds to run.")
print(simulationResults)





