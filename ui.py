import tkinter as tk
from calc_operations import (
    addition, subtraction, multiplication, division, modulus, power,
    square_root, sine, cosine, floor_value, ceil_value,
    memory_add, memory_subtract, memory_clear, memory_recall
)

entry_text = None

def on_button_click(value):
    """Обрабатывает нажатие кнопок цифр и операций."""
    entry_text.set(entry_text.get() + value)

def on_clear():
    """Очищает поле ввода."""
    entry_text.set("")

def on_equal():
    """Выполняет вычисление введенного выражения."""
    try:
        # Оцениваем выражение, используя встроенный eval
        result = eval(entry_text.get())
        entry_text.set(result)
    except Exception as e:
        entry_text.set(f"Error: {e}")