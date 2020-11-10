#%%
#install path: C:\Users\Danny\AppData\Local\Programs\Python\Python38-32

import numpy as np

A = np.random.randint(2, size = (4,4))
At=np.transpose(A)

C = A@A
print(A)
print(At)
print(C)

# %%
import networkx as nx
F = nx.Graph() # The graph F
F.add_node(1) # the integer 1 is a node in the graph F
F.add_nodes_from([2,3]) # the list [2,3] is a node in the graph F
E = nx.path_graph(10) # The Graph E, where the remaining integers from 0 to n are returned: what is a path graph?
F.add_nodes_from(E) # The nodes from the graph E are now nodes in the graph F
F.add_node(E) # The graph E is now a node in the graph F

print(F.nodes)

G = nx.watts_strogatz_graph(30,3,0.1)
print(G.nodes)
print(G.edges)
# print(nx.clustering(G))

 # %%
