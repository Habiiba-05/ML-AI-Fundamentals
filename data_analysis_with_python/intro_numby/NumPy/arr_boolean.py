# array boolean

# I use it for filtering.
# boolean mask - create body array based on condition that is lead to 
# filter data and combining condition AND, OR, NOT


import numpy as np

# Create an array
arr = np.array([5, 10, 15, 20, 25])

# Simple condition: values > 10
mask = arr > 10
print("Boolean mask:", mask)        # [False False  True  True  True]
print("Filtered:", arr[mask])       # [15 20 25]

# Combine conditions (AND, OR, NOT)
print("arr[(arr > 10) & (arr < 25)] =", arr[(arr > 10) & (arr < 25)])   # between 10 and 25
print("arr[(arr < 10) | (arr > 20)] =", arr[(arr < 10) | (arr > 20)])   # less than 10 OR greater than 20
print("arr[~(arr > 15)] =", arr[~(arr > 15)])                           # NOT greater than 15
