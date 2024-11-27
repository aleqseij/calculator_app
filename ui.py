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

def on_memory_add():
    """Добавляет текущее значение в память."""
    try:
        value = float(entry_text.get())
        memory_add(value)
        entry_text.set("")  # Очистить поле ввода
    except ValueError:
        entry_text.set("Error")

def on_memory_subtract():
    """Вычитает текущее значение из памяти."""
    try:
        value = float(entry_text.get())
        memory_subtract(value)
        entry_text.set("")  # Очистить поле ввода
    except ValueError:
        entry_text.set("Error")

def on_memory_recall():
    """Вставляет значение из памяти в поле ввода."""
    value = memory_recall()
    entry_text.set(entry_text.get() + str(value))

def on_memory_clear():
    """Очищает память."""
    memory_clear()

def start_calculator():
    """Запускает графический интерфейс калькулятора."""
    global entry_text
    window = tk.Tk()
    window.title("Calculator")

    # Переменная для поля ввода
    entry_text = tk.StringVar()

    # Поле ввода
    entry = tk.Entry(window, textvariable=entry_text, font=('Arial', 20), bd=10, relief="sunken", justify="right")
    entry.grid(row=0, column=0, columnspan=4)

    # Кнопки калькулятора
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ('MC', 5, 0), ('MR', 5, 1), ('M+', 5, 2), ('M-', 5, 3)
    ]