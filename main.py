from modules import *


def VerifyEmail():
    is_valid = validate_email(mail.get())
    if (is_valid):
        response.config(text="This email exists", fg="green")
    else:
        response.config(text="This email does not exist", fg="red")
    mail.set("")


'''is_valid = validate_email("yahya.mazouar@viacesi.fr")
print(is_valid)'''

root = Tk() # Creat tkinter object
mail = StringVar()
root.resizable(0, 0)
root.geometry("700x450") # ANCHURA - ALTURA
root.title("Mail Verificator") # Window Title

title = Label(root, text="Mail Verificator", font=("Verdana", 30))
title.pack()

Label(root, text="").pack() # SEPARATOR

description = Label(root, text="Welcome to Mail Verificator, if you want to verify if an email exists\nenter it and click on the 'Verify' button", font=("Verdana", 10))
description.pack()

Label(root, text="").pack() # SEPARATOR

input_text = Entry(root, justify="center", width=35, textvariable=mail)
input_text.pack()

Label(root, text="").pack() # SEPARATOR

btn_verify = Button(root, text = "Verify email", command=VerifyEmail, bd=8)
btn_verify.pack()

Label(root, text="").pack() # SEPARATOR

response = Label(root)
response.pack()


















root.mainloop()