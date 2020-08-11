from tkinter import Tk, Label, StringVar, Entry, Button
from functools import partial
from main import bot

def run(email, password):
    window.destroy()
    bot(email, password)

#window
window = Tk()  
window.geometry('400x150')  
window.title('classBot')
window.iconbitmap('icon.ico')

#username label and text entry box
Label(window, text="Email:").place(x=10, y=19)
email = StringVar()
Entry(window, textvariable=email).place(x=55, y=20, width=300)

#password label and password entry box
Label(window,text="Senha:").place(x=10, y=69)
password = StringVar()
Entry(window, textvariable=password, show='*').place(x=55, y=70, width=300)

submit = partial(run, email, password)

#login button
Button(window, text="Login", command=submit).place(x=120, y=110, width=150)

window.mainloop()

# 260300@aluno.colegioprovecto.com.br