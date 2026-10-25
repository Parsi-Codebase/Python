#Create a 3-D array
#A 3-D array is an array with more than two dimensions.
#In the example below, we create a 3-D array with two 2-D arrays,
#each containing two arrays of three elements:
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)
print(arr.ndim) #ndim attribute returns the number of dimensions of the array