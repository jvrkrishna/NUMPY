#Creation of ndarray using specific datatypes
#Using int type
import numpy as np
l=[10,20,30,40.5,50.6]
arr=np.array(l,dtype="int")
print(arr)
print(arr.size)
print(arr.ndim)
print(arr.shape)
print(arr.dtype)

#Another way
import numpy as np
arr=np.array([10,20,30.6,50.4],dtype=np.int)
print(arr)
print(arr.dtype)

#Using float type
import numpy as np
l=[10,20,30,40.5,50.6]
arr=np.array(l,dtype="float")
print(arr)

#Using bool type
import numpy as np
l=[10,20,0,16.4,"Rama",True,False]
arr=np.array(l,dtype="bool")
print(arr)

#Using Complex type
import numpy as np
l=[10,20,30,43,True,False]
arr=np.array(l,dtype="complex")
print(arr)

#Using str type
import numpy as np
l=["surendra",10,20,30,"Priyanka"]
arr=np.array(l,dtype="str")
print(arr)

#Creation of ndarray using object type
import numpy as np
l=["Rama",10,20,30.6,16+1j,True]
arr=np.array(l,dtype="object")
print(arr) #object can hold multi datatypes
print(arr.dtype)
