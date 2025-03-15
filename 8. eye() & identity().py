#What is identity matrix
'''matrix having diagonal filled with 1 and others are filled with 0'''

#Creation of ndarray using eye() and identity()
import numpy as np
print(help(np.eye))

''' eye(N, M=None, k=0, dtype=<class 'float'>, order='C', *, device=None, like=None)
    Return a 2-D array with ones on the diagonal and zeros elsewhere.
N=rows
M=cols
K=diagonal    
'''

#Create 3*3 identity matrix using eye() function
import numpy as np
arr=np.eye(3,dtype="int")
print(arr)

#Creation of 3*4 matrix using eye() function with row and column
import numpy as np
arr=np.eye(3,4,dtype="int")
print(arr)

#Customization of diagonal with default k=0
import numpy as np
arr=np.eye(4,4,dtype="int")
print(arr)
'''
[[1 0 0 0]
 [0 1 0 0]
 [0 0 1 0]
 [0 0 0 1]]
'''

#Customization of diagonal k with 1
import numpy as np
arr=np.eye(4,4,k=1,dtype="int")
print(arr)
'''
[[0 1 0 0]
 [0 0 1 0]
 [0 0 0 1]
 [0 0 0 0]]
'''

#identity()
''' It is exactly as eye() function, the difference is here number of rows
and no.of cols must be same, here the main diagonal k cannot customise.'''

#Creation of ndarray using identity()
import numpy as np
print(help(np.identity))

''' identity(n, dtype=None, *, like=None)
    Return the identity array.
n=it represent both no of rows and cols.   
'''

#Create identity matrix using identity()
import numpy as np
arr=np.identity(10,dtype="int")
print(arr)