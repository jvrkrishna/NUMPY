########## normal() #########
'''It is same as general functions but here we can customize mean and variance.'''
import numpy as np
print(help(np.random.normal))
'''
normal(loc=0.0, scale=1.0, size=None) method of numpy.random.mtrand.RandomState instance
    normal(loc=0.0, scale=1.0, size=None)
    
📌 Explanation:
loc → This is the mean (center) of the distribution.
→ Think of it as the "average" value.

scale → This is the standard deviation (spread or width) of the distribution.
→ It determines how far the values deviate from the mean.

size → The shape of the output array (e.g., a single number, a 1D array, a 2D array, etc.).
'''

import numpy as np
arr=np.random.normal(loc=10,scale=2,size=5)
print(arr)

import numpy as np
arr=np.random.normal(5,2,(100,100))
print(arr)

import matplotlib.pyplot as plt
plt.hist(arr)
plt.show()

import numpy as np
arr=np.random.normal(10,5,(100,100))
print(arr)

import matplotlib.pyplot as plt
plt.hist(arr)
plt.show()