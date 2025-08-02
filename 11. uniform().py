#Uniform() functions
''' Exactly same as rand() but here we can cutomize our low and high values.'''

import numpy as np
print(help(np.random.uniform))
'''uniform(low=0.0, high=1.0, size=None) method of numpy.random.mtrand.RandomState instance
    uniform(low=0.0, high=1.0, size=None)
'''

import numpy as np
arr=np.random.uniform()
print(arr)

#Give the value between 1 to 5
import numpy as np
arr=np.random.uniform(1.0,5.0)
print(arr)

import matplotlib.pyplot as plt
plt.hist(arr)
plt.show() #Here it is showing uniform distribution.