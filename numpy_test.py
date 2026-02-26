import numpy as np

array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20]])

#How to access a specific element in a 2D array
#Extract the second row
print(array[1:4,2:4])

#Extract the last column
print(array[:, 1])

print(array)


#How to select a range in a 2D array
print(array[1:3, 2:4])  # Selects rows 1 to 2 and columns 2 to 3 (0-indexed)

#How to crate a Numpy array from a list
 
arr = np.array([1, 2, 3, 4, 5])

print(arr)


##How to create a array of zeros

zeros = np.zeros((3,4))
print(zeros)

#Create a 4x4 array of ones
ones = np.ones((4,4))
print(ones)

#Create numbers from 0 to 20 using arange function 
numbers = np.arange(0,21)
print(numbers)

#How to create 10 evenly spaced numbers between 0 and 1 using linspace function
spaced_numbers = np.linspace(0, 1, 10)
print(spaced_numbers)

#create a 3x3 identity matrix
iden_matrix = np.eye(3)
print(iden_matrix)

#generate a 3x3 array of random numbers

random_matrix = np.random.rand(30)
print(random_matrix)


#How to find the shape of an array
print(random_matrix.shape)


#How to find the maximum value in an array and its index
print(np.max(random_matrix))
print(np.argmax(random_matrix))

#How to calculate the mean and standard deviation of an array
print(np.mean(random_matrix))
print(np.std(random_matrix))


##Advanced Exresises
## Create a 5*5 matrix with values ranging from 0 to 24
matrix_5 = np.arange(25).reshape(5,5)
print(matrix_5)
print(np.sum(matrix_5))

a = np.array([[1,2,3],
             [5,6,7]])
b = np.array([[5,6,7],
             [9,10,11],
             [13,14,15]])

#How to perform matrix multiplication
print(np.dot(a,b))

#How to calculate the transpose of a matrix
print(np.transpose(b))

marks = np.array([85, 90, 78,34,45,56,67,89,90,91])
normalized_marks = (marks - np.mean(marks)) /np.std(marks)
print(normalized_marks)

#how to find even numbers in an array

even = marks[marks % 2 == 0]
print(even)