from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            try:
                search = data[website]
                print(search)
                messagebox.showinfo(title="Result", message=f"{search['email']} \n {search['password']}")
            except KeyError:
                messagebox.showerror(title="Not Found", message="No details for the website exist.")
    except FileNotFoundError:
        messagebox.showinfo(title="No data file found", message="No Data File Found")


def save():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave the fields empty.")
    else:
        try:
            with open('data.json', 'r') as file:
                #Reading the old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
        website_entry.delete(0, 'end')
        password_entry.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, columnspan=3)
# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "hiren6@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
gen_password_btn = Button(text="Generate Password", command=generate_password)
gen_password_btn.grid(column=2, row=3)

search_btn = Button(text="Search", command=find_password)
search_btn.grid(column=2, row=1)


add_btn = Button(width=36, text="Add", command=save)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
