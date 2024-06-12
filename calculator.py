import tkinter as tk
from tkinter import messagebox

def perform_calculation():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation")

        label_result.config(text=f"Result: {result}")

    except ValueError as ve:
        messagebox.showerror("Error", str(ve))

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place the widgets
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.grid(row=1, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

operation_var = tk.StringVar(root)
operation_var.set('+')  # default value

option_menu_operation = tk.OptionMenu(root, operation_var, '+', '-', '*', '/')
option_menu_operation.grid(row=2, column=0, columnspan=2, pady=10)

button_calculate = tk.Button(root, text="Calculate", command=perform_calculation)
button_calculate.grid(row=3, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="Result:")
label_result.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
