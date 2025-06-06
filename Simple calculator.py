import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

expression = ""

def press(key):
    global expression
    expression += str(key)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def evaluate():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result  # allow continuous calculation
    except:
        input_text.set("Error")
        expression = ""

# Entry widget
input_text = tk.StringVar()
entry = tk.Entry(root, textvariable=input_text, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Create buttons dynamically
for (text, row, col) in buttons:
    action = lambda x=text: press(x) if x not in ('=', 'C') else evaluate() if x == '=' else clear()
    tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=action).grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

# Expand rows/columns
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Run the app
root.mainloop()
