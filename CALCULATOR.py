import tkinter as tk
from tkinter import messagebox

# Function to perform the calculation
def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ValueError("Division by zero")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation")
        
        result_var.set(result)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

# Title and instructions
title_label = tk.Label(root, text="Simple Calculator", font=("Arial", 16))
title_label.grid(row=0, column=0, columnspan=4, pady=10)

instruction_label = tk.Label(root, text="Enter numbers, select an operation, and see the result", font=("Arial", 10))
instruction_label.grid(row=1, column=0, columnspan=4, pady=5)

# Input fields
tk.Label(root, text="Number 1:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky='e')
entry_num1 = tk.Entry(root, font=("Arial", 12))
entry_num1.grid(row=2, column=1, padx=10, pady=5, columnspan=3, sticky='we')

tk.Label(root, text="Number 2:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky='e')
entry_num2 = tk.Entry(root, font=("Arial", 12))
entry_num2.grid(row=3, column=1, padx=10, pady=5, columnspan=3, sticky='we')

# Operation buttons
tk.Label(root, text="Operation:", font=("Arial", 12)).grid(row=4, column=0, padx=10, pady=5, sticky='e')

button_add = tk.Button(root, text="+", font=("Arial", 12), width=4, command=lambda: calculate('+'))
button_add.grid(row=4, column=1, padx=5, pady=5)

button_subtract = tk.Button(root, text="-", font=("Arial", 12), width=4, command=lambda: calculate('-'))
button_subtract.grid(row=4, column=2, padx=5, pady=5)

button_multiply = tk.Button(root, text="*", font=("Arial", 12), width=4, command=lambda: calculate('*'))
button_multiply.grid(row=4, column=3, padx=5, pady=5)

button_divide = tk.Button(root, text="/", font=("Arial", 12), width=4, command=lambda: calculate('/'))
button_divide.grid(row=4, column=4, padx=5, pady=5)

# Result field
tk.Label(root, text="Result:", font=("Arial", 12)).grid(row=5, column=0, padx=10, pady=5, sticky='e')
result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var, font=("Arial", 12), state='readonly')
result_entry.grid(row=5, column=1, padx=10, pady=5, columnspan=3, sticky='we')

# Run the application
root.mainloop()
