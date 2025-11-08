## unit-3 ##
#3.2) Write a NumPy program using NumPy methods max, min,
#argmax, argmin, argmax, repr, count, bincount, unique.
#a.)To extract all numbers from a given array,
#which are less and greater than a specified number.

import numpy as np

arr = np.array([1, 5, 8, 10, 3, 7])
num = 5

less_than = arr[arr < num]
greater_than = arr[arr > num]

print(less_than)
print(greater_than)
