# Task 2: Skills Counter
# This file prints a numbered list of skills and the total count.

skills = ["Python", "CSS", "HTML", "JAVASCRIPT", "Communication", "problem solving",]

for i, skill in enumerate(skills, 1):
    print(f"{i}. {skill}")

print(f"\nTotal skills: {len(skills)}")