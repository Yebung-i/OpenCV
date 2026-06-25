import numpy as np

A = np.array([[1,1,1,1], [2,-1,2,-1], [3,2,-1,2], [1,3,2,-1]])
B = np.array([10,3,11,9])

A_inv = np.linalg.inv(A)

solution = A_inv @ B

w,x,y,z = solution

print(f"w : {w:.1f}, x : {x:.1f}, y : {y:.1f}, z : {z:.1f}")

