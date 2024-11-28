import math
from decimal import Decimal

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

def validate_decimal(value):
    try:
        return Decimal(value)
    except (ValueError, TypeError):
        raise ValueError("Invalid input: Please enter a valid number")

class Memory:
    def __init__(self):
        self.memory = Decimal(0)
        self.history = []

    def m_add(self, value):
        """Добавить значение в память."""
        value = validate_decimal(value)  # Валидация значения
        self.memory += value
        self.history.append(value)

    def m_subtract(self, value):
        """Вычесть значение из памяти."""
        value = validate_decimal(value)
        self.memory -= value
        self.history.append(-value)

    def m_multiply(self, value):
        """Умножить значение в памяти."""
        value = validate_decimal(value)
        self.memory *= value
        self.history.append(f"*{value}")

    def m_divide(self, value):
        """Разделить значение в памяти."""
        value = validate_decimal(value)
        if value == 0:
            raise ValueError("Cannot divide by zero in memory")
        self.memory /= value
        self.history.append(f"/{value}")

    def m_clear(self):
        """Очистить память."""
        self.memory = Decimal(0)
        self.history.clear()

    def m_recall(self):
        """Возвращает текущее значение из памяти."""
        return self.memory

    def get_history(self):
        """Получить историю операций с памятью."""
        return self.history

    def delete_last(self):
        """Удалить последнюю операцию из памяти."""
        if self.history:
            last_value = self.history.pop()
            if isinstance(last_value, Decimal):
                self.memory -= last_value
            elif isinstance(last_value, str):
                operator = last_value[0]
                value = Decimal(last_value[1:])
                if operator == "*":
                    self.memory /= value
                elif operator == "/":
                    self.memory *= value
        else:
            raise ValueError("No items in memory to delete")
