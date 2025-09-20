# NumPy

# NumPy: a fundamental library for working with large datasets
# Arrays: support multidimensional arrays and multiple data types
# Integration: works efficiently with C/C++ for speed

# Basics:
# - Create arrays from Python lists or tuples using np.array()
# - Array attributes: understand key attributes
#     ndim: number of dimensions
#     shape: size of each dimension
#     size: total number of elements
# - data type: all elements share a single data type

# Key features:
# Fast mathematical functions
# Vectorization (much faster than Python loops)
# Broadcasting (operations between arrays of different shapes)
# Tools for linear algebra, random numbers, FFT
# Memory-efficient storage


# craete a one/two dimensional numpy array from a list:

# one - 1D
import numpy as np

data1 = [1, 2, 3, 4]
array1 = np.array(data1)

print("array1:", array1)
print("size:", array1.size)
print("shape:", array1.shape)
print("dimensions:", array1.ndim)
print("data type", array1.dtype)


# two - 2D
import numpy as np 

data2 = [1, 2, 3, 4], [5, 6, 7, 8]
array2 = np.array(data2)

print("array2:", array2)
print("size:", array2.size)
print("shape:", array2.shape)
print("dimensions:", array2.ndim)
print("data type", array2.dtype)