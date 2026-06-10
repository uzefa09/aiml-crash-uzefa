# Day 7 Task 7: describe() and value_counts()

import pandas as pd

data = {
    "name": ["Uzefa", "Sara", "Ali", "Riya", "Zain", "Priya"],
    "city": ["Jaipur", "Delhi", "Mumbai", "Jaipur", "Delhi", "Jaipur"],
    "math": [92, 75, 60, 88, 55, 95],
    "science": [85, 70, 65, 92, 50, 90]
}

df = pd.DataFrame(data)

print("=== describe() - Numeric Summary ===")
print(df.describe())

print("\n=== value_counts() - City Distribution ===")
print(df["city"].value_counts())

# Observation:
# describe() shows mean, min, max of math and science scores
# value_counts() shows Jaipur has most students (3)