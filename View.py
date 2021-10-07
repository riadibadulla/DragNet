from tkinter import *
from tkinter import ttk

class Main_menu:

    def __init__(self, master):
        self.label = ttk.Label(master, text="Welcome to the DragNet")
        self.label.grid(row=0,column=1, columnspan=2)

        ttk.Button(master, text="Conv2D", command = self.button_drag).grid(row=1,column=0)
        ttk.Button(master, text="Dense", command=self.button_drag).grid(row=2, column=0)

    def button_drag(self):
        pass


def main():
    root = Tk()
    app = Main_menu(root)
    root.mainloop()

if __name__ == '__main__':
    main()