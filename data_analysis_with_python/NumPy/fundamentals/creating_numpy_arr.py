# creating numpy arrays 

# ready-made functions:
# scratch - np.zeros() , np.full() , np.eye() , etc
# sequance array - np.arange():
# using np.linspace(): - number of evenly space
# random using - np.random()


# create arrays with diffrent functions
import numpy as np

# ready-made arrays
zeros_array = np.zeros((2, 3))
ones_array = np.ones((2, 3))
full_array = np.full((2, 3), 7)
identity_matrix = np.eye(3)
empty_array = np.empty((2, 3))

# seqyence arrays 
arange_array = np.arange(0 , 10, 2)
linspace_array = np.linspace(0, 1, 5)

# random array 
random_array = np.random.rand(2,3)
random_int_array = np.random.randint(1, 10, (2, 3))

print("Zeros:\n", zeros_array)
print("Ones:\n", ones_array)
print("Full:\n", full_array)
print("Identity:\n", identity_matrix)
print("Empty:\n", empty_array)
print("Arange:\n", arange_array)
print("Linspace:\n", linspace_array)
print("Random float:\n", random_array)
print("Random int:\n", random_int_array)