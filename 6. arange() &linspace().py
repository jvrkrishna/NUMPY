#Creation of ndarray using arange()
import numpy as np
arr=np.arange(10)
print(arr)
print(arr.shape)
print(arr.dtype)
print(arr.size)
print(arr.ndim)

print(help(np.arange))

#Creation of ndarray using linspace()
import numpy as np
print(help(np.linspace))
#linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0, *, device=None)

#print the values between 0 to 1
import numpy as np
arr=np.linspace(0,1) #Here it prints 50 values which is 50 default
print(arr) 

#print the values between 0 to 1 with number of values 5
import numpy as np
arr=np.linspace(0,1,num=5)
print(arr)

#print the values between 0 to 1 with dtype
import numpy as np
arr=np.linspace(0,1,num=5,dtype="int")
print(arr)

#print the values between 100 to 200 with dtype and endpoint
import numpy as np
arr=np.linspace(100,200,num=5,dtype="int",endpoint=False)
print(arr)

#print the values between 100 to 200 and know the gap value by retstep
import numpy as np
arr=np.linspace(100,200,num=10,retstep=True)
print(arr)