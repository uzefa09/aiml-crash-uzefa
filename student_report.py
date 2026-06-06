# Task 1: Class-Based Student Report

class Student:
    school_name = "CodeTrade Academy"

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90: return "A"
        elif avg >= 80: return "B"
        elif avg >= 70: return "C"
        elif avg >= 60: return "D"
        else: return "F"

    def __str__(self):
        return f"[{Student.school_name}] {self.name} | Roll: {self.roll_no} | Avg: {self.average():.1f} | Grade: {self.grade()}"

s1 = Student("Uzefa", 1, [92, 88, 95])
s2 = Student("Sara", 2, [75, 70, 68])
s3 = Student("Ali", 3, [55, 60, 50])

print(s1)
print(s2)
print(s3)