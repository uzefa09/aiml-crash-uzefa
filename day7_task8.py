# Day 7 Task 8: NumPy Arrays and Slicing

import numpy as np

# Create arrays
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.arange(1, 11)
arr3 = np.zeros((3, 3))
arr4 = np.linspace(0, 1, 5)

print("=== arr1 ===", arr1)
print("Shape:", arr1.shape, "| dtype:", arr1.dtype, "| ndim:", arr1.ndim)

print("\n=== arr2 ===", arr2)
print("Shape:", arr2.shape, "| dtype:", arr2.dtype, "| ndim:", arr2.ndim)

# Slicing
print("\n=== Slicing ===")
print("First 3:", arr1[0:3])
print("Last element:", arr1[-1])
print("Every 2nd:", arr1[::2])

# 2D array
arr5 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("\n=== 2D Array ===")
print(arr5)
print("Row 0:", arr5[0])
print("Element [1][2]:", arr5[1][2])
print("Subarray:", arr5[0:2, 1:3])