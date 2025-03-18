''' 
Shuffle means re arranging.
Array shuffle means re-arranging the array elements.
'''

#shuffle with 1d array
import numpy as np
arr=np.arange(5)
print(arr)

np.random.shuffle(arr)
print(arr)

import numpy as np
help(np.random.shuffle)
'''
shuffle(x) method of numpy.random.mtrand.RandomState instance
    shuffle(x)

    Modify a sequence in-place by shuffling its contents.

    This function only shuffles the array along the first axis of a
    multi-dimensional array. The order of sub-arrays is changed but
    their contents remains the same.
'''

#Shuffle with 2d array
import numpy as np
arr=np.arange(9).reshape(3,3)
print(arr)

np.random.shuffle(arr)
print(arr) #only rows will shuffle

#Incase of 3d array will apply to 2d array's