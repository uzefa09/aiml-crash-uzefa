# Task 2: List Comprehension Drills

# Drill 1: Numbers divisible by 3
numbers = list(range(1, 21))
div_by_3 = [n for n in numbers if n % 3 == 0]
print("Divisible by 3:", div_by_3)

# Drill 2: Words longer than 4 characters in title case
words = ["python", "is", "great", "for", "data", "science", "and", "ai"]
long_words = [w.title() for w in words if len(w) > 4]
print("Long words:", long_words)

# Drill 3: Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40, 100]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
print("Fahrenheit:", fahrenheit)

# Drill 4: Flatten nested list
nested = [[1,2],[3,4],[5,6],[7,8]]
flat = [n for sublist in nested for n in sublist]
print("Flattened:", flat)

# Explore: dict and set comprehensions
squares_dict = {n: n**2 for n in range(1, 6)}
unique_lengths = {len(w) for w in words}
print("Dict comprehension:", squares_dict)
print("Set comprehension:", unique_lengths)