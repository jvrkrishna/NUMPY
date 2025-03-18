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