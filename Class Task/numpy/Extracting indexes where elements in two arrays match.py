import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([5, 4, 3, 2, 1])
matching_indexes = np.where(array1 == array2)
print("Indexes where elements in the two arrays match:")
print(matching_indexes)
