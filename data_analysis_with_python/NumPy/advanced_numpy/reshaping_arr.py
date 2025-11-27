# re-shaping arrays

# reshape: change array's dimensions using    reshape()
# flatten: convert multi-dimensions arrays to 1D  using   flatten(), ravel()
# reshape rules: total number of elements remain the same

import numpy as np

array = np.arange(12)
print("original array", array)

# reshape to 3x4
reshaped_array = array.reshape(3, 4)
print("reshaped_array:", reshaped_array)

# reshape to 2x2x3
reshaped_array_3D = array.reshape(2, 2, 3)
print("reshaped_array_3D:", reshaped_array_3D)

# flatten to array
flattened_array = reshaped_array.flatten()
print("flattened_array:", flattened_array)