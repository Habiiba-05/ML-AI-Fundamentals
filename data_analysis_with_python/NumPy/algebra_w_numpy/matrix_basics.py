# matrix operating basics

# dot product: compute dot product of two arrays using   np.dot() or @ operator
# matrix multiplication: create array with evenly spaces values
# transpose: swith row and column using  .T


import numpy as np 

# dot product
a = np.array([1, 2, 3, 4])
b = np.array([1, 3, 5, 7])

dot1 = np.dot(a, b)
dot2 = a @ b
print("dot product:", dot1, dot2)
# key point: dot = a.b = (1.1)+(2.3)+(3.5)+(4.7)=50


# Quick summary (rule of thumb):

# 1D arrays (vectors):
#   np.dot or @  → computes dot product = scalar
# 2D arrays (matrices):
#   np.dot or @  → performs matrix multiplication (not scalar)
# Element-wise multiplication (each element multiplied by the same position):
#   use * directly (not dot/@)


# matrix multiplication
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 2], [3, 4], [5, 6]])

multi = a @ b
print("multiplication:", multi )

# transpose
import numpy as np

M = np.array([[1, 2, 3], 
              [4, 5, 6]])

print("original:\n", M)
print("transpose:\n", M.T)