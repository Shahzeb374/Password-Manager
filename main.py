# import json
# import pyperclip
# from tkinter import *
# from tkinter import messagebox
# from random import choice, randint, shuffle
# import ttkbootstrap as tb
# from ttkbootstrap.constants import *

# # ---------------------------- PASSWORD GENERATOR ------------------------------- #
# def generate_password():
#     letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     numbers = '0123456789'
#     symbols = '!#$%&()*+'

#     password_letters = [choice(letters) for _ in range(randint(8, 10))]
#     password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
#     password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

#     password_list = password_letters + password_symbols + password_numbers
#     shuffle(password_list)
#     password = "".join(password_list)

#     password_entry.delete(0, END)
#     password_entry.insert(0, password)
#     pyperclip.copy(password)

# # ---------------------------- SAVE PASSWORD ------------------------------- #
# def save():
#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()
#     new_data = {website: {"email": email, "password": password}}

#     if len(website) == 0 or len(password) == 0:
#         messagebox.showinfo(title="Oops", message="Please don’t leave any fields empty.")
#     else:
#         is_ok = messagebox.askokcancel(title=website, message=f"Details:\nEmail: {email}\nPassword: {password}")
#         if is_ok:
#             try:
#                 with open("D:\\Python\\Password-Manager\\data.json", "r") as data_file:
#                     data = json.load(data_file)
#             except FileNotFoundError:
#                 with open("D:\\Python\\Password-Manager\\data.json", "w") as data_file:
#                     json.dump(new_data, data_file, indent=4)
#             else:
#                 data.update(new_data)
#                 with open("D:\\Python\\Password-Manager\\data.json", "w") as data_file:
#                     json.dump(data, data_file, indent=4)
#             finally:
#                 website_entry.delete(0, END)
#                 password_entry.delete(0, END)

# # ---------------------------- SEARCH ------------------------------- #
# def search():
#     website = website_entry.get()
#     try:
#         with open("D:\\Python\\Password-Manager\\data.json", "r") as data_file:
#             data = json.load(data_file)
#     except FileNotFoundError:
#         messagebox.showerror(title="Error", message="No Data File Found.")
#     else:
#         if website in data:
#             email = data[website]["email"]
#             password = data[website]["password"]
#             messagebox.showinfo(title=website, message=f"Username: {email}\nPassword: {password}")
#         else:
#             messagebox.showwarning(title="Not Found", message="No details for this website exist.")

# # ---------------------------- UI SETUP ------------------------------- #
# # Modern themed window with soft look
# window = tb.Window(themename="flatly")   # Try: flatly, lumen, journal (sab light pastel look dete hain)
# window.title("🔐 Password Manager")
# window.geometry("520x500")

# # Logo
# logo = tb.Label(window, text="🔐 Password Manager", font=("Segoe UI", 18, "bold"), bootstyle="info")
# logo.pack(pady=20)

# # Frame
# frame = tb.Frame(window, padding=20, bootstyle="light")
# frame.pack(fill=X, padx=20, pady=10)

# # Labels & Entries
# tb.Label(frame, text="🌐 Website:", font=("Segoe UI", 11), bootstyle="secondary").grid(row=0, column=0, pady=5, sticky="w")
# website_entry = tb.Entry(frame, width=25, bootstyle="info")
# website_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
# website_entry.focus()

# tb.Label(frame, text="📧 Email/Username:", font=("Segoe UI", 11), bootstyle="secondary").grid(row=1, column=0, pady=5, sticky="w")
# email_entry = tb.Entry(frame, width=35, bootstyle="info")
# email_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=5, sticky="w")
# email_entry.insert(0, "shahzaibe374@gmail.com")

# tb.Label(frame, text="🔑 Password:", font=("Segoe UI", 11), bootstyle="secondary").grid(row=2, column=0, pady=5, sticky="w")
# password_entry = tb.Entry(frame, width=25, bootstyle="info")
# password_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# # Buttons (soft pastel colors)
# search_button = tb.Button(frame, text="🔍 Search", bootstyle="warning-outline", command=search)
# search_button.grid(row=0, column=2, padx=10)

# generate_button = tb.Button(frame, text="⚡ Generate", bootstyle="info-outline", command=generate_password)
# generate_button.grid(row=2, column=2, padx=10)

# add_button = tb.Button(window, text="💾 Save Password", bootstyle="success", command=save, width=30)
# add_button.pack(pady=20)

# # Footer
# footer = tb.Label(window, text="Made with ❤️ by Shahzeb", font=("Segoe UI", 9), bootstyle="secondary")
# footer.pack(side=BOTTOM, pady=10)

# window.mainloop()

"""
second code
"""

# import json
# import pyperclip
# from tkinter import *
# from random import choice, randint, shuffle
# import ttkbootstrap as tb
# from ttkbootstrap.constants import *

