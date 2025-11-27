# create numpy arrays from files 

# load data use function - np.load(), np.loadtxt():
# and we used them to read data from a text or binary fil.
# numpy format can read and write - text, csv, and binary  .npy format

import numpy as np

# create array
data = np.array([[1, 2, 3], [4, 5, 6]])

# save to CSV
np.savetxt("data.csv", data, delimiter=",", fmt="%d")

# load back from CSV
loaded_csv = np.loadtxt("data.csv", delimiter=",", dtype=int)

print("Loaded data:\n", loaded_csv)
