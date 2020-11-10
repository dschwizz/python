#%%
import numpy
import pandas
import uuid
import random
from datetime import datetime
import networkx as nx
import matplotlib.pyplot as plt
import scipy
from sklearn.metrics.pairwise import cosine_similarity

F = nx.DiGraph()
ledger = {}

def skus():
    items = ["Paper","Fox","Lamp","Potatoe","Fur","Love","Madness","Amtrack","Cinnamon","Entropy","Unsettled","Manniquin"]
    SkuId = str(uuid.uuid4())
    SkuName = random.choice(items)
    sku = {"uuid" : SkuId, "desc" : SkuName}
    return sku

def entry():
    TransactionUid = str(uuid.uuid4())
    SKU1 = skus()
    SKU2 = skus()
    SKU3 = skus()
    TransactionSkus = [SKU1,SKU2,SKU3]
    transaction = {"uuid" : TransactionUid,  "contents" : [TransactionSkus[0],TransactionSkus[1],TransactionSkus[2]], "datetime" : datetime.now()}
    entry = sum(transaction.items(), ())
    return entry

i = 0
while i < 100:
    ledgerEntry = entry()
    entryID = ledgerEntry[1]
    desc1 = ledgerEntry[3][0]['desc']
    desc2 = ledgerEntry[3][1]['desc']
    desc3 = ledgerEntry[3][2]['desc']
    # entryTime = ledgerEntry[5]
    ledger[entryID] = [desc1,desc2,desc3]
    i += 1

F = nx.DiGraph(ledger)
nx.draw(F,with_labels=False)
plt.draw()
plt.show()

adjF = nx.adjacency_matrix(F) #nx.to_numpy_array(F) #creates adjacency matrix of graph F
# similarities = cosine_similarity(adjF)
# print('pairwise dense output:\n {}\n'.format(similarities))

#also can output sparse matrices
similarities_sparse = cosine_similarity(adjF,dense_output=False)
print('pairwise sparse output:\n {}\n'.format(similarities_sparse))

# c = adjF@adjF #comput inner product

# %%
