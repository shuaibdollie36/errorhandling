
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Authorise")
root.geometry("400x400")
root.config(bg="red")

label = Label(root, text="Please Enter yout details ", bg="white")
label.place(x=90, y=5)
input_user = Label(root, text="Username", bg="white")
input_user.place(x=160, y=70)
user_entry = Entry(root)
user_entry.place(x=115, y=100)

input_pass = Label(root, text="Password", bg="white")
input_pass.place(x=160, y=150)
pass_entry = Entry(root)
pass_entry.place(x=115, y=180)

def verify():
    username = ["Mia", "Yamkela", "Kim", "Shuaib"]
    passwords = ["36", "35", "34", "33"]
    found = False
    for x1 in range(len(username)):
        if user_entry.get() == username[x1] and pass_entry.get() == passwords[x1]:
            found = True
    if found == True:
        messagebox.showinfo("STATUS", "Access granted")
        root.destroy()

    else:
        messagebox.showinfo("ERROR INFO", "Access denied")


def clear():
    user_entry.delete(0, END)
    pass_entry.delete(0, END)


def exit_program():
    root.destroy()

login_btn = Button(root, text="Login", fg="black", command=verify)
login_btn.place(x=30, y=250)
clear_btn = Button(root, text="Clear", fg="black", command=clear)
clear_btn.place(x=170, y=250)
exit_btn = Button(root, text="Exit", fg="black", command=exit_program)
exit_btn.place(x=300, y=250)

root.mainloop()