# # ---------------------------- PASSWORD GENERATOR ------------------------------- #
# def generate_password():
#     letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     numbers = '0123456789'
#     symbols = '!#$%&()*+'

#     password_letters = [choice(letters) for _ in range(randint(8, 10))]
#     password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
#     password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

#     password_list = password_letters + password_symbols + password_numbers
#     shuffle(password_list)
#     password = "".join(password_list)

#     password_entry.delete(0, END)
#     password_entry.insert(0, password)
#     pyperclip.copy(password)

#     update_status("✅ Password generated & copied to clipboard!", "success")


# # ---------------------------- SAVE PASSWORD ------------------------------- #
# def save():
#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()
#     new_data = {website: {"email": email, "password": password}}

#     if len(website) == 0 or len(password) == 0:
#         update_status("⚠️ Please don’t leave any fields empty!", "warning")
#     else:
#         try:
#             with open("D:\\Python\\Password-Manager\\data.json", "r") as data_file:
#                 data = json.load(data_file)
#         except FileNotFoundError:
#             data = {}

#         data.update(new_data)
#         with open("D:\\Python\\Password-Manager\\data.json", "w") as data_file:
#             json.dump(data, data_file, indent=4)

#         website_entry.delete(0, END)
#         password_entry.delete(0, END)
#         update_status("💾 Password saved successfully!", "success")


# # ---------------------------- SEARCH ------------------------------- #
# def search():
#     website = website_entry.get()
#     try:
#         with open("D:\\Python\\Password-Manager\\data.json", "r") as data_file:
#             data = json.load(data_file)
#     except FileNotFoundError:
#         update_status("❌ No Data File Found.", "danger")
#     else:
#         if website in data:
#             email = data[website]["email"]
#             password = data[website]["password"]
#             update_status(f"🌐 {website} → {email} | {password}", "info")
#         else:
#             update_status("⚠️ No details found for this website.", "warning")


# # ---------------------------- COPY PASSWORD ------------------------------- #
# def copy_password():
#     password = password_entry.get()
#     if password:
#         pyperclip.copy(password)
#         update_status("📋 Password copied to clipboard!", "success")
#     else:
#         update_status("⚠️ No password to copy!", "warning")


# # ---------------------------- SHOW / HIDE PASSWORD ------------------------------- #
# def toggle_password():
#     if password_entry.cget("show") == "":
#         password_entry.config(show="*")
#         show_button.config(text="👁️ Show")
#     else:
#         password_entry.config(show="")
#         show_button.config(text="🙈 Hide")


# # ---------------------------- STATUS UPDATE ------------------------------- #
# def update_status(message, style="info"):
#     status_label.config(text=message, bootstyle=style)


# # ---------------------------- UI SETUP ------------------------------- #
# window = tb.Window(themename="flatly")
# window.title("🔐 Password Manager")
# window.geometry("550x520")

# # Logo
# logo = tb.Label(window, text="🔐 Password Manager", font=("Segoe UI", 18, "bold"), bootstyle="info")
# logo.pack(pady=15)

# # Frame
# frame = tb.Frame(window, padding=20, bootstyle="light")
# frame.pack(fill=X, padx=20, pady=10)

# # Labels & Entries
# tb.Label(frame, text="🌐 Website:", font=("Segoe UI", 11), bootstyle="secondary").grid(row=0, column=0, pady=5, sticky="w")
# website_entry = tb.Entry(frame, width=25, bootstyle="info")
# website_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
# website_entry.focus()

# tb.Label(frame, text="📧 Email/Username:", font=("Segoe UI", 11), bootstyle="secondary").grid(row=1, column=0, pady=5, sticky="w")
# email_entry = tb.Entry(frame, width=35, bootstyle="info")
# email_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=5, sticky="w")
# email_entry.insert(0, "shahzaibe374@gmail.com")

# tb.Label(frame, text="🔑 Password:", font=("Segoe UI", 11), bootstyle="secondary").grid(row=2, column=0, pady=5, sticky="w")
# password_entry = tb.Entry(frame, width=25, bootstyle="info", show="*")
# password_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# # Buttons
# search_button = tb.Button(frame, text="🔍 Search", bootstyle="warning-outline", command=search)
# search_button.grid(row=0, column=2, padx=10)

# generate_button = tb.Button(frame, text="⚡ Generate", bootstyle="info-outline", command=generate_password)
# generate_button.grid(row=2, column=2, padx=10)

# show_button = tb.Button(frame, text="👁️ Show", bootstyle="secondary-outline", command=toggle_password)
# show_button.grid(row=2, column=3, padx=5)

# copy_button = tb.Button(frame, text="📋 Copy", bootstyle="primary-outline", command=copy_password)
# copy_button.grid(row=3, column=1, pady=5, sticky="w")

