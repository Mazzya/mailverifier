from modules import *


def VerifyEmail():
    if (mail.get() == ""):
        response.config(text="You have to introduce an email", fg="black")
    else:
        is_valid = validate_email(mail.get())
        if (is_valid):
            response.config(text="This email exists", fg="green", font=("Verdana", 15))
        else:
            response.config(text="This email does not exist", fg="red")
        mail.set("")

root = Tk() # Creat tkinter object
mail = StringVar()
root.resizable(0, 0)
root.iconbitmap('icon.ico')
root.geometry("700x350") # ANCHURA - ALTURA
root.title("Mail Verificator") # Window Title

title = Label(root, text="Mail Verificator", font=("Calibri Bold", 30))
title.pack()

Label(root, text="").pack() # SEPARATOR

description = Label(root, text="Welcome to Mail Verificator, if you want to verify if an email exists\nenter it and click on the 'Verify' button", font=("Calibri Bold", 10))
description.pack()

Label(root, text="").pack() # SEPARATOR

input_text = Entry(root, justify="center", width=35, textvariable=mail, bd=5)
input_text.pack()

Label(root, text="").pack() # SEPARATOR

btn_verify = Button(root, text = "Verify email", command=VerifyEmail, bd=5, font=("Calibri Bold", 10))
btn_verify.pack()

Label(root, text="").pack() # SEPARATOR

response = Label(root)
response.pack()

Label(root, text="").pack() # SEPARATOR

version = Label(root, text="Version Beta")
version.pack(anchor = "sw", side="left", pady=5, padx=5)


















root.mainloop()