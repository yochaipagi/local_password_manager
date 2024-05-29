# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import string
import random
import tkinter.messagebox
from tkinter import *
from tkinter import dialog, simpledialog, messagebox
import pyperclip
password = ""


# ---------------------------- SAVE PASSWORD ------------------------------- #


def generate_password():
    global password
    symbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    for i in range(4):
        password += random.choice(string.ascii_letters)
        password += random.choice(string.digits)
        password += random.choice(symbol)
    # Convert the password string to a list
    password_list = list(password)

    # Shuffle the list
    random.shuffle(password_list)

    # Convert the list back to a string
    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)



def validate_entries():
    if website_entry.get() == "":
        return False
    if email_entry.get() == "":
        return False
    if password_entry.get() == "":
        return False
    return True


def add_password():
    global password
    if validate_entries():
        website = website_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        save_flag = messagebox.askokcancel(title=website,
                                           message=f"These are the details entered: \nEmail: {email} \nPassword: {password} save?")
        if not save_flag:
            return
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
        messagebox.showinfo("Information", "Your password added properly")
        password_entry.delete(0, END)
        website_entry.delete(0, END)
        website_entry.focus()
    else:
        messagebox.showerror("Error", "Please fill all the entries")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "alice.bob@gmail.com")
password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)
# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=33, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)
# #User_Dialog
# user_common_email = simple-dialog.askstring("Email", "Enter your email")
# # with open(user_common_email, "w") as user_email_file:
# #     user_email_file.write(user_common_email)
# #     email_entry.insert(0, user_email_file.readline())
# email_entry.insert(0,user_common_email)

window.mainloop()
