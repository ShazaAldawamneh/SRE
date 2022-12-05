from random import randint
from tkinter import *

import Routes
from Controller import Controller


class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Demo")
        self.master.geometry("800x800")
        self.master.resizable(True, True)
        self.master.configure(bg="black")
        self.master.protocol("WM_DELETE_WINDOW", self.exit)
        self.create_widgets()

    def create_widgets(self):
        self.btn = Button(self.master, text="Run", command=self.click)
        self.btn.pack()

        self.btn = Button(self.master, text="Stop", command=self.clickStop)
        self.btn.pack()

    def click(self):
        controller = Controller(1, 30, 10)
        controller.start_of_day()
        controller.loop()
        text = Text(self.master, width=50, height=40)
        text.pack()
        for bus in controller.buses:
            text.insert(END, bus)
            text.insert(END,"\n")


    def clickStop(self):
        pass


    def exit(self):
        self.master.destroy()


class Main:
    def __init__(self):
        self.root = Tk()
        self.gui = GUI(self.root)
        self.root.mainloop()


if __name__ == "__main__":
    Main()
