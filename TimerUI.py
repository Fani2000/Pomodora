
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from os import path
from os.path import join


class Timer:
    """
    The UI app for the timer screen
    """

    def __init__(self):
        app = tk.Tk()
        # app.geometry("%dx%d+%d+%d" % (450, 300, 50, -10))
        app.title("Fani's pomodoro")
        app.configure(background="red")
        app.iconphoto(False, tk.PhotoImage(file="Fani.png"))
        app.configure(pady=10, padx=20)
        app.resizable(False, False)

        self.add_label()

        app.mainloop()

    def add_label(self):
        heading = Font(size=16, weight="bold")

        style = ttk.Style()
        style.configure("Label", font=heading,
                        foreground="white", background="red")

        label = ttk.Label(text="Welcome back, Fani",
                          style="Label", padding=(10, 10))
        label.grid(row=0, column=0, columnspan=4)
