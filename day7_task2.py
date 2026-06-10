# Day 7 Task 2: Extract Report from JSON File

import json

# Create a sample JSON file first
data = {
    "name": "Uzefa Shaikh",
    "role": "AI/ML Intern",
    "skills": ["Python", "Pandas", "NumPy", "GitHub"],
    "experience_months": 1,
    "location": "Jaipur"
}

with open("profile.json", "w") as f:
    json.dump(data, f, indent=4)

# Read and print report
with open("profile.json", "r") as f:
    profile = json.load(f)

skills_upper = [s.upper() for s in profile["skills"]]

print(f"Name     : {profile['name']}")
print(f"Role     : {profile['role']}")
print(f"Location : {profile['location']}")
print(f"Skills   : {', '.join(skills_upper)}")
print(f"Experience: {profile['experience_months']} month(s)")