import tkinter
from tkinter import *
from PIL import ImageTk, Image
import time
import requests


root = Tk()
# root.configure(bg="White")
root.geometry("1280x720")
root.title("DAV Login")
root.resizable(width=False, height=True)
root.iconbitmap("LOGO.ico")
# title frame
frame1 = LabelFrame(root, bg="Red")
frame1.pack()
# main frame
frame3 = Frame(root, bg="White")
frame3.pack(fill='both')
frame3.pack_forget()
# login frame
frame2 = LabelFrame(root, bg="White", width="18", labelanchor="n")
frame2.pack(pady=200, ipadx=10, ipady=10)

# Title image
img = ImageTk.PhotoImage(Image.open("LOGO.png"))
my_img_lbl = Label(frame1, image=img, bg="Red")
my_img_lbl.grid(row=0, column=1)
# Title
title = Label(frame1, text="D.A.V International School, Kharghar", font=("Times New Roman", 30, 'bold'), fg="White", width=38, bg="Red")
title.grid(row=0, column=2)
# clock
label = Label(frame1, font=("Times New Roman", 30, 'bold'), bd=30, fg="White", bg="Red")
label.grid(row=0, column=3)


def digitalclock():
    text_input = time.strftime("%H:%M:%S")
    label.config(text=text_input)
    label.after(200, digitalclock)


digitalclock()
# clock end
# Login part
userid = Label(frame2, text="Login ID:", width=20, font=("Times New Roman", 10, 'bold'), fg="Black", bg="White")
userid.grid(row=2, column=1, pady=(20, 10))


def clear_login_insert(var):
    user.delete(0, tkinter.END)


def clear_pass_insert(var):
    password.delete(0, tkinter.END)


def login():
    resp = requests.get('http://127.0.0.1:5000/login/' + user.get() + '/' + password.get()).text
    if resp == "Success":
        frame2.pack_forget()
        frame3.pack()
    elif resp == "Email or password Not Found":
        respon = Label(frame2, text="User or password Not Found", bg="White", width=30, fg="Red")
        respon.grid(row=1, column=1, columnspan=2)
    elif resp == "User not found, Please enter a valid user":
        respon = Label(frame2, text="User not found, Please enter a valid user", bg="White", width=30, fg="Red")
        respon.grid(row=1, column=1, columnspan=2)
    elif resp == "Incorrect Password":
        respon = Label(frame2, text="Incorrect Password", bg="White", width=30, fg="Red")
        respon.grid(row=1, column=1, columnspan=2)


user = Entry(frame2, width=40, font=("Times New Roman", 10, 'bold'))
user.insert(0, "Enter your user ID / Email ID")
user.grid(row=2, column=2, pady=(20, 10))
user.bind("<Button-1>", clear_login_insert)

passtxt= Label(frame2, text="Password", width=20, font=("Times New Roman", 10, 'bold'), fg="Black", bg="White")
passtxt.grid(row=3, column=1, pady=(10, 10))
password = Entry(frame2, width=40, font=("Times New Roman", 10, 'bold'), show="*")
password.grid(row=3, column=2)
password.insert(0, "Enter Password")
password.bind("<Button-1>", clear_pass_insert)


login_button = Button(frame2, text="Login", command=login, fg="Red", bg="white")
login_button.grid(row=4, column=1, columnspan=2, pady=(10, 20))





root.mainloop()
