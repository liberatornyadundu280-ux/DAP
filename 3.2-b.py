#3.2) Write a NumPy program usingNumPy methods
#max, min, argmax, argmin, argmax, repr, count, bincount, unique.
#b.) To find the indices of the maximum and minimum numbers
#along the given axis of an array.

import numpy as np

arr2d = np.array([[3, 7, 2],
                  [9, 5, 1],
                  [4, 6, 8]])

max_indices_col = np.argmax(arr2d, axis=0)
max_indices_row = np.argmax(arr2d, axis=1)
min_indices_col = np.argmin(arr2d, axis=0)
min_indices_row = np.argmin(arr2d, axis=1)

print(max_indices_col)
print(max_indices_row)
print(min_indices_col)
print(min_indices_row)
