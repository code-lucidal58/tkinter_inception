from tkinter import *
from tkinter import ttk  # a submodule in tkinter


def save_form_values():
    name = name_field.get()
    company = company_field.get()
    dob = dob_field.get()
    password = password_field.get()
    result["text"] = "Entry submitted"
    result.config(fg="green", font="Roboto 15")


if __name__ == '__main__':
    root = Tk()
    # size of window
    root.geometry("500x450")

    # Basic Widgets
    label = Label(root, text="Fill in the details below", justify=LEFT)
    label.config(font="Roboto 15", fg="blue", bg="white")
    label.pack()

    # Field Full Name
    name_field = ttk.Entry(root, width=30)
    name_field.pack()

    # Field Company
    company_field = ttk.Entry(root, width=30)
    company_field.pack()

    # Field DOB
    dob_field = ttk.Entry(root, width=30)
    dob_field.insert(0, "dd-mm-yyyy")
    dob_field.pack()
    # make this field read only
    dob_field.state(["readonly"])

    # Field Password
    password_field = ttk.Entry(root, width=30)
    password_field.config(show="*")
    password_field.pack()
    # to disable entry field and then enable
    password_field.state(["disabled"])
    password_field.state(["!disabled"])

    submitButton = Button(root, text="Submit", command=save_form_values)
    submitButton["state"] = "normal"
    button2 = ttk.Button(root, text="Cancel")
    submitButton.pack()  # geometry manager. here it is pack
    button2.pack()

    result = Label(root)
    result.pack()

    root.mainloop()
