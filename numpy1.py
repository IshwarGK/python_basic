import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)


arr2 = np.array([[1, 2, 3, 4, 5], [22, 33, 11, 44, 55]])

print(arr2)

zeros_arr1 = np.zeros((3, 4))

print(zeros_arr1)

arr2 = np.array([3, 3, 3, 3, 3])

arr_add = arr1 + arr2
print(arr_add)

arr_multi = arr1 * arr2
print(arr_multi)


# dot product

dot_product = np.dot(arr1, arr2)
print(dot_product)

arr1 = np.array([[1, 2], [3, 4]])
result = np.transpose(arr1)
print(result)

arr1 = np.array([1, 2, 3, 4, 5])
slice1 = arr1[1:4]
print(slice1)

print(arr1[2])

mask = arr1 > 3
result = arr1[mask]
print(result)

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr1.shape)

arr2 = arr1.reshape(3,2)
print(arr2)

arr1 = np.array([[1, 2, 3], [4, 5, 6]])

total_sum = np.sum(arr1)
print(total_sum)

mean1 = np.mean(arr1)
print(mean1)

max1 = np.max(arr1)
min1 = np.min(arr1)

print(max1)
print(min1)