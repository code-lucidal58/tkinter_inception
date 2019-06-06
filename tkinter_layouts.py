from tkinter import *
from tkinter import ttk


def callback():
    print("Your name :" + entry.get())
    print("Your password: " + entry2.get())
    if chvar.get() == 1:
        print("remember me checked")
    else:
        print("remember me not selected")
    print("Gender is:", gender.get())
    print("Combo box selection:", months.get())
    print("Spin box value:", year.get())


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
# button.grid(row=3, column=1, sticky=E)
button.grid(row=3, column=1, sticky=E + W, pady=5)
button.config(command=callback)

chvar = IntVar()
chvar.set(0)
cbox = Checkbutton(root, text="Remember me", variable=chvar, font="Roboto 16") \
    .grid(row=4, column=0, sticky=E, columnspan=2)

gender = StringVar()
male_radio = ttk.Radiobutton(root, text="male", value="male", variable=gender)
male_radio.grid(row=5, column=0)
female_radio = ttk.Radiobutton(root, text="female", value="female", variable=gender)
female_radio.grid(row=5, column=1)

# Spinner
months = StringVar()
combo_box = ttk.Combobox(root, textvariable=months, values=("Jan", "Feb", "Mar", "Apr"), state="readonly")
combo_box.grid(row=6, column=0)

# Scroller: not available in ttk
year = StringVar()
spin_box = Spinbox(root, from_=1990, to=2018, textvariable=year, state="readonly")
spin_box.grid(row=6, column=1)

root.geometry("500x450")
root.mainloop()
