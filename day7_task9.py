# Day 7 Task 9: Masking, Broadcasting, Cosine Similarity

import numpy as np

# Masking
arr = np.array([10, 25, 3, 47, 8, 32, 15])
mask = arr > 15
print("=== Masking (values > 15) ===")
print(arr[mask])

# Broadcasting
arr2 = np.array([1, 2, 3, 4, 5])
print("\n=== Broadcasting (multiply by 10) ===")
print(arr2 * 10)

# Cosine Similarity
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v3 = np.array([1, 0, 0])
v4 = np.array([0, 1, 0])

print("\n=== Cosine Similarity ===")
print(f"v1 & v2: {cosine_similarity(v1, v2):.4f}")
print(f"v3 & v4: {cosine_similarity(v3, v4):.4f}")