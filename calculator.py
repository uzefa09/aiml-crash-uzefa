# Task 6: Simple Calculator

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

operations = {"add": add, "subtract": subtract, "multiply": multiply, "divide": divide}

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operation (add/subtract/multiply/divide): ")

    if op in operations:
        print(f"Result: {operations[op](num1, num2)}")
    else:
        print("Invalid operation!")
except ValueError:
    print("Please enter valid numbers!")