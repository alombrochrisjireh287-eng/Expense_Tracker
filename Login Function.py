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

# Function to view expenses
def view_expenses():
    global text_area

    try:
        file = open("expenses.txt", "r")

        records = file.readlines()

        file.close()

        text_area.delete(1.0, END)

        if records:
            # Header
            header = "{:<20} {:<10} {:<10} {:<15} {:<12}\n".format("Expense Item", "Quantity", "Amount", "Category", "Total (PHP)")
            text_area.insert(END, header)
            text_area.insert(END, "-" * 67 + "\n")  # Separator line

            total_sum = 0.0

            # Data rows
            for record in records:
                parts = record.strip().split(" | ")
                if len(parts) == 4:
                    try:
                        qty = float(parts[1])
                        amt = float(parts[2])
                        total = qty * amt
                        total_sum += total
                        row = "{:<20} {:<10} {:<10} {:<15} {:.2f}\n".format(parts[0], parts[1], parts[2], parts[3], total)
                        text_area.insert(END, row)
                    except ValueError:
                        # Skip invalid lines
                        continue

            # Grand total
            text_area.insert(END, "\nGrand Total: {:.2f} PHP".format(total_sum))
        else:
            text_area.insert(END, "No expenses recorded yet.")

    except FileNotFoundError:
        messagebox.showerror("Error", "Expense file not found.")

    except:
        messagebox.showerror("Error", "Cannot open file.")

def create_main_window():
    global window, text_area, entry_item, entry_amount, entry_quantity, category_var

    # MAIN WINDOW
    window = Tk()
    window.title("Expense Tracker")
    window.geometry("500x500")
    window.configure(bg=BG_COLOR)

    # TITLE
    title_label = Label(window, text="Expense Tracker System", font=("Arial", 18), bg=BG_COLOR, fg=FG_COLOR)
    title_label.pack(pady=10)

    # ITEM
    label_item = Label(window, text="Expense Item", bg=BG_COLOR, fg=FG_COLOR)
    label_item.pack()

    entry_item = Entry(window, width=30, bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=FG_COLOR)
    entry_item.pack(pady=5)

    # AMOUNT
    label_amount = Label(window, text="Amount of Expense", bg=BG_COLOR, fg=FG_COLOR)
    label_amount.pack()

    entry_amount = Entry(window, width=30, bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=FG_COLOR)
    entry_amount.pack(pady=5)

 # QUANTITY
    label_quantity = Label(window, text="Quantity", bg=BG_COLOR, fg=FG_COLOR)
    label_quantity.pack()

    entry_quantity = Entry(window, width=30, bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=FG_COLOR)
    entry_quantity.pack(pady=5)

    # CATEGORY
    label_category = Label(window, text="Category", bg=BG_COLOR, fg=FG_COLOR)
    label_category.pack()

    category_var = StringVar()
    category_var.set("Food")

    category_menu = OptionMenu(
        window,
        category_var,
        "Food",
        "Transportation",
        "School",
        "Bills",
        "Others"
    )
    category_menu.config(bg=OPTION_BG, fg=OPTION_FG, activebackground=BUTTON_BG, activeforeground=BUTTON_FG, highlightthickness=0)
    category_menu["menu"].config(bg=OPTION_BG, fg=OPTION_FG)
    category_menu.pack(pady=5)
 # BUTTONS
    save_button = Button(window, text="Save Expense", command=save_expense)
    save_button.pack(pady=10)

    view_button = Button(window, text="View Expenses", command=view_expenses)
    view_button.pack(pady=5)


    # TEXT AREA
    frame = Frame(window)
    frame.pack(pady=10)

    # Horizontal scrollbar
    h_scrollbar = Scrollbar(frame, orient=HORIZONTAL)
    h_scrollbar.pack(side=BOTTOM, fill=X)

    # Vertical scrollbar
    v_scrollbar = Scrollbar(frame)
    v_scrollbar.pack(side=RIGHT, fill=Y)

    text_area = Text(frame, height=12, width=80, xscrollcommand=h_scrollbar.set, yscrollcommand=v_scrollbar.set, wrap=NONE)
    text_area.pack(side=LEFT)

    h_scrollbar.config(command=text_area.xview)
    v_scrollbar.config(command=text_area.yview)


    # RUN WINDOW
    window.mainloop()

def login():
    if entry_pass.get() == "admin123":
        login_window.destroy()
        create_main_window()
    else:
        messagebox.showerror("Error", "Incorrect password LOLOLOL")


def show_login_window():
    global login_window, entry_pass

    login_window = Tk()
    login_window.title("Login")
    login_window.geometry("500x500")
    login_window.configure(bg=BG_COLOR)
    login_window.resizable(False, False)

    label_pass = Label(login_window, text="Enter Password:", bg=BG_COLOR, fg=FG_COLOR)
    label_pass.pack(pady=10)

    entry_pass = Entry(login_window, show="*", bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=FG_COLOR)
    entry_pass.pack(pady=5)

    button_login = Button(login_window, text="Login", command=login, bg=BUTTON_BG, fg=BUTTON_FG, activebackground=BG_COLOR, activeforeground=FG_COLOR)
    button_login.pack(pady=10)

    login_window.mainloop()
    