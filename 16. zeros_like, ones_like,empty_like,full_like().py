#Creation of ndarray using
'''
zeros_like()
ones_like()
empty_like()
full_like()
'''

#zeros
import numpy as np
arr=np.zeros((2,2),dtype=int)
print(arr)

#ones
import numpy as np
arr=np.ones((2,2),dtype=int)
print(arr)

#empty
import numpy as np
arr=np.empty((2,2),dtype=int)
print(arr)

#full
import numpy as np
arr=np.full((2,2),10,dtype=int)
print(arr)

#zeros_like()
import numpy as np
arr=np.arange(10)
print(arr)

arr1=np.zeros_like(arr)
print(arr1)

#ones_like()
import numpy as np
arr=np.arange(10)
print(arr)

arr1=np.ones_like(arr)
print(arr1)

#empty_like()
import numpy as np
arr=np.arange(10)
print(arr)

arr1=np.empty_like(arr)
print(arr1)

#full_like()
import numpy as np
arr=np.arange(10)
print(arr)

arr1=np.full_like(arr,10)
print(arr1)

#Create a 3*3 array
import numpy as np
x=np.arange(9).reshape(3,3)
print(x)

arr=np.zeros_like(x)
print(arr)