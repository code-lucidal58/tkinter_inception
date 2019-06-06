from tkinter import *
from tkinter import ttk

root = Tk()
entry = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=30)

entry.insert(0, "Enter name")
entry2.insert(0, "Enter password")
button = ttk.Button(root, text="Enter")

title = ttk.Label(text="Title of Form", font=("Arial", 22))
name_title = ttk.Label(text="Your name: ")
pwd_title = ttk.Label(text="Your password: ")

title.grid(row=0, column=0, columnspan=2)
name_title.grid(row=1, column=0, sticky=W)
pwd_title.grid(row=2, column=0)
entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)

chvar = IntVar()
chvar.set(0)
cbox = Checkbutton(root, text="Remember me", variable=chvar, font="Roboto 16") \
    .grid(row=4, column=0, sticky=E, columnspan=2)

# button.grid(row=3, column=1, sticky=E)
button.grid(row=3, column=1, sticky=E + W, pady=5)

root.geometry("500x450")
root.mainloop()
