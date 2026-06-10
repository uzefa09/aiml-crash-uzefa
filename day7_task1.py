# Day 7 Task 1: Student Profile Card

def profile_card(name: str, role: str, skills: list) -> str:
    return (
        f"Name  : {name}\n"
        f"Role  : {role}\n"
        f"Skills: {', '.join(skills)}"
    )

profile = {
    "name": "Uzefa Shaikh",
    "role": "AI/ML Intern",
    "skills": ["Python", "Pandas", "GitHub", "Data Analysis"]
}

print(profile_card(profile["name"], profile["role"], profile["skills"]))