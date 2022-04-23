from tkinter import *
from tkinter.ttk import *
import DB

master = Tk()
master.title("Invoice Manager")


def open_new_invoice():
    master.destroy()
    import Upload

def show_all():
    master.destroy()
    import Show_All

# this will create a label widget
search_lb = Label(master, text="Search Box:")
search_tb = Entry(master)
search_btn = Button(master, text='Find')
upload_btn = Button(master, text='New Invoice', command=open_new_invoice)
showAll_btn = Button(master, text='Show All', command=show_all)

# grid method to arrange labels in respective
# rows and columns as specified
search_lb.grid(row=0, column=0, sticky=W, pady=2)
search_tb.grid(row=0, column=1, pady=2)
search_btn.grid(row=0, column=2, sticky=W, pady=2)
upload_btn.grid(row=1, column=0, sticky=W, pady=2)
showAll_btn.grid(row=2, column=0, sticky=W, pady=2)

master.mainloop()
