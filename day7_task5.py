# Day 7 Task 5: Compare .loc and .iloc

import pandas as pd

data = {
    "name": ["Uzefa", "Sara", "Ali", "Riya", "Zain"],
    "city": ["Jaipur", "Delhi", "Mumbai", "Jaipur", "Delhi"],
    "math_score": [92, 75, 60, 88, 55],
    "science_score": [85, 70, 65, 92, 50]
}

df = pd.DataFrame(data)

# .loc = label based (row name/condition + column name)
print("=== .loc example ===")
print(df.loc[0:2, ["name", "math_score"]])

# .iloc = position based (row number + column number)
print("\n=== .iloc example ===")
print(df.iloc[0:3, 0:2])

# Note:
# .loc uses column NAMES and row LABELS
# .iloc uses column NUMBERS and row NUMBERS (like index)