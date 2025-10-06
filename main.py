from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
#------------------------------------ CONSTANT ------------------------------------#
VERSION_APP = 'version 1.0'
#------------------------------------ PASSWORD GENERATOR ------------------------------------#
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letter = [choice(letters) for _ in range(nr_letters)]
    password_symbol = [choice(symbols) for _ in range(nr_symbols)]
    password_number = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_symbol + password_number


    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

#------------------------------------ SAVE PASSWORD ------------------------------------#
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
         messagebox.showinfo(title='Oops',message="please make sure you haven't left any fields empty")
    else:
        boolean_OK = messagebox.askokcancel(title=website,message=f'there are the details entered: \nEmail: {email}\nPassword: {password} \nIt is ok to save it ?')
    
        if boolean_OK:
                with open('data.txt',mode='a') as data_file:
                    data_file.write(f"{website} | {email} | {password}\n")
                    website_entry.delete(0, END)
                    password_entry.delete(0,END)


#------------------------------------ UI SETUP ------------------------------------#
windown = Tk()
windown.title('password manageer GUI')
windown.config(padx=10,pady=10)
canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0, column=1)

#labelS
website_label = Label(text='website')
website_label.grid(row=1,column=0)

email_label = Label(text='Email/Username')
email_label.grid(row=2,column=0)

password_label = Label(text='password')
password_label.grid(row=3,column=0)

version_label = Label(text=VERSION_APP)
version_label.grid(row=6, column=2)

#entries
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,'Usergmail@gmail.com')

password_entry = Entry(width=35)
password_entry.grid(row=3,column=1,columnspan=2)
password_entry.insert(0,'Ex:12345...')

#buttons
generate_password_button = Button(text='Generate password',command=password_generator)
generate_password_button.grid(row=3,column=2)

add_button = Button(text='Add',width=36,command=save_password)
add_button.grid(row=4,column=1,columnspan=2)

windown.mainloop()
