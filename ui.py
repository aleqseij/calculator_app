import tkinter as tk
from calc_operations import (
    addition, subtraction, multiplication, division, modulus, power,
    square_root, sine, cosine, floor_value, ceil_value,
    memory_add, memory_subtract, memory_clear, memory_recall
)

# Глобальная переменная для отображения текста в поле ввода
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
        entry_text.set("")
    except ValueError:
        entry_text.set("Error")

def on_memory_subtract():
    """Вычитает текущее значение из памяти."""
    try:
        value = float(entry_text.get())
        memory_subtract(value)
        entry_text.set("")
    except ValueError:
        entry_text.set("Error")

def on_memory_recall():
    """Вставляет значение из памяти в поле ввода."""
    value = memory_recall()
    entry_text.set(entry_text.get() + str(value))

def on_memory_clear():
    """Очищает память."""
    memory_clear()

def on_modulus():
    """Выполняет операцию остатка от деления."""
    try:
        values = entry_text.get().split('%')
        if len(values) == 2:
            a, b = float(values[0]), float(values[1])
            result = modulus(a, b)
            entry_text.set(result)
        else:
            entry_text.set("Error")
    except Exception:
        entry_text.set("Error")

def on_sine():
    """Вычисляет синус."""
    try:
        value = float(entry_text.get())
        result = sine(value)
        entry_text.set(result)
    except ValueError:
        entry_text.set("Error")

def on_cosine():
    """Вычисляет косинус."""
    try:
        value = float(entry_text.get())
        result = cosine(value)
        entry_text.set(result)
    except ValueError:
        entry_text.set("Error")

def on_power():
    """Выполняет возведение в степень."""
    try:
        values = entry_text.get().split('^')
        if len(values) == 2:
            a, b = float(values[0]), float(values[1])
            result = power(a, b)
            entry_text.set(result)
        else:
            entry_text.set("Error")
    except Exception:
        entry_text.set("Error")

def on_square_root():
    """Вычисляет квадратный корень."""
    try:
        value = float(entry_text.get())
        result = square_root(value)
        entry_text.set(result)
    except ValueError:
        entry_text.set("Error")

def on_floor():
    """Округляет число в меньшую сторону."""
    try:
        value = float(entry_text.get())
        result = floor_value(value)
        entry_text.set(result)
    except ValueError:
        entry_text.set("Error")

def on_ceil():
    """Округляет число в большую сторону."""
    try:
        value = float(entry_text.get())
        result = ceil_value(value)
        entry_text.set(result)
    except ValueError:
        entry_text.set("Error")

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
        ('MC', 5, 0), ('MR', 5, 1), ('M+', 5, 2), ('M-', 5, 3),
        ('%', 6, 0), ('sin', 6, 1), ('cos', 6, 2), ('^', 6, 3),
        ('√', 7, 0), ('floor', 7, 1), ('ceil', 7, 2)
    ]

    # Генерация кнопок
    for (text, row, col) in buttons:
        if text == "=":
            button = tk.Button(window, text=text, width=10, height=3, command=on_equal)
        elif text == "C":
            button = tk.Button(window, text=text, width=10, height=3, command=on_clear)
        elif text == "MC":
            button = tk.Button(window, text=text, width=10, height=3, command=on_memory_clear)
        elif text == "MR":
            button = tk.Button(window, text=text, width=10, height=3, command=on_memory_recall)
        elif text == "M+":
            button = tk.Button(window, text=text, width=10, height=3, command=on_memory_add)
        elif text == "M-":
            button = tk.Button(window, text=text, width=10, height=3, command=on_memory_subtract)
        elif text == "%":
            button = tk.Button(window, text=text, width=10, height=3, command=on_modulus)
        elif text == "sin":
            button = tk.Button(window, text=text, width=10, height=3, command=on_sine)
        elif text == "cos":
            button = tk.Button(window, text=text, width=10, height=3, command=on_cosine)
        elif text == "^":
            button = tk.Button(window, text=text, width=10, height=3, command=on_power)
        elif text == "√":
            button = tk.Button(window, text=text, width=10, height=3, command=on_square_root)
        elif text == "floor":
            button = tk.Button(window, text=text, width=10, height=3, command=on_floor)
        elif text == "ceil":
            button = tk.Button(window, text=text, width=10, height=3, command=on_ceil)
        else:
            button = tk.Button(window, text=text, width=10, height=3, command=lambda t=text: on_button_click(t))
        button.grid(row=row, column=col)

    # Запуск главного цикла окна
    window.mainloop()