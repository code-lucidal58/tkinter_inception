from tkinter import *


def callback():
    result = textEditor.get(1.0, END)  # meaning 1st word to end
    print("TextEditor text is", result)


root = Tk()

textEditor = Text(root, width=30, height=10, font="Roboto 16", wrap=WORD)
textEditor.grid(row=0, column=0, pady=20, padx=40)
textEditor.insert(INSERT, "Hello! I am tkinter widget")
textEditor.config(state="disable")  # edit removed
textEditor.config(state="normal")  # edit enabled

button = Button(root, text="Save", width=10, height=1, command=callback)
button.grid(row=3, column=0)

root.geometry("550x550")
root.mainloop()
