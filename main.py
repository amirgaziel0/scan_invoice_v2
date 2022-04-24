from tkinter import *
from tkinter import *
import DB

master = Tk()
master.title("Invoice Manager")




def save_click():

    query = "INSERT INTO [dbo].[Upload_Invoice] ([Company Name],[Date] ,[Product] ,[Price] ,[Payment] ,[Guarantee] ," \
            "[Description] , [Link] ,[File]) VALUES (? ,? ,? ,? ,? ,? ,? ,? ,?) "
    val = (company_name_tb.get("1.0",END),Date_tb.get("1.0",END),Product_tb.get("1.0",END),Price_tb.get("1.0",END),Payment_tb.get("1.0",END),Guarantee_tb.get("1.0",END),Description_tb.get("1.0",END),Link_tb.get("1.0",END),9)
    DB.cursor.execute(query, val)
    DB.cursor.commit()
    fr_upload.destroy()




def open_new_invoice():

    global company_name_tb
    global Date_tb
    global Product_tb
    global Price_tb
    global Payment_tb
    global Guarantee_tb
    global Description_tb
    global Link_tb
    global Upload_File_btn
    global fr_upload

    # be treated as a new window
    fr_upload = Toplevel(master)

    # sets the title of the
    # Toplevel widget
    fr_upload.title("New Invoice")

    # sets the geometry of toplevel
    fr_upload.geometry("1000x1000")

    # this will create a widget
    company_name_lb = Label(fr_upload, text="Company Name:")
    company_name_tb = Text(fr_upload, height=1, width=15)

    Date_lb = Label(fr_upload, text="Date:")
    Date_tb = Text(fr_upload, height=1, width=15)

    Product_lb = Label(fr_upload, text="Product:")
    Product_tb = Text(fr_upload, height=1, width=15)

    Price_lb = Label(fr_upload, text="Price:")
    Price_tb = Text(fr_upload, height=1, width=15)

    Payment_lb = Label(fr_upload, text="Payment:")
    Payment_tb = Text(fr_upload, height=1, width=15)

    Guarantee_lb = Label(fr_upload, text="Guarantee:")
    Guarantee_tb = Text(fr_upload, height=1, width=15)

    Description_lb = Label(fr_upload, text="Description:")
    Description_tb = Text(fr_upload, height=5, width=15)

    Link_lb = Label(fr_upload, text="Link:")
    Link_tb = Text(fr_upload, height=1, width=15)

    Upload_File_btn = Button(fr_upload, text='Upload File')

    Save_btn = Button(fr_upload, text='Save', command=save_click)

    back_btn = Button(fr_upload, text='Back', command=fr_upload_destroy)

    # rows and columns as specified
    company_name_lb.grid(row=0, column=0, sticky=W, pady=2)
    company_name_tb.grid(row=0, column=1, pady=2)

    Date_lb.grid(row=1, column=0, sticky=W, pady=2)
    Date_tb.grid(row=1, column=1, pady=2)

    Product_lb.grid(row=2, column=0, sticky=W, pady=2)
    Product_tb.grid(row=2, column=1, pady=2)

    Price_lb.grid(row=3, column=0, sticky=W, pady=2)
    Price_tb.grid(row=3, column=1, pady=2)

    Payment_lb.grid(row=4, column=0, sticky=W, pady=2)
    Payment_tb.grid(row=4, column=1, pady=2)

    Guarantee_lb.grid(row=5, column=0, sticky=W, pady=2)
    Guarantee_tb.grid(row=5, column=1, pady=2)

    Description_lb.grid(row=6, column=0, sticky=W, pady=2)
    Description_tb.grid(row=6, column=1, pady=2)

    Link_lb.grid(row=7, column=0, sticky=W, pady=2)
    Link_tb.grid(row=7, column=1, pady=2)

    Upload_File_btn.grid(row=8, column=1, pady=2)

    Save_btn.grid(row=9, column=1, pady=2)

    back_btn.grid(row=9, column=2, pady=2)


def show_all():

    global fr_Show_All
    fr_Show_All = Toplevel(master)
    fr_Show_All.title("New ")

    # sets the geometry of toplevel
    fr_Show_All.geometry("1000x1000")

    back_btn = Button(fr_Show_All, text='Back', command=fr_Show_All_destroy)

    DB.cursor.execute("SELECT * FROM Upload_Invoice")
    i = 0
    for student in DB.cursor:
        for j in range(len(student)):
            e = Entry(fr_Show_All, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, student[j])
        i = i + 1
        back_btn.grid(row=i, column=j, pady=2)

def fr_Show_All_destroy():
    fr_Show_All.destroy()

def fr_upload_destroy():
    fr_upload.destroy()

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

