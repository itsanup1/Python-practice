import numpy as np

#arr1 = np.array([[1,2,3,4,5,6],
#                            [7,8,9,10,11,12],
#                            [13,14,15,16,17,18],
#                            [19,20,21,22,23,24],
#                            [25,26,27,28,29,30],
#                            [31,32,33,34,35,36]])

arr1 = np.arange(1,37).reshape(6,6)
arr2 = np.arange(1,17)
arr3 = np.arange(1,5).reshape(2,2)
arr4 = np.arange(5,9).reshape(2,2)
A = np.array([[1,2,3],[2,1,1],[3,4,1]])
B = np.array([14,10,19])

matrix= arr2.reshape(4,4)
splitMatrix1 = np.hsplit(matrix,2)[0]
splitMatrix2 = np.hsplit(matrix,2)[1]
print(arr1)
print()
print(np.hstack((splitMatrix1,splitMatrix2)))
print()
print(np.dot(arr3 ,arr4))
print()



A = np.array([[1, 2, 3],
              [2, 1, 1],
              [3, 4, 1]])

B = np.array([14, 10, 19])

X = np.linalg.solve(A, B)
print(X)

#print(arr1)
#print('')
#print(arr2)
#print('')
#print(arr3)
#print('')
#print(arr4)
#print('')
#print( "Shape of arr2 is: " ,arr2.shape) #shape of array
#print('')
#print( "Dimensions of arr3 is: " ,arr3.ndim) #dimensions of array
#print('')
#print("Datatype of arr3 is: ",arr3.dtype) #datatype of array
#print('')
#print("Size of arr3 is: ",arr3.size) #Number of elements in an array
#print('')

#arr = np.arange(10) # [0 1 2 3 4 5 6 7 8 9]
#print(arr[2])        # Access a single element: 2
#print('')
#print(arr[1:5])      # Slice: [1 2 3 4]
#print('')
#print(arr[:5])       # Slice from the beginning: [0 1 2 3 4]
#print('')
#print(arr[5:])       # Slice to the end: [5 6 7 8 9]
#print('')
#print(arr[::2])      # Slice with a step: [0 2 4 6 8]
#print('')
