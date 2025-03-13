#List VS Array
'''
-->List and array both are ordered collection and they both are mutable in nature.
-->List is used to hold heterogenous data where array is used to store homogeneous data items.
'''

'''
-->Array consume less space as compared to list.
'''
import sys
l=[i for i in range(100)]
print('size of l is',sys.getsizeof(l))

import numpy as np
import sys
n=np.arange(100)
print('size of n is',sys.getsizeof(n))

'''
-->By using array, we can perform vector operation, but we can't perform vector opertaion by using list.
'''
#vector operations using numpy array(possible) and python list(not possible)
l=[10,20,30,40,50]
data=l+3 #TypeError: can only concatenate list (not "int") to list

#vector operation using numpy array
import numpy as np
n=np.arange(10)
data=n+3
print(data)

'''
1. Creation of ndarray using array()
2. Check different properties of ndarray
3. Upcating at the time of array creation
'''

####Creation of 1darray by using array()
#Creation of 1D array() by list, tuple
l=[10,20,30,40,50]
print(l)
print(type(l))

'''
Output:
[10, 20, 30, 40]
<class 'list'>'''

#Converting list to 1D array()
import numpy as np
arr=np.array(l)
print(arr)
print(type(arr))

'''
Output:
[10 20 30 40]
<class 'numpy.ndarray'>'''

'''Checking different properties of 1drray'''
import numpy as np
l=[10,20,30,40,50]
arr=np.array(l)
print(arr)
print(arr.ndim) #To check the dimension
print(arr.shape)#To check the shape
print(arr.size) #To check the size
print(arr.dtype)#To check the data type

#Creation  of 2d array from nested list using array()
l=[[10,20,30],[40,"Ram",60],[70,80,90]]
print(l)
print(type(l))

#Converting nested list to 2D Array
import numpy as np
arr=np.array(l)
print(arr)

#Checking different properties
print(arr.ndim) #To check the dimension
print(arr.shape)#To check the shape
print(arr.size) #To check the size
print(arr.dtype)#To check the data type

#Creation  of 3d array from nested list using array()
l=[[[10,20,30],[40,50,60],[70,80,90]],[[5,15,25],[35,45,55],[65,75,85]]]
print(l)
print(type(l))

#Converting nested list to 3d array
import numpy as np
arr=np.array(l)
print(arr)

#Checking different properties
print(arr.ndim) #To check the dimension
print(arr.shape)#To check the shape
print(arr.size) #To check the size
print(arr.dtype)#To check the data type
print(arr[1][2][2])#To Check the value

#Upcasting
'''
In NumPy, upcasting refers to the automatic conversion of data types to a higher or more general type when performing operations between arrays of different types. This ensures that the result can hold all possible values from the operation without data loss.
'''
#Example:
import numpy as np
l=[10,20,30,40.5,50.6]
arr=np.array(l)
print(arr)

#Example:
import numpy as np

# Integer array
int_arr = np.array([1, 2, 3])

# Float array
float_arr = np.array([1.1, 2.2, 3.3])

# Performing an operation
result = int_arr + float_arr

print(result)  # Output: [2.1 4.2 6.3]
print(result.dtype)  # Output: float64 (upcasted to float)


