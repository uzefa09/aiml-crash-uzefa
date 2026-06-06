# Task 3: File I/O - Student Records

import csv

# Step 1: Create students.csv
students = [
    {"name": "Uzefa", "math": 90, "science": 85, "english": 88},
    {"name": "Sara", "math": 75, "science": 70, "english": 72},
    {"name": "Ali", "math": 60, "science": 65, "english": 58},
    {"name": "Riya", "math": 88, "science": 92, "english": 85},
    {"name": "Zain", "math": 55, "science": 50, "english": 60}
]

with open("students.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "math", "science", "english"])
    writer.writeheader()
    writer.writerows(students)

print("students.csv created!")

# Step 2: Read and calculate average
def classify(avg):
    if avg >= 90: return "A"
    elif avg >= 80: return "B"
    elif avg >= 70: return "C"
    elif avg >= 60: return "D"
    else: return "F"

results = []
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        avg = (int(row["math"]) + int(row["science"]) + int(row["english"])) / 3
        results.append({"name": row["name"], "average": round(avg, 1), "grade": classify(avg)})

# Step 3: Write results.csv
with open("results.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "average", "grade"])
    writer.writeheader()
    writer.writerows(results)

print("results.csv created!")
for r in results:
    print(f"{r['name']}: Avg={r['average']} Grade={r['grade']}")