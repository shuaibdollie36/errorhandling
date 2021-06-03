
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Account Balance")
window.geometry("400x300")
window.config(bg="red")

top_label = Label(window, text="Please enter your amount below: ", bg="white")
top_label.place(x=84, y=10)
input_label = Entry(window)
input_label.place(x=110, y=70)

def qualify():
    funds = input_label.get()
    try:
        funds = int(funds)
        if funds < 3000:
            messagebox.showerror(" Declined ", "Insufficient funds.")
        else:
            messagebox.showinfo("Congratulations", "You qualify for the trip to Dubai")
    except ValueError:
        messagebox.showerror("Error", "Please insert a valid number.")


def exit_program():
    window.destroy()

qualify_btn = Button(window, text="Check Qualification", command=qualify)
qualify_btn.place(x=115, y=170)
exit_btn = Button(window, text="Exit", fg="black", command=exit_program)
exit_btn.place(x=165, y=260)
window.mainloop()
