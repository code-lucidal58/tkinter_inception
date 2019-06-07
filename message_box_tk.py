from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()


def callback():
    mbox = messagebox.askquestion("Delete", "Are you sure?", icon="warning")
    if mbox == "yes":
        print("Deleted")
    else:
        print("Not deleted")


def callback2():
    messagebox.showinfo("Success", "Well done!")
    print("You clicked Ok")


button1 = ttk.Button(root, text="Delete", command=callback).grid(row=0, column=0, pady=25, padx=50)
button2 = ttk.Button(root, text="Info", command=callback2).grid(row=0, column=1)

root.geometry("350x250")
root.mainloop()
