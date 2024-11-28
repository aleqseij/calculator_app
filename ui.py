import tkinter as tk
from calc_operations import (
    addition, subtraction, multiplication, division, modulus, power,
    square_root, sine, cosine, floor_value, ceil_value,
)

from calc_operations import Memory

# Создаем экземпляр класса Memory
memory = Memory()

# Глобальная переменная для отображения текста в поле ввода
entry_text = None

def on_button_click(value):
    """Обрабатывает нажатие кнопок цифр и операций."""
    entry_text.set(entry_text.get() + value)

def on_clear():
    """Очищает поле ввода."""
    entry_text.set("")

def on_backspace():
    """Удаляет последний символ из поля ввода."""
    current_text = entry_text.get()
    entry_text.set(current_text[:-1])

def on_equal():
    """Выполняет вычисление введенного выражения."""
    try:
        # Преобразуем ^ в ** для возведения в степень
        expression = entry_text.get().replace("^", "**")
        result = eval(expression)
        entry_text.set(result)
    except ZeroDivisionError:
        entry_text.set("Error: Division by zero")
    except SyntaxError:
        entry_text.set("Error: Invalid syntax")
    except Exception as e:
        entry_text.set(f"Error: {e}")

def on_memory_add():
    """Добавить значение в память."""
    try:
        value = float(entry_text.get())
        memory.m_add(value)
        entry_text.set("")
    except ValueError:
        entry_text.set("Error: Invalid input")

def on_memory_subtract():
    """Вычесть значение из памяти."""
    try:
        value = float(entry_text.get())
        memory.m_subtract(value)
        entry_text.set("")
    except ValueError:
        entry_text.set("Error: Invalid input")

def on_memory_multiply():
    """Умножить значение в памяти."""
    try:
        value = float(entry_text.get())
        memory.m_multiply(value)
        entry_text.set("")
    except ValueError:
        entry_text.set("Error: Invalid input")

def on_memory_divide():
    """Разделить значение в памяти."""
    try:
        value = float(entry_text.get())
        memory.m_divide(value)
        entry_text.set("")
    except ValueError:
        entry_text.set("Error: Invalid input")
    except ZeroDivisionError:
        entry_text.set("Error: Cannot divide by zero")

def on_memory_recall():
    """Получить значение из памяти."""
    entry_text.set(str(memory.m_recall()))

def on_memory_clear():
    """Очистить память."""
    memory.m_clear()
    entry_text.set("")

def on_memory_delete():
    """Удалить последнюю операцию из памяти."""
    try:
        memory.delete_last()
        entry_text.set(str(memory.m_recall()))
    except ValueError:
        entry_text.set("Error: No operations to delete")

def on_history():
    """Открывает окно с историей операций с памятью."""
    history_window = tk.Toplevel()
    history_window.title("Memory History")
    
    # Получаем историю из памяти
    history_list = memory.get_history()

    # Отображаем историю в окне
    history_text = tk.Text(history_window, width=40, height=10)
    history_text.pack(padx=10, pady=10)

    if history_list:
        for operation in history_list:
            history_text.insert(tk.END, f"{operation}\n")
    else:
        history_text.insert(tk.END, "No operations in history.")
    
    # Делаем поле только для чтения
    history_text.config(state=tk.DISABLED)

def on_modulus():
    """Добавляет знак остатка от деления в поле ввода."""
    entry_text.set(entry_text.get() + " % ")

def on_sine():
    """Вычисляет синус."""
    try:
        value = float(entry_text.get())
        result = sine(value)
        entry_text.set(result)
    except ValueError:
        entry_text.set("Error: Invalid input")

def on_cosine():
    """Вычисляет косинус."""
    try:
        value = float(entry_text.get())
        result = cosine(value)
        entry_text.set(result)
    except ValueError:
        entry_text.set("Error: Invalid input")

def on_power():
    """Добавляет знак возведения в степень в поле ввода."""
    entry_text.set(entry_text.get() + " ^ ")

def on_square_root():
    """Вычисляет квадратный корень."""
    try:
        value = float(entry_text.get())
        result = square_root(value)
        entry_text.set(result)
    except ValueError:
        entry_text.set("Error: Invalid input")

def on_floor():
    """Округляет число в меньшую сторону."""
    try:
        value = float(entry_text.get())
        result = floor_value(value)
        entry_text.set(result)
    except ValueError:
        entry_text.set("Error: Invalid input")

def on_ceil():
    """Округляет число в большую сторону."""
    try:
        value = float(entry_text.get())
        result = ceil_value(value)
        entry_text.set(result)
    except ValueError:
        entry_text.set("Error: Invalid input")

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
        ('√', 7, 0), ('floor', 7, 1), ('ceil', 7, 2), ('←', 7, 3),  # Кнопка Backspace (←)
        ('History', 8, 0)  # Кнопка для истории операций
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
        elif text == "←":
            button = tk.Button(window, text=text, width=10, height=3, command=on_backspace)
         elif text == "History":
            button = tk.Button(window, text=text, width=10, height=3, command=on_history)
        else:
            button = tk.Button(window, text=text, width=10, height=3, command=lambda t=text: on_button_click(t))
        button.grid(row=row, column=col)

    # Запуск главного цикла окна
    window.mainloop()
