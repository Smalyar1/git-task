# Автор: Маляр Сергей
import math
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    # Returns the product of two numbers
    return a*b
def sqrt(x):
    """Returns the square root of a number"""
    if x < 0:
        raise ValueError("The square root of a negative number is not defined")
    return math.sqrt(x)

if __name__ == "__main__":
    print("Простой калькулятор запущен.")
    print(f"2 + 2 = {add(2, 2)}")
