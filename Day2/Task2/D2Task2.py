import numpy as np

A = np.array([[1,2,3],[-1,3,-10]])
B = np.array([[2,-1],[3,1],[0,5]])


AB = np.zeros(A.shape[0], B.shape[1])

for i in range(A.shape[0]):
    for j in range(B.shape[1]):
        for k in range(A.shape[1]):
            AB[i][j] += A[i][k] * B[k][j]
