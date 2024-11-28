import math

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)

def sine(a):
    return round(math.sin(math.radians(a)), 15)

def cosine(a):
    return round(math.cos(math.radians(a)), 15)

def floor_value(a):
    return math.floor(a)

def ceil_value(a):
    return math.ceil(a)

memory = 0
ram1 = 0
ram2 = 0
memory1 = 0
memory2 = 0

def memory_add(value):
    """Добавить значение в память (m+)"""
    global memory
    memory += value

def memory_subtract(value):
    """Вычесть значение из памяти"""
    global memory
    memory -= value

def memory_clear():
    """Очистить память (mc)"""
    global memory
    memory = 0

def memory_recall():
    """Вернуть значение из памяти (mr)"""
    return memory