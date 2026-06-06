# Task 8: Dunder Methods - Custom Fraction Class

import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        top = self.numerator * other.denominator + other.numerator * self.denominator
        bottom = self.denominator * other.denominator
        gcd = math.gcd(top, bottom)
        return Fraction(top // gcd, bottom // gcd)

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
f3 = Fraction(2, 4)

print(f1 + f2)
print(f1 == f3)
print(f2 < f1)