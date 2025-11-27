# linear algebra and matrix operating basics

# determinate: np.linalg.det(matrix)
# inverse: np.linalg.inv(matrix)
# eignvaluse, eignvectors: np.linalg.eig(matrix)

import numpy as np

matrix = np.array([[1, 2],
                   [5, 6]])

determenate = np.linalg.det(matrix)
print("determenate:", determenate)
# (6.1)-(2.5)=-4

inverse = np.linalg.inv(matrix)
print("inverse:", inverse)

eignvaluse, eignvectors = np.linalg.eig(matrix)
print("eignvaluse, eignvectors:", eignvaluse, eignvectors)