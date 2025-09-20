# array type and casting 

# to use different data type i will use type casting using  .astype()
# why cast type? for memory optimization and compatibility:
# Save memory (e.g. use int8 instead of default int64).
# Compatibility (e.g. make sure your array matches another array’s dtype before operations).

import numpy as np

# Create array of integers
arr = np.array([1, 2, 3, 4, 5])
print("Original dtype:", arr.dtype)

# Cast to float
arr_float = arr.astype(float)
print("As float:", arr_float, "dtype:", arr_float.dtype)

# Cast to int8 (smaller memory)
arr_int8 = arr.astype(np.int8)
print("As int8:", arr_int8, "dtype:", arr_int8.dtype)

# Example: from string to int
str_arr = np.array(["10", "20", "30"])
num_arr = str_arr.astype(int)
print("String array:", str_arr, "-> Casted to int:", num_arr)


# Key idea:
# .astype(new_dtype) - makes a new array with the chosen type.
# Useful when handling large datasets where smaller dtypes save RAM.