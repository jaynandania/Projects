import tkinter as tk

# Function to evaluate the expression
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        history_listbox.insert(tk.END, expression + " = " + str(result))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator with History")

# Create an Entry widget for input
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for digits and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, command=lambda b=button: entry.insert(tk.END, b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create a Calculate button
tk.Button(root, text="Calculate", padx=40, pady=20, command=calculate).grid(row=row_val, columnspan=4)

# Create a Listbox for history
history_listbox = tk.Listbox(root, width=50, height=10)
history_listbox.grid(row=row_val+1, column=0, columnspan=4)

# Start the GUI main loop
root.mainloop()
