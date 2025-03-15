#Creation of array using empty()
import numpy as np
arr=np.empty((2,2))
print(arr)

#When we use empty(): If we are not worry about data that is system generated data then we can go for empty().

#Creation of array using diag()
'''
If we are passing 2d array it will return the diagonal.
If we are passing 1d array then it will construct 2d array and make that 1d array as main diagonal.
'''
#2d array
import numpy as np
arr=np.arange(16).reshape(4,4)
print(arr)

print(np.diag(arr)) # It will return main diagonal.
print(np.diag(arr,k=1))

#1d array
import numpy as np
arr=np.arange(5)
print(arr)

'''
[0 1 2 3 4]
'''

print(np.diag(arr))
'''
[[0 0 0 0 0]
 [0 1 0 0 0]
 [0 0 2 0 0]
 [0 0 0 3 0]
 [0 0 0 0 4]]
'''

import numpy as np
arr=np.arange(5)
print(np.diag(arr,k=-1))
'''
[[0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 1 0 0 0 0]
 [0 0 2 0 0 0]
 [0 0 0 3 0 0]
 [0 0 0 0 4 0]]
'''