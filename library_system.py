# Task 5: Inheritance - Library System

class LibraryItem:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def describe(self):
        return f"{self.title} by {self.author} ({self.year})"

class Book(LibraryItem):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages

    def describe(self):
        return f"{super().describe()} - {self.pages} pages"

class EBook(LibraryItem):
    def __init__(self, title, author, year, file_size_mb):
        super().__init__(title, author, year)
        self.file_size_mb = file_size_mb

    def describe(self):
        return f"{super().describe()} - {self.file_size_mb}MB"

items = [
    Book("Python Crash Course", "Eric Matthes", 2019, 544),
    Book("Clean Code", "Robert Martin", 2008, 431),
    EBook("Deep Learning", "Ian Goodfellow", 2016, 12.5),
    EBook("AI Basics", "John Paul", 2021, 8.2)
]

for item in items:
    print(item.describe())

# isinstance check - returns True because Book inherits from LibraryItem
print(isinstance(items[0], LibraryItem))