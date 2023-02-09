import json
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip

input_website = None
input_email = None
input_pass = None
text_details = None


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    global input_pass
    input_pass.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    input_pass.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- Find Website ------------------------------- #
def find_website():
    # global input_website, input_pass
    # try:
    #     with open("data.json", "r") as data_file:
    #         data = json.load(data_file)
    #
    # except FileNotFoundError:
    #     pass
    # else:

        # for i in data.items():
        #     if i[0] == input_website.get():
        #         messagebox.askokcancel(title="Result", message=f"Email: {i[1]['email']}\n Password: {i[1]['password']}")

    global input_website
    website= input_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Result", message=f"There are no records" )
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Result", message=f"Email: {email}\n Password: {password}" )
        else:
            messagebox.showinfo(title="No Details", message=f"No details for {website}.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    global input_website, input_email, input_pass, text_details
    web = input_website.get()
    email = input_email.get()
    password = input_pass.get()
    details = text_details.get("1.0", END)
    new_data = {
        web: {"email": email,
              "password": password,
              "details": details}

    }
    if not web or not password:
        messagebox.askokcancel(title="No values", message="Please fill all values")

    else:

        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            input_website.delete(0, END)
            input_pass.delete(0, END)
            text_details.delete('1.0', END)


# ---------------------------- UI SETUP ------------------------------- #

def ui_setup():
    global input_pass, input_email, input_website, text_details
    window = Tk()
    window.title("Password Manager")
    window.config(padx=20, pady=20)

    label_website = Label(text="Website", font=("Arial", 9, "bold"))

    label_website.grid(row=1, column=0)

    label_email = Label(text="Email/Username:", font=("Arial", 9, "bold"))
    label_email.grid(row=2, column=0)
    label_pass = Label(text="Password:", font=("Arial", 9, "bold"))
    label_pass.grid(row=3, column=0)

    input_website = Entry(width=32)
    input_website.grid(row=1, column=1, pady=10)
    input_website.focus()
    btn_website = Button(text="Find", width=15, command=find_website)
    btn_website.grid(column=2, row=1)
    input_email = Entry(width=50)
    input_email.grid(row=2, column=1, columnspan=2)
    input_email.insert(0, "alex@gmail.com")
    input_pass = Entry(width=32)
    input_pass.grid(row=3, column=1)

    btn_generata = Button(text="Generate Password", command=generate_password, width=14)
    btn_generata.grid(column=2, row=3, pady=10)

    btn_add = Button(text="Add", width=50, command=save_pass)
    btn_add.grid(column=0, row=5, columnspan=3, pady=10)

    text_details = Text(height=5, width=50)
    text_details.grid(row=4, columnspan=3, column=0)

    window.mainloop()


ui_setup()
