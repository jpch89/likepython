def calculate(num1, num2, calc_func):
    print(calc_func(num1, num2))

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

calculate(1, 2, add)
calculate(1, 2, sub)
"""
3
-1
"""
