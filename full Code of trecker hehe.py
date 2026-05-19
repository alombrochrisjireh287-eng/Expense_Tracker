# Expense Tracker System with GUI
# Beginner Friendly Python Project
# Uses:
# - Tkinter (Window Widgets)
# - File Handling
# - Error Handling

from tkinter import *
from tkinter import messagebox

# Dark mode colors
BG_COLOR = "#2b2b2b"
FG_COLOR = "#f0f0f0"
ENTRY_BG = "#3c3f41"
ENTRY_FG = "#f8f8f2"
BUTTON_BG = "#44475a"
BUTTON_FG = "#f8f8f2"
TEXT_BG = "#272822"
TEXT_FG = "#f8f8f2"
OPTION_BG = "#44475a"
OPTION_FG = "#f8f8f2"

# Function to save expense
def save_expense():
    global entry_item, entry_amount, entry_quantity, category_var

    try:
        item = entry_item.get()
        amount = entry_amount.get()
        quantity = entry_quantity.get()
        category = category_var.get()

        # Check if fields are empty
        if item == "" or amount == "" or quantity == "":
            messagebox.showerror("Error", "Please fill all fields.")
            return

        # Check if amount is a number
        amount_value = float(amount)
        quantity_value = float(quantity)

        file = open("expenses.txt", "a")

        file.write(item + " | " + quantity + " | " + amount + " | " + category + "\n")

        file.close()

        messagebox.showinfo("Success", "Expense Saved!")

        # Clear entries
        entry_item.delete(0, END)
        entry_amount.delete(0, END)
        entry_quantity.delete(0, END)

    except ValueError:
        messagebox.showerror("Error", "Amount and Quantity must be numbers.")

    except:
        messagebox.showerror("Error", "Something went wrong.")
