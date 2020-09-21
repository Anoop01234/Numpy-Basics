import numpy as np

a=np.array([1,2,3])

#Display elements at particular index
a=[1,2,3]
print(a[0],a[1])

#Changing element at particular index
a[2]=5
print(a)

#Manipulating multidimensional array
b=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(b.shape)
print(b[1,0,0], b[1,0,1], b[1,0,2])

#Creating array of m*n dimension with all entities as 0
a=np.zeros((2,2))
print(a)


#Creating array of m*n dimension with all entities as 1
b=np.ones((1,2))
print(b)


#Creating array of m*n dimension with all entities as 7
c=np.full((2,2),7)
print(c)


#Creating identity matrix of dimension N
d=np.eye(2)
print(d)


#Creating array of m*n dimension with random entities
e=np.random.random((2,2))
print(e)

a=np.zeros((1,8))
print(a)
b=np.reshape(a,(2,4))
print(b)

arr = np.array([1, 2, 3, 4, 5, 6, 7])

#Printing array
print(arr)


#Printing array from index 1 to 4 (last index is not considered)
print(arr[1:5])


#Printing array from index 2 to end (length of array)
print(arr[2:])

#Printing array with step size of 2 (skipping every second index)
print(arr[: : 2])


#Printing reverse of array
print(arr[::-1])


#Printing reverse of array with step size of 2
print(arr[-1::-2])
