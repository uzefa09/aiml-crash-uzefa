# Day 7 Task 4: Select Columns and Filter Rows

import pandas as pd

data = {
    "name": ["Uzefa", "Sara", "Ali", "Riya", "Zain", "Priya"],
    "city": ["Jaipur", "Delhi", "Mumbai", "Jaipur", "Delhi", "Mumbai"],
    "math_score": [92, 75, 60, 88, 55, 95],
    "science_score": [85, 70, 65, 92, 50, 90],
    "english_score": [88, 72, 58, 85, 60, 88]
}

df = pd.DataFrame(data)

# Select specific columns
print("=== Selected Columns ===")
print(df[["name", "math_score", "science_score"]])

# Filter: math score > 75
print("\n=== Students with Math > 75 ===")
print(df[df["math_score"] > 75][["name", "math_score"]])

# Filter: city is Jaipur
print("\n=== Students from Jaipur ===")
print(df[df["city"] == "Jaipur"][["name", "city"]])