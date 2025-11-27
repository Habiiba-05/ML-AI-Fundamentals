# array math operating

# element-wise operations - Operations that are performed on each part separately.
# broad casting - can perform operations on arrays of different shapes (together).

# element-wise
import numpy as np

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print("a + b =", a + b)

print("a * b =", a * b)


# broad casting
x = np.array([1, 2, 3])
y = 10   # scalar

print("x + y =", x + y)

m = np.array([[1], [2], [3]])   # shape (3,1)
n = np.array([10, 20, 30])      # shape (3,)
print("m + n =\n", m + n) 