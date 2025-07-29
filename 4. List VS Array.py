'''
🧮 List vs NumPy Array
✅ Similarities
    . Both are ordered collections.
    . Both are mutable (can be changed after creation).

🔁 Key Differences
+-----------------------+----------------------------------+----------------------------------+
| Feature               | Python List                      | NumPy Array                      |
+-----------------------+----------------------------------+----------------------------------+
| Data Type             | Can store heterogeneous data     | Stores homogeneous data only     |
+-----------------------+----------------------------------+----------------------------------+
| Performance           | Slower                           | Much faster (optimized in C)     |
+-----------------------+----------------------------------+----------------------------------+
| Memory Efficiency     | Consumes more memory             | Consumes less memory             |
+-----------------------+----------------------------------+----------------------------------+
| Vectorized Operations | ❌ Not supported                  | ✅ Supported                      |
+-----------------------+----------------------------------+----------------------------------+


📏 Memory Comparison Example
    import sys
    import numpy as np

# Python list
    l = [i for i in range(100)]
    print('Size of list:', sys.getsizeof(l))  # Includes object overhead

# NumPy array
    n = np.arange(100)
    print('Size of NumPy array:', sys.getsizeof(n))  # Much smaller

➕ Vector Operations
❌ Not possible with lists:
    l = [10, 20, 30, 40, 50]
    data = l + 3  # ❌ TypeError: can only concatenate list (not "int") to list

✅ Possible with NumPy arrays:
    import numpy as np
    n = np.arange(10)
    data = n + 3
    print(data)  # [3 4 5 6 7 8 9 10 11 12]

🧱 Creating NumPy Arrays
🔹 From List (1D)
    l = [10, 20, 30, 40, 50]
    print(type(l))  # <class 'list'>

    arr = np.array(l)
    print(arr)      # [10 20 30 40 50]
    print(type(arr))  # <class 'numpy.ndarray'>

🔍 Checking Array Properties
    print(arr.ndim)   # 1 → Dimension
    print(arr.shape)  # (5,) → Shape (5 elements)
    print(arr.size)   # 5 → Total elements
    print(arr.dtype)  # int64 or int32 depending on system

🔹 Creating a 2D Array (Nested List)
    l = [[10, 20, 30], [40, "Ram", 60], [70, 80, 90]]
    arr = np.array(l)
    print(arr)
    Output:
        [['10' '20' '30']
        ['40' 'Ram' '60']
        ['70' '80' '90']]

Properties:
    print(arr.ndim)   # 2
    print(arr.shape)  # (3, 3)
    print(arr.size)   # 9
    print(arr.dtype)  # <U21 (due to mixed types, upcasted to string)

🔹 Creating a 3D Array
        l = [
            [[10, 20, 30], [40, 50, 60], [70, 80, 90]],
            [[5, 15, 25], [35, 45, 55], [65, 75, 85]]
        ]

        arr = np.array(l)
        print(arr)

Accessing elements:
        print(arr[1][2][2])  # Output: 85
        Array properties:
            print(arr.ndim)   # 3
            print(arr.shape)  # (2, 3, 3)
            print(arr.size)   # 18
            print(arr.dtype)  # int64

⚙️ Upcasting in NumPy
Upcasting is the automatic promotion of data types to avoid data loss when combining different types.
🔸 Example 1
        l = [10, 20, 30, 40.5, 50.6]
        arr = np.array(l)
        print(arr)        # Output: [10.  20.  30.  40.5 50.6]
        print(arr.dtype)  # float64

🔸 Example 2
        int_arr = np.array([1, 2, 3])        # int64
        float_arr = np.array([1.1, 2.2, 3.3])  # float64

        result = int_arr + float_arr
        print(result)        # [2.1 4.2 6.3]
        print(result.dtype)  # float64
'''