# add_button = tb.Button(window, text="💾 Save Password", bootstyle="success", command=save, width=30)
# add_button.pack(pady=20)

# # Status / Notification Area
# status_label = tb.Label(window, text="Welcome! Ready to manage your passwords 🔐", 
#                         font=("Segoe UI", 10), bootstyle="secondary", anchor="center")
# status_label.pack(fill=X, padx=10, pady=10)

# # Footer
# footer = tb.Label(window, text="Made with Love by Shahzeb", font=("Segoe UI", 9), bootstyle="secondary")
# footer.pack(side=BOTTOM, pady=10)

# window.mainloop()

"""
third code
"""

import json
import pyperclip
from tkinter import *
from random import choice, randint, shuffle
import ttkbootstrap as tb
from ttkbootstrap.constants import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

    update_status("✅ Password generated & copied to clipboard!", "success")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(password) == 0:
        update_status("⚠️ Please don’t leave any fields empty!", "warning")
    else:
        try:
            with open("D:\\Python\\Password-Manager\\data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            data = {}

        data.update(new_data)
        with open("D:\\Python\\Password-Manager\\data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        update_status("💾 Password saved successfully!", "success")


# ---------------------------- SEARCH ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open("D:\\Python\\Password-Manager\\data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        update_status("❌ No Data File Found.", "danger")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            update_status(f"🌐 {website} → {email} | {password}", "info")
        else:
            update_status("⚠️ No details found for this website.", "warning")


# ---------------------------- COPY PASSWORD ------------------------------- #
def copy_password():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        update_status("📋 Password copied to clipboard!", "success")
    else:
        update_status("⚠️ No password to copy!", "warning")


# ---------------------------- SHOW / HIDE PASSWORD ------------------------------- #
def toggle_password():
    if password_entry.cget("show") == "":
        password_entry.config(show="*")
        show_button.config(text="👁️ Show")
    else:
        password_entry.config(show="")
        show_button.config(text="🙈 Hide")


# ---------------------------- STATUS UPDATE ------------------------------- #
def update_status(message, style="info"):
    status_label.config(text=message, bootstyle=style)


# ---------------------------- UI SETUP ------------------------------- #
window = tb.Window(themename="flatly")
window.title("🔐 Password Manager")
window.geometry("550x520")

# Logo
logo = tb.Label(window, text="🔐 Password Manager", font=("Segoe UI", 18, "bold"), bootstyle="info")
logo.pack(pady=15)

# Frame
frame = tb.Frame(window, padding=20, bootstyle="light")
frame.pack(fill=X, padx=20, pady=10)

# Labels & Entries
tb.Label(frame, text="🌐 Website:", font=("Segoe UI", 11), bootstyle="secondary").grid(row=0, column=0, pady=5, sticky="w")
website_entry = tb.Entry(frame, width=25, bootstyle="info")
website_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
website_entry.focus()

tb.Label(frame, text="📧 Email/Username:", font=("Segoe UI", 11), bootstyle="secondary").grid(row=1, column=0, pady=5, sticky="w")
email_entry = tb.Entry(frame, width=35, bootstyle="info")
email_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=5, sticky="w")
email_entry.insert(0, "shahzaibe374@gmail.com")

tb.Label(frame, text="🔑 Password:", font=("Segoe UI", 11), bootstyle="secondary").grid(row=2, column=0, pady=5, sticky="w")
password_entry = tb.Entry(frame, width=25, bootstyle="info", show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Buttons
search_button = tb.Button(frame, text="🔍 Search", bootstyle="warning-outline", command=search)
search_button.grid(row=0, column=2, padx=10)

generate_button = tb.Button(frame, text="⚡ Generate", bootstyle="info-outline", command=generate_password)
generate_button.grid(row=2, column=2, padx=10)

show_button = tb.Button(frame, text="👁️ Show", bootstyle="secondary-outline", command=toggle_password)
show_button.grid(row=2, column=3, padx=5)

copy_button = tb.Button(frame, text="📋 Copy", bootstyle="primary-outline", command=copy_password)
copy_button.grid(row=3, column=1, pady=5, sticky="w")

add_button = tb.Button(window, text="💾 Save Password", bootstyle="success", command=save, width=30)
add_button.pack(pady=20)

# Status / Notification Area
status_label = tb.Label(window, text="Welcome! Ready to manage your passwords 🔐", 
                        font=("Segoe UI", 10), bootstyle="secondary", anchor="center")
status_label.pack(fill=X, padx=10, pady=10)

# Footer
footer = tb.Label(window, text="Made with ❤️ by Shahzeb", font=("Segoe UI", 9), bootstyle="secondary")
footer.pack(side=BOTTOM, pady=10)

window.mainloop()
