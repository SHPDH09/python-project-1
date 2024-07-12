import tkinter as tk
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="lightgray")

# Create an entry widget for displaying calculations
entry = tk.Entry(root, width=35, borderwidth=5, font=('Arial', 18, 'bold'))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Variable to store the result of the last calculation
last_result = None

# Define button click function
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

# Define button clear function
def button_clear():
    entry.delete(0, tk.END)

# Define button equal function
def button_equal():
    global last_result
    try:
        result = eval(entry.get())
        last_result = result  # Update the last result
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Define button for different operations
def button_operation(operator):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + operator)

# Define button creation function
def create_button(text, row, column, command, bg_color):
    button = tk.Button(root, text=text, padx=20, pady=20, command=command, bg=bg_color, fg="white", font=('Arial', 14, 'bold'), activebackground="darkgray")
    button.grid(row=row, column=column, padx=5, pady=5)

# Colors
number_color = "#4CAF50"
operation_color = "#2196F3"
special_color = "#FF5722"

# Create number buttons with correct lambda usage
for i in range(1, 10):
    create_button(str(i), (i-1)//3 + 1, (i-1)%3, lambda num=i: button_click(num), number_color)
create_button("0", 4, 0, lambda: button_click(0), number_color)

# Create operation buttons
create_button("+", 1, 3, lambda: button_operation('+'), operation_color)
create_button("-", 2, 3, lambda: button_operation('-'), operation_color)
create_button("*", 3, 3, lambda: button_operation('*'), operation_color)
create_button("/", 4, 3, lambda: button_operation('/'), operation_color)
create_button("=", 4, 2, button_equal, special_color)
create_button("C", 4, 1, button_clear, special_color)

# Run the main loop
if __name__ == "__main__":
    root.mainloop()
