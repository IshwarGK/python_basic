import numpy as np

np_arr1 = np.array([1, 2 ,3])

np_arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print(np_arr1 + np_arr2)

print(np_arr1 + 3)

arr1 = np.array([[1, 2, 3], [4, 5, 6]])  # Shape: (2, 3)
arr2 = np.array([[1], [2]])                  # Shape: (2,)

print(arr1 + arr2)