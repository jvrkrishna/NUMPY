#Creation of ndarray using random module
#randint()
import numpy as np
print(help(np.random.randint))
'''
randint(low, high=None, size=None, dtype=<class 'int'>) method of numpy.random.mtrand.RandomState instance
    randint(low, high=None, size=None, dtype=int)
'''

#Generate a random number
import numpy as np
arr=np.random.randint(10)
print(arr)

#Generate 10 random numbers
import numpy as np
for i in range(50):
    arr=np.random.randint(10)
    print(arr)
    
#Creation of ndarray(1D) using randint() function
import numpy as np
arr=np.random.randint(1,21,size=5)
print(arr)

#Creation of ndarray(2D) using randint() function
import numpy as np
arr=np.random.randint(1,21,size=(3,3))
print(arr)

#Creation of ndarray(3D) using randint() function
import numpy as np
arr=np.random.randint(1,21,size=(2,3,3))
print(arr)

#Creation of ndarray(4D) using randint() function
import numpy as np
arr=np.random.randint(1,21,size=(2,2,3,3))
print(arr)

#dtype int32
import numpy as np
arr1=np.random.randint(1,21,size=5,dtype='int32')
print(arr1)
print(arr1.dtype)

#dtype int8
import numpy as np
arr2=np.random.randint(1,21,size=5,dtype='int8')
print(arr2)
print(arr2.dtype)

import sys
print(sys.getsizeof(arr1))
print(sys.getsizeof(arr2))

#Suppose if we want to create 3*3 ndarray using randint in float data can we
import numpy as np
arr=np.random.randint(10,21,size=(3,3),dtype="float")##### it will raise error
print(arr)

#Suppose if we want to create 3*3 ndarray using randint in float data can we
import numpy as np
arr=np.random.randint(10,21,size=(3,3))
print(arr)

#Now we will convert this int based array to float based array
farr=arr.astype(float)#Converting int to float
print(farr)

#########Creation of ndarray using rand(), uniform(), randn() & normal()
'''
rand() function is used to generate random float values in the range 0 to 1 from uniform distribution samples.
Here 0 is included and 1 is not included.
if we pass shape, it will give random values in the given shape.
'''

#What is Uniform distribution
''' In uniform distribution the probability of x is constant.'''

#What is normal distribution
''' In normal distribution the probability of x is high at the center and low at the start and end.'''

#rand() function
import numpy as np
arr=np.random.rand()
print(arr)

#print(help(np.random.rand))

#2d array
import numpy as np
arr=np.random.rand(2,2)
print(arr)

#2d array with large values
import numpy as np
arr=np.random.rand(1000,1000)
print(arr)

import matplotlib.pyplot as plt
plt.hist(arr)
plt.show() #Here it is showing uniform distribution.

