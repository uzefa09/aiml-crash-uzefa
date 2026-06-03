# Task 7: Grade Classifier

def classify(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else: return "F"

students = [
    {"name": "Uzefa", "score": 92},
    {"name": "Sara", "score": 78},
    {"name": "Ali", "score": 65},
    {"name": "Riya", "score": 55},
    {"name": "Zain", "score": 83}
]

for student in sorted(students, key=lambda x: x["score"], reverse=True):
    print(f"{student['name']}: {student['score']} -> {classify(student['score'])}")