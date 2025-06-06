import tkinter as tk
from tkinter import messagebox
import math

# Create main window
root = tk.Tk()
root.title("Advanced Scientific Calculator")
root.geometry("450x650")
root.configure(bg="#1e1e1e")  # Dark background
root.resizable(False, False)

expression = ""
history = []

def press(key):
    global expression
    expression += str(key)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def backspace():
    global expression
    expression = expression[:-1]
    input_text.set(expression)

def evaluate():
    global expression
    try:
        result = str(eval(expression))
        history.append(expression + " = " + result)
        update_history()
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def scientific_function(func):
    global expression
    try:
        result = str(func(float(expression)))
        history.append(f"{func.__name__}({expression}) = {result}")
        update_history()
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def update_history():
    history_list.delete(0, tk.END)
    for item in history[-5:]:  # Show last 5 calculations
        history_list.insert(tk.END, item)

def on_key(event):
    key = event.char
    if key.isdigit() or key in "+-*/().":
        press(key)
    elif key == '\r':
        evaluate()
    elif key == '\x08':
        backspace()

# Entry widget
input_text = tk.StringVar()
entry = tk.Entry(root, textvariable=input_text, font=('Arial', 24), bd=10,
                 relief='flat', justify='right', bg="#2d2d2d", fg="white", insertbackground="white")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=20, ipady=10)

# History Label
tk.Label(root, text="History", bg="#1e1e1e", fg="#cccccc", font=('Arial', 12)).grid(row=0, column=5)
history_list = tk.Listbox(root, height=12, width=25, bg="#2d2d2d", fg="white", font=('Arial', 10))
history_list.grid(row=1, column=5, rowspan=6, padx=10, pady=10)

# Button layout (basic + scientific)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sqrt', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('^', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('log', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3), ('C', 4, 4),
    ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('(', 5, 3), (')', 5, 4),
    ('←', 6, 0)
]

# Button actions
for (text, row, col) in buttons:
    if text == '=':
        cmd = evaluate
    elif text == 'C':
        cmd = clear
    elif text == '←':
        cmd = backspace
    elif text == 'sqrt':
        cmd = lambda f=math.sqrt: scientific_function(f)
    elif text == 'log':
        cmd = lambda f=math.log10: scientific_function(f)
    elif text == 'sin':
        cmd = lambda f=math.sin: scientific_function(f)
    elif text == 'cos':
        cmd = lambda f=math.cos: scientific_function(f)
    elif text == 'tan':
        cmd = lambda f=math.tan: scientific_function(f)
    elif text == '^':
        cmd = lambda: press("**")
    else:
        cmd = lambda x=text: press(x)

    b = tk.Button(root, text=text, command=cmd, font=('Arial', 14),
                  bg="#333", fg="white", activebackground="#555", activeforeground="white",
                  padx=20, pady=20)
    b.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

# Grid resizing
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for j in range(5):
    root.grid_columnconfigure(j, weight=1)

# Keyboard support
root.bind("<Key>", on_key)

# Run the application
root.mainloop()
