from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD SEARCH ------------------------------- #
def find_password():
    # Grabs user search keyword, then trys to search the data.json file if the file exist
    try:
        website = website_input.get()
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\n Password: {password}")
    except FileNotFoundError:
        messagebox.showinfo(title=None, message="No Data File Found, save at least one password first.")
    except KeyError:
        messagebox.showinfo(title=None, message="No details for the entered website exist.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    # Populate password_list with random characters, symbols, and numbers
    password_list += [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    # Shuffle password_list to mix up the order from above
    shuffle(password_list)

    # Extract each character from password_list into the variable "password"
    password = ""
    for char in password_list:
        password += char

    # Check if password field has already been generated or not
    if len(password_input.get()) == 0:
        password_input.insert(0, password)
        pyperclip.copy(password)
    else:
        password_input.delete(0, 'end')
        password_input.insert(0, password)
        pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Stores user input into their respective variables. Then creates the new dictionary key/value pair
    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }
    }
    # Checks to see if the user has left the website or password field blank
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Empty Fields", message="Please don't leave any fields blank.")
    else:
        # Checks to see if the data.json file exist before saving, if it doesn't. The exception handling creates it.
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Creates Dictionary Key/Value Pair for storage
            data.update(new_data)
            # Writes new Key/Value pair to the data.json file
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
            # Clear Website, and Password Field after writing to file
            website_input.delete(0, 'end')
            password_input.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Buttons
add_button = Button(text="Add", command=save, width=40)
add_button.grid(column=1, row=4, columnspan=2)
generate_button = Button(text="Generate Password", command=password_generator, width=15)
generate_button.grid(column=2, row=3)
search_button = Button(text="Search", command=find_password, width=15)
search_button.grid(column=2, row=1)

# Input Fields
website_input = Entry(width=22)
website_input.grid(column=1, row=1)
website_input.focus()
email_username_input = Entry(width=42)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(0, "john.dough@gmail.com")
password_input = Entry(width=22)
password_input.grid(column=1, row=3)

# Keeps Tkinter window from disappearing when program starts
window.mainloop()
