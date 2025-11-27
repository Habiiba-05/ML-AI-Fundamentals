# array manipulation 

# Array Manipulation in NumPy = ways to reshape, join, split, or change elements inside arrays.
# Some of the most common operations:
# Reshape → change the shape of the array without changing the data.
# Flatten / Ravel → convert a multi-dimensional array to 1D.
# Stack / Concatenate → join arrays together.
# Split → break an array into parts.

import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5, 6])

# 1) Reshape into 2D (2 rows, 3 columns)
reshaped = arr.reshape(2, 3)
print("Reshaped:\n", reshaped)

# 2) Flatten back to 1D
flattened = reshaped.flatten()
print("\nFlattened:", flattened)

# 3) Stack arrays vertically and horizontally
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

v_stack = np.vstack((a, b))   # vertical stack
h_stack = np.hstack((a, b))   # horizontal stack

print("\nVertical Stack:\n", v_stack)
print("\nHorizontal Stack:\n", h_stack)

# 4) Split array into 3 parts
split_arr = np.split(arr, 3)
print("\nSplit into 3 parts:", split_arr)
