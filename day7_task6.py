# Day 7 Task 6: Clean Missing Values

import pandas as pd
import numpy as np

data = {
    "name": ["Uzefa", "Sara", "Ali", "Riya", "Zain"],
    "math": [92, None, 60, 88, 55],
    "science": [85, 70, None, 92, 50],
    "city": ["Jaipur", None, "Mumbai", "Jaipur", "Delhi"]
}

df = pd.DataFrame(data)

print("=== Before Cleaning ===")
print(df)
print("\nMissing values:\n", df.isnull().sum())

# dropna - row drop karo jahan city missing ho
df_dropped = df.dropna(subset=["city"])

# fillna - math aur science ki missing values average se bharo
df["math"] = df["math"].fillna(df["math"].mean())
df["science"] = df["science"].fillna(df["science"].mean())

print("\n=== After Cleaning ===")
print(df)