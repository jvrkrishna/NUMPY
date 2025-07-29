'''
🛠️ Creating NumPy Arrays with Specific dtype
    NumPy allows you to explicitly specify the data type (dtype) of an array at the time of creation.

🔢 Using int Type
    import numpy as np
    l = [10, 20, 30, 40.5, 50.6]
    arr = np.array(l, dtype="int")

    print(arr)         # [10 20 30 40 50]
    print(arr.size)    # 5
    print(arr.ndim)    # 1
    print(arr.shape)   # (5,)
    print(arr.dtype)   # int64 or int32 (depends on system)
    ⚠️ Note: The float values are truncated, not rounded.

🧱 Another Way (using np.int – deprecated in newer versions)
import numpy as np
arr = np.array([10, 20, 30.6, 50.4], dtype=int) #Better:use `int` instead `np.int`

print(arr)        # [10 20 30 50]
print(arr.dtype)  # int64

💧 Using float Type
import numpy as np
l = [10, 20, 30, 40.5, 50.6]
arr = np.array(l, dtype="float")

print(arr)        # [10.  20.  30.  40.5 50.6]

🔘 Using bool Type
import numpy as np
l = [10, 20, 0, 16.4, "Rama", True, False]
arr = np.array(l, dtype="bool")

print(arr)        # [True True False True True True False]
Anything non-zero or non-empty is treated as True.

🔮 Using complex Type
import numpy as np

l = [10, 20, 30, 43, True, False]
arr = np.array(l, dtype="complex")
print(arr)

Output:
    [10.+0.j 20.+0.j 30.+0.j 43.+0.j  1.+0.j  0.+0.j]

🔤 Using str Type
import numpy as np

l = ["surendra", 10, 20, 30, "Priyanka"]
arr = np.array(l, dtype="str")

print(arr)

Output:
    ['surendra' '10' '20' '30' 'Priyanka']
    All values are converted to strings.

🧰 Using object Type
import numpy as np

l = ["Rama", 10, 20, 30.6, 16+1j, True]
arr = np.array(l, dtype="object")

print(arr)         # ['Rama' 10 20 30.6 (16+1j) True]
print(arr.dtype)   # object

object arrays can store mixed data types, including strings, numbers, booleans, and even complex numbers.'''