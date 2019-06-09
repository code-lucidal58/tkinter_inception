from tkinter import *
from tkinter import ttk

from PIL import ImageTk


class ImageWindow:
    def __init__(self):
        self.root = Tk()
        self.btn = ttk.Button(self.root, text="show image", command=self.show_image)
        self.btn.grid(row=0, column=0)
        self.canvas = Canvas(self.root, width=1000, height=1000)
        self.canvas.grid(row=1, column=0)
        self.root.mainloop()

    def show_image(self):
        img = ImageTk.PhotoImage(file="index.png", master=self.root)
        self.canvas.create_image(0, 120, image=img)
        self.root.mainloop()


if __name__ == '__main__':
    ImageWindow()
