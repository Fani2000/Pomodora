import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from os import path
from os.path import join


class App:
    """
    The UI app for the whole app including the buttons and other pages
    """

    def __init__(self):
        app = tk.Tk()
        # app.geometry("%dx%d+%d+%d" % (450, 300, 50, -10))
        app.title("Fani's pomodoro")
        app.configure(background="red")
        app.iconphoto(False, tk.PhotoImage(file="Fani.png"))
        app.configure(pady=10, padx=20)

        self.add_label()
        self.add_project_field()
        self.input_label()
        self.button()

        app.mainloop()

    def button(self):
        style = ttk.Style()
        style.configure(
            "TButton",
            background="red",
            foreground="white",
            justify="center",
            pady=15,
        )
        timer_btn = ttk.Button(
            text="Start",
            style="TButton"
        )
        timer_btn.grid(column=0, row=5, sticky="e",columnspan=4)

    def input_label(self):
        style = ttk.Style()
        style.configure(
            "TLabel",
            font=Font(size=12),
            foreground="white",
            background="red",
        )

        label = ttk.Label(
            text="Title: ",
            padding=[10, 10],
        )
        label.grid(
            row=3,
            column=0,
            sticky="w",
        )

        task_entry = tk.StringVar()
        entry = ttk.Entry(textvariable=task_entry)
        entry.grid(row=3, column=3)

        desc_label = ttk.Label(text="Description: ", padding=[10, 10])
        desc_label.grid(
            row=4,
            column=0,
            sticky="w",
        )

        desc_entry = tk.StringVar()
        entry = ttk.Entry(textvariable=desc_entry)
        entry.grid(row=4, column=3)

    def add_project_field(self):
        style = ttk.Style()
        style.configure(
            "TLabel", font=Font(size=12), foreground="white", background="red"
        )

        label = ttk.Label(
            text="Project: ",
            padding=[10, 10],
        )
        label.grid(
            column=0,
            row=2,
            columnspan=3,
            sticky="w",
        )

        select = ttk.Combobox()
        select["values"] = (
            "Q8 Demo app",
            "Recovery App",
            "Fleet Management",
            "Roads",
            "TicketingService",
        )
        select.grid(column=3, row=2, columnspan=2)

    def add_label(self):
        heading = Font(size=16, weight="bold")

        style = ttk.Style()
        style.configure("Label", font=heading, foreground="white", background="red")

        label = ttk.Label(text="Welcome back, Fani", style="Label", padding=(10, 10))
        label.grid(row=0, column=0, columnspan=4)
