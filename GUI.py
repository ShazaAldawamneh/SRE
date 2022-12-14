from tkinter import *
from Simulation import Simulation
from Controller import Controller


class GUI:
    """Design of the Graphical User Interface (GUI)."""

    def __init__(self, master):
        self.label = None
        self.btn = None
        self.text = None
        self.master = master
        self.master.title("Demo")
        self.master.geometry("500x800")
        self.master.resizable(True, True)
        self.master.configure(bg="beige")
        self.master.protocol("WM_DELETE_WINDOW", self.exit)
        self.number_of_buses = IntVar()
        self.number_of_routes = IntVar()
        self.number_of_loops = IntVar()
        self.create_widgets()

    def create_widgets(self):
        """Creates the button and label (widgets) needed to run the simulation."""

        self.btn = Button(self.master, text="Run", command=self.run)
        self.btn.pack(side=TOP)

        self.btn = Button(self.master, text="Clear", command=self.clear)
        self.btn.pack(side=TOP)
        
        self.label = Label(self.master, text="Number of Buses:")
        self.label.pack(side=TOP)

        self.btn = Entry(self.master, textvariable=self.number_of_buses)
        self.btn.pack(side=TOP)

        self.label = Label(self.master, text="Number of Routes:")
        self.label.pack()

        self.btn = Entry(self.master, textvariable=self.number_of_routes)
        self.btn.pack(side=TOP)

        self.label = Label(self.master, text="Number of Loops:")
        self.label.pack()

        self.btn = Entry(self.master, textvariable=self.number_of_loops)
        self.btn.pack(side=TOP)

        self.text = Text(self.master, width=50, height=40, padx=10, pady=10)
        self.text.pack()

    def run(self):
        """Reads data from the GUI and input it on the simulation.
            The status of the buses (output) is printed off to a textbox on the last loop."""
        self.text.delete("1.0", END)

        controller = Controller(self.number_of_buses.get(), self.number_of_routes.get())
        Simulation.sim_on_click(controller, self.number_of_loops.get())
        for bus in controller.buses:
            self.text.insert(END, bus)
            self.text.insert(END, "\n")

    def clear(self):
        """Clears the textbox in which the output is printed off."""
        self.text.delete("1.0", END)

    def exit(self):
        """Exits the GUI."""
        self.master.destroy()


class Main:
    """Initialises the GUI."""

    def __init__(self):
        self.root = Tk()
        self.gui = GUI(self.root)
        self.root.mainloop()


if __name__ == "__main__":
    Main()
