# Task 4: Type-Hinted Calculator

from typing import Optional

def add(a: float, b: float) -> float:
    """Adds two numbers and returns the result."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtracts b from a and returns the result."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiplies two numbers and returns the result."""
    return a * b

def divide(a: float, b: float) -> Optional[float]:
    """Divides a by b. Returns None if b is zero."""
    if b == 0:
        return None
    return a / b

def power(base: float, exp: float) -> float:
    """Returns base raised to the power of exp."""
    return base ** exp

def modulo(a: int, b: int) -> int:
    """Returns remainder of a divided by b. Returns 0 if b is zero."""
    if b == 0:
        return 0
    return a % b

print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 0))
print(power(2, 8))
print(modulo(10, 3))