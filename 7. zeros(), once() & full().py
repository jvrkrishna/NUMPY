#Creation of ndarray using zeros()
#Creation of 1d ayyar with size 10 and fill 0
import numpy as np
arr=np.zeros(10)
print(arr)

#print(help(np.zeros))
'''zeros(shape, dtype=float, order='C', *, like=None)'''

#Create 2*3 array and fill zero
import numpy as np
arr=np.zeros((2,3))
print(arr)

#Create 2*3 array and fill zero with int value
import numpy as np
arr=np.zeros((2,3), dtype='int')
print(arr)

#Create 3d array with shape 2*3*3
import numpy as np
arr=np.zeros((2,3,3))
print(arr)

#Create 4d array with shape 2*2*3*3
import numpy as np
arr=np.zeros((2,2,3,3))
print(arr)

#Creation of ndarray using ones()
#Creation of 1d array with size 10 and fill 1
import numpy as np
arr=np.ones(10)
print(arr)

#Creation of ndarray using fill()
import numpy as np
print(help(np.full))
'''full(shape, fill_value, dtype=None, order='C', *, device=None, like=None)'''

#Creation of 1d array with size 10 and fill 999
import numpy as np
arr=np.full(10,999)
print(arr)

#Creation of 2d array and fill 888
import numpy as np
arr=np.full((2,3),888)
print(arr)