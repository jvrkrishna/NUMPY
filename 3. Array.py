'''
An array is a collection of homogeneous data items (i.e., all elements must be of the same type). In NumPy, arrays are powerful, multi-dimensional data structures used for storing and manipulating numerical data efficiently.

✅ Key Points
    NumPy arrays are known as n-dimensional arrays (n can be 1, 2, 3, ...).

Arrays are categorized as:
1D Array
2D Array
3D (or nD) Array

📌 1D Array (One-dimensional)
Represents a single row (or column) of elements.
    import numpy as np
    arr = np.array([10, 20, 30])
    print(arr[0])   # Output: 10

🧾 Visual:
[10, 20, 30]   ← Single row with multiple elements

📌 2D Array (Two-dimensional)
A collection of 1D arrays arranged as rows and columns.
    arr = np.array([
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ])

    print(arr[0][2])  # Output: 30
    print(arr[1][2])  # Output: 60  (2nd row, 3rd column)
    
🧾 Visual:
    [[10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]]
    
📌 3D Array (Three-dimensional)
A collection of 2D arrays, essentially forming a cube-like structure.
    arr = np.array([
        [
            [10, 20, 30],
            [40, 50, 60],
            [70, 80, 90]
        ],
        [
            [11, 12, 13],
            [14, 15, 16],
            [17, 18, 19]
        ],
        [
            [15, 25, 35],
            [45, 55, 65],
            [75, 85, 95]
        ]
    ])

    print(arr[2][2][2])  # Output: 95
    
🧾 Breakdown of arr[2][2][2]:
    arr[2] → selects the 3rd 2D array
    arr[2][2] → selects the 3rd row in that 2D array
    arr[2][2][2] → selects the 3rd column in that row → 95
'''