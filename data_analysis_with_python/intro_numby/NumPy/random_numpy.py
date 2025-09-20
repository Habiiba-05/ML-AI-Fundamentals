# random numpy generation 

# create random data from scratch:
# generate random arrays that follow the -
# uniform distribution     np.random.rand()
# normal distribution      np.random.randn()
# integers      np.random.randint(low, high, size numbers)

# seed:
# The number that the computer starts from to generate random numbers.     np.random.seed()
    


import numpy as np

# Uniform distribution (0 to 1) 
uniform_arr = np.random.rand(2, 3)   # 2x3 array
print("Uniform distribution:\n", uniform_arr)

# Normal distribution (mean=0, std=1) 
normal_arr = np.random.randn(2, 3)
print("\nNormal distribution:\n", normal_arr)

# Random integers 
int_arr = np.random.randint(1, 10, (2, 3))   # numbers from 1 to 9
print("\nRandom integers:\n", int_arr)

# Seed (to get repeatable results)
np.random.seed(42)    # set seed
repeat_arr = np.random.randint(1, 10, (2, 3))
print("\nWith seed (repeatable):\n", repeat_arr)


# Key points:
# rand() → uniform between 0 and 1.
# randn() → normal distribution (bell curve).
# randint(low, high, size) → integers in given range.
# seed(n) → fix the randomness, so every run gives the same result.