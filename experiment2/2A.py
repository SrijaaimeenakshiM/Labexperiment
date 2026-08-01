import numpy as np

print("--- Working with NumPy Arrays ---")
# 1. Array creation
arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("1D Array:\n", arr_1d)
print("\n2D Array:\n", arr_2d)

# 2. Operations
print("\nArray addition (arr_1d + 5):\n", arr_1d + 5)
print("\nArray multiplication (arr_1d * 2):\n", arr_1d * 2)

# 3. Aggregations
print("\nSum of 2D array elements:", np.sum(arr_2d))
print("Mean of 1D array elements:", np.mean(arr_1d))

# 4. Reshaping
arr_reshaped = arr_1d.reshape(5, 1)
print("\nReshaped Array (5x1):\n", arr_reshaped)

# 5. Indexing and Slicing
print("\nFirst element of 1D array:", arr_1d[0])
print("First row of 2D array:", arr_2d[0, :])
