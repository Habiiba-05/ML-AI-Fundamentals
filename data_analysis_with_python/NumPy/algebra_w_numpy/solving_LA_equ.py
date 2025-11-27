# solving linear equation

# for ex  AX=B  (find X),
# using  np.linalg.solve() - requirement: A is square matrix and invertible.
# verification: check solution by computing A @ B and comparing it with B 

import numpy as np 

a = np.array([[1, 2], [3, 4]])
b = np.array([1, 2])

# solution
solution = np.linalg.solve(a, b)
print("solution:", solution)

# verification
verfication = a @ solution
print("verfication:", verfication)
print("original b:", b)