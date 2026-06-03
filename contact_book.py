# Task 9: Mini Contact Book

contacts = [
    {"name": "Uzefa", "phone": "9876543210", "email": "uzefa@gmail.com"},
    {"name": "Sara", "phone": "9123456789", "email": "sara@gmail.com"},
    {"name": "Ali", "phone": "9988776655", "email": "ali@gmail.com"},
    {"name": "Riya", "phone": "9871234567", "email": "riya@gmail.com"},
    {"name": "Zain", "phone": "9765432100", "email": "zain@gmail.com"}
]

def find_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return "Contact not found!"

search = input("Enter name to search: ")
print(find_contact(search))