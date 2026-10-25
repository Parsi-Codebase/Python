import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
#Access the element on the first row, second column:
print('2nd element on 1st row: ', arr[0, 1])  # Output: 2
print('3rd element on 2nd row: ', arr[1, 2])  # Output: 8
#Access the element on the 2nd row, 5th column:
print('5th element on 2nd row: ', arr[1, 4])  # Output: 10
#Print the last element from the 2nd dim:
print('Last element from 2nd dim: ', arr[1, -1])  # Output: 10