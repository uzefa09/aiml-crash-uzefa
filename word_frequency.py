# Task 5: Word Frequency Counter

from collections import Counter

sentence = "the cat sat on the mat the cat is fat"

words = sentence.split()
frequency = Counter(words)

for word, count in sorted(frequency.items(), key=lambda x: x[1], reverse=True):
    print(f"{word}: {count}")