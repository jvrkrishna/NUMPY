'''randn() function is used to generate random float values from normal distribution samples with mean 0 and variance 1.'''

import numpy as np
print(help(np.random.randn))

import numpy as np
arr=np.random.randn()
print(arr)

#Creating 1d array
import numpy as np
arr=np.random.randn(10)
print(arr)

#Creation of 2d array
import numpy as np
arr=np.random.randn(10,10)
print(arr)

#Creation of 2d array with large values
import numpy as np
arr=np.random.randn(1000,1000)
print(arr)

import matplotlib.pyplot as plt
plt.hist(arr)
plt.show() #Here it is showing normal distribution.