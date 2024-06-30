import numpy as np

n = np.arange(20)
arr = np.reshape(n, [4, 5])
print("Original array:")
print(arr)

print([0, 1, 2, 3, 4] in arr.tolist())
print([0, 1, 2, 3, 5] in arr.tolist())
print([15, 16, 17, 18, 19] in arr.tolist())
