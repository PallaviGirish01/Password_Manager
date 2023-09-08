from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list=[choice(letters) for _ in range(randint(8,10))]
    symbols_list=[choice(symbols) for _ in range(randint(2,4))]
    numbers_list=[choice(numbers) for _ in range(randint(2,4))]

    password_list=letters_list+symbols_list+numbers_list
    shuffle(password_list)

    password="".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


def save():
    website=website_input.get()
    email=email_input.get()
    password=password_input.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops!!",message="Please don't leave any fields empty!!")
    else:
        msg_is_ok = messagebox.askokcancel(title=website, message="These are the details entered: \nEmail: {email}"
                                                                  f"\nPassword:{password} \nis ot ok to save?")
    if msg_is_ok:
        with open("data.txt","a") as file:
            file.write(f"{website} | {email} | {password}\n")
            website_input.delete(0,END)
            password_input.delete(0,END)


window = Tk()
window.title("Password Manager")

window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo)
canvas.grid(column=2, row=1)

# labels
website_label = Label(text="Website:")
website_label.grid(column=1, row=2)
email_label = Label(text="Email/Username:")
email_label.grid(column=1, row=3)
password_label = Label(text="Password:")
password_label.grid(column=1, row=4)

# inputs
website_input = Entry(width=35)
website_input.grid(column=2, row=2, columnspan=2)
email_input = Entry(width=35)
email_input.grid(column=2, row=3, columnspan=2)
email_input.insert(0,"pallavi@gmail.com")
password_input = Entry(width=21)
password_input.grid(column=2, row=4)

password_button = Button(text="Generate Password",command=generate_password)
password_button.grid(column=3, row=4)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=5, column=2, columnspan=2)

window.mainloop()
