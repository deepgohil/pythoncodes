import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print("\n",arr)

print(type(arr))

arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("\n",arr2)

print("Number of dimensions:",arr2.ndim)

print("\nArray Indexing:")

print(arr[2] + arr[3])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print("\nAccessing in 2D array:",arr)

print('5th element on 2nd row: ', arr[1, 4])

print('\nLast element from 2nd dim: ', arr[1, -1])

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

print("\nSlicing in array", arr)

print(arr[4:])

print("\nSlicing in array using step:")

print(arr[1:10:2])

arr = np.array([3, 2, 0, 1])

print('\nSorting array', arr)

print(np.sort(arr))

arr = np.array(['banana', 'cherry', 'apple'])

print('\nSorting array',arr)

print(np.sort(arr))