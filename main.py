from tkinter import *
import random
def add_password():
    with open("password.txt", mode="a") as file:
        file.write(f"{web_text_field.get()} | {username_field.get()} | {password_field.get()}\n")

def ganarate_password():
    charactors = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
    password = ""
    for _ in range(16):
        password += random.choice(charactors)
    password_field.delete(0,END)
    password_field.insert(0,password)
    
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canves = Canvas(window, width=200, height=200)
image = PhotoImage(file="logo.png")
canves.create_image(120,100, image=image, anchor=CENTER)
# canves.pack(padx=(20,20),pady=(20,20))
canves.grid(row=0, column=1)
website_lable = Label(window, text="Website", font=("Arial", 16))
emil_lable = Label(window, text="Email", font=("Arial", 16))
password_lable = Label(window, text="Password", font=("Arial", 16))
website_lable.grid(row=1, column=0, padx=(20,0))
emil_lable.grid(row=2, column=0,padx=(20,0))
password_lable.grid(row=3, column=0,padx=(20,0))

# entry
web_text_field = Entry(window, font=("Arial", 16),width=38)
web_text_field.focus()
username_field = Entry(window, font=("Arial", 16),width=38)
password_field = Entry(window, font=("Arial", 16),width=21)


username_field.grid(row=2, column=1, columnspan=2,padx=(10,10))
password_field.grid(row=3, column=1,padx=(10,0))
password_genaration_button = Button(window, text="Generate Password", font=("Arial", 14),width=14,command=ganarate_password)
password_genaration_button.grid(row=3, column=2,padx=(0,10))
web_text_field.grid(row=1, column=1, columnspan=2,padx=(10,10))
add_button = Button(window, text="Add", font=("Arial", 14),width=35,command=add_password)
add_button.grid(row=4,column=1,columnspan=2,pady=(0,30),padx=(0,0))

window.mainloop()