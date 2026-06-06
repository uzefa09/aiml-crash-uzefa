# Task 7: Pandas - Explore a Dataset

import pandas as pd

data = {
    "name": ["Uzefa", "Sara", "Ali", "Riya", "Zain", "Priya", "Rahul", "Neha", "Arjun", "Pooja"],
    "city": ["Jaipur", "Delhi", "Mumbai", "Jaipur", "Delhi", "Mumbai", "Jaipur", "Delhi", "Mumbai", "Jaipur"],
    "math_score": [92, 75, 60, 88, 55, 95, 78, 82, 70, 65],
    "science_score": [85, 70, 65, 92, 50, 90, 80, 75, 68, 72],
    "english_score": [88, 72, 58, 85, 60, 88, 76, 79, 65, 70]
}

df = pd.DataFrame(data)

df["total"] = df["math_score"] + df["science_score"] + df["english_score"]

print("1. Average score per subject:")
print(df[["math_score", "science_score", "english_score"]].mean())

print("\n2. Highest total score:")
print(df.loc[df["total"].idxmax(), "name"])

print("\n3. Students per city:")
print(df.groupby("city")["name"].count())

print("\n4. Students with math > 75:")
print(df[df["math_score"] > 75][["name", "math_score"]])

print("\n5. Top 3 students by total:")
print(df.nlargest(3, "total")[["name", "total"]])