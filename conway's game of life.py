#%%
import numpy as np
matrixSize=1000
n=matrixSize

cycles=6
m=cycles

states = {}

A = np.random.randint(2,size=(n,n))
A1 = np.zeros(shape=(n,n))

def padded(matrixA):
    Apad = np.pad(matrixA,[(1,0),(1,0)],mode='constant')
    Apadded = np.pad(Apad,[(1,0),(1,0)],mode='constant')
    return Apadded
    
print("Starting with State 0 with A0:")
print(A)


for k in range(m):
    Ap = padded(A)

    Aleft = Ap[1:n+1,0:n]
    Aright = Ap[1:n+1,2:n+2]
    Atop = Ap[0:n,1:n+1]
    Abottom = Ap[2:n+2,1:n+1]

    Aresult = Aleft + Aright + Atop + Abottom

    for i in range(n):
        for j in range(n):
            if A[(i,j)] == 1 and Aresult[(i,j)] < 2 or Aresult[(i,j)] > 3:
                A1[(i,j)] = 0 # death
            elif A[(i,j)] == 1 and 1< Aresult[(i,j)] <4:
                A1[(i,j)] = 1 # survive
            elif A[(i,j)] == 0 and Aresult[(i,j)] == 3:
                A1[(i,j)]= 1 # birth
    
    print("We proceed to State " + str(k +1)+ ", where FALSE indicates a change of state:")
    print(A==A1)
    print("Resulting in A" + str(k +1)+ ": \n{}".format(A1))
    A = A1
    A1 = np.zeros(shape=(n,n))





# %%
