import numpy as np

A = np.array([[1,2,3],[10,-1,-5],[6,7,5]])

res = np.linalg.matrix_power(A,3) - 5*np.linalg.matrix_power(A,2) - 4*A -98*np.eye(3,3)
print(res)
