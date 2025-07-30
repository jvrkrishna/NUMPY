'''📏 Creation of ndarray using np.arange()
import numpy as np
arr = np.arange(10)

print(arr)          # [0 1 2 3 4 5 6 7 8 9]
print(arr.shape)    # (10,)
print(arr.dtype)    # int64
print(arr.size)     # 10
print(arr.ndim)     # 1

print(help(np.arange))

np.arange([start, ]stop, [step, ], dtype=None)
Creates an array with regularly incrementing values.

📐 Creation of ndarray using np.linspace()
import numpy as np
print(help(np.linspace))

Signature:
linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
Returns evenly spaced numbers over a specified interval.

🔹 Example 1: Values between 0 and 1 (default 50 values)
import numpy as np

arr = np.linspace(0, 1)
print(arr)

🔹 Example 2: Values between 0 and 1 with num=5
import numpy as np

arr = np.linspace(0, 1, num=5)
print(arr)  # [0.   0.25 0.5  0.75 1.  ]

🔹 Example 3: Values with dtype=int
import numpy as np

arr = np.linspace(0, 1, num=5, dtype="int")
print(arr)  # [0 0 0 0 1]
⚠️ Note: Floating-point values are truncated to integers.

🔹 Example 4: Values between 100 and 200 (5 steps, no endpoint, integer dtype)
import numpy as np

arr = np.linspace(100, 200, num=5, endpoint=False, dtype="int")
print(arr)  # [100 120 140 160 180]

🔹 Example 5: Get values and the step size using retstep=True
import numpy as np

arr, step = np.linspace(100, 200, num=10, retstep=True)
print(arr)   # Array of 10 values
print(step)  # Step size (approx. 11.11)'''