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

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website :{
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("D:\\Python\\Password-Manager\\data.json", "r") as data_file:
                    data = json.load(data_file)
                    
            except FileNotFoundError:
                create_file = messagebox.askquestion(title= "FILE NOT EXIST", message= "You want to create a file?")
                if create_file == "yes":
                    with open("D:\\Python\\Password-Manager\\data.json", "w") as data_file:
                        json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("D:\\Python\\Password-Manager\\data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def search():
    website = website_entry.get()
    try:
        with open("D:\\Python\\Password-Manager\\data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title = "ERROR", message= "No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title = website, message= f"your {website.upper()} \nusername/E-mail: {email}"
                                f"\nPassword: {password}")
        else:
            messagebox.showwarning(title= "This Website Doesn't Exist", message="There is no Email Password for this website.")

 

# ---------------------------- UI SETUP ------------------------------- #

#Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#f7f5dd")

#LOGO
canvas = Canvas(height=200, width=200, bg="#f7f5dd", highlightthickness=0)
logo_img = PhotoImage(file="D:\\Python\\Password-Manager\\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", bg="#f7f5dd", fg="#333")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", bg="#f7f5dd", fg="#333")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", bg="#f7f5dd", fg="#333")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21, bg="#fffbe7", fg="#333", insertbackground="#333")
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35, bg="#fffbe7", fg="#333", insertbackground="#333")
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "shahzaibe374@gmail.com")
password_entry = Entry(width=21, bg="#fffbe7", fg="#333", insertbackground="#333")
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=13, command=search, bg="#e1bee7", fg="#333", activebackground="#ce93d8")
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password, bg="#b3e5fc", fg="#333", activebackground="#81d4fa")
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save, bg="#c8e6c9", fg="#333", activebackground="#a5d6a7")
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
