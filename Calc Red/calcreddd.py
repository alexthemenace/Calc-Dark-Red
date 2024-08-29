import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Dark Red Calculator")
window.configure(bg="darkred")

# Create entry field for displaying the calculation
entry = tk.Entry(window, width=30, font=("Arial", 16), bg="black", fg="red")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons for numbers and operators
buttons = {
    "7": (1, 0), "8": (1, 1), "9": (1, 2), "/": (1, 3),
    "4": (2, 0), "5": (2, 1), "6": (2, 2), "*": (2, 3),
    "1": (3, 0), "2": (3, 1), "3": (3, 2), "-": (3, 3),
    "0": (4, 0), ".": (4, 1), "=": (4, 2), "+": (4, 3)
}

for text, (row, col) in buttons.items():
    button = tk.Button(window, text=text, font=("Arial", 14), bg="black", fg="red",
                       command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Function to handle button clicks
def button_click(text):
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    else:
        entry.insert(tk.END, text)

# Start the main loop
window.mainloop()