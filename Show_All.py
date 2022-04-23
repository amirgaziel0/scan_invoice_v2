import DB
import tkinter as tk
from tkinter import *

my_w = tk.Tk()
my_w.geometry("1000x900")


def quit_click():
    my_w.destroy()
    import main


Save_btn = Button(my_w, text='Back', command=quit_click)

DB.cursor.execute("SELECT * FROM Upload_Invoice")
i = 0
for student in DB.cursor:
    for j in range(len(student)):
        e = Entry(my_w, width=10, fg='blue')
        e.grid(row=i, column=j)
        e.insert(END, student[j])
    i = i + 1
    Save_btn.grid(row=i, column=j, pady=2)

my_w.mainloop()
