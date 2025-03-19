'''linspace means linear space: 2 4 6 8 10'''

'''logspace means logrithm space: 2 4 8 16 32'''

import numpy as np
arr=np.logspace(1,2)
print(arr)

print(help(np.logspace))

import numpy as np
arr=np.logspace(1,2,num=5)
print(arr) #Log 10 to the power 10 to 100

import numpy as np
arr=np.logspace(1,3,num=5)
print(arr) #Log 10 to the power 10 to 1000

import numpy as np
arr=np.logspace(2,3,num=5,base=2)
print(arr) #log 2 to the power of 2 to 3

import numpy as np
arr=np.logspace(2,3,num=5,base=2,endpoint=False)
print(arr) #log 2 to the power of 2 to 3