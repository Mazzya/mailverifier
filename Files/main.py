from modules import *

def About():
    MessageBox.showinfo("About", "Developer github profile : www.github.com/Mazzya\n"
                                 " \n"
                                 "The code of this program is totally accessible and free on GitHub, you can contribute for free, either with code or with documentation.\n"
                                 " \n"
                                 "Project repository : www.github.com/mailverificator\n"
                                 " \n"
                                 "Current Version : 1.0.1 - Beta")

def Quit():
    choice = MessageBox.askyesno("Exit", "Are you sure you want exit ?")
    if (choice):
        root.quit()

def VerifyEmail():
    if (mail.get() == ""):
        response.config(text="You have to introduce an email", fg="black", font=("Calibri Bold", 12))
    else:
        is_valid = validate_email(mail.get())
        if (is_valid):
            response.config(text="This email exists", fg="green", font=("Calibri Bold", 12))
        else:
            response.config(text="This email does not exist", fg="red", font=("Calibri Bold", 12))
        mail.set("")

root = Tk() # Create tkinter object

# Window configuration
mail = StringVar()
root.resizable(0, 0)
root.iconbitmap('icon.ico') # Window icon
root.geometry("700x350") # WIDTH - HEIGHT
root.title("Mail Verificator") # Window Title

# Menu configuration
menubar = Menu(root)
root.config(menu=menubar)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=About)
helpmenu.add_separator()
helpmenu.add_command(label="Exit", command=Quit)
menubar.add_cascade(label="Help", menu=helpmenu)


title = Label(root, text="Mail Verificator", font=("Calibri Bold", 30))
title.pack()

Label(root, text="").pack() # SEPARATOR

description = Label(root, text="Welcome to Mail Verificator, if you want to verify if an email exists\nenter it and click on the 'Verify' button", font=("Calibri Bold", 10))
description.pack()

Label(root, text="").pack() # SEPARATOR

input_text = Entry(root, justify="center", width=35, textvariable=mail, bd=5)
input_text.pack()

Label(root, text="").pack() # SEPARATOR

btn_verify = Button(root, text = "Verify email", command=VerifyEmail, bd=5, font=("Calibri Bold", 10), cursor="hand2")
btn_verify.pack()

Label(root, text="").pack() # SEPARATOR

response = Label(root)
response.pack()

Label(root, text="").pack() # SEPARATOR

version = Label(root, text="V 1.0.1 - BETA", bg="white", pady=5, padx=5, font=("Calibri Bold", 10))
version.pack(anchor = "sw", side="left", pady=5, padx=5)


root.mainloop()