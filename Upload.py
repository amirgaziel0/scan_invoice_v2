from tkinter import *
from tkinter.ttk import *
import DB

# creating main tkinter window
fr_upload = Tk()
fr_upload.title("Invoice Upload")
fr_upload.geometry('300x320')


def save_click():
    query = "INSERT INTO [dbo].[Upload_Invoice] ([Company Name],[Date] ,[Product] ,[Price] ,[Payment] ,[Guarantee] ," \
            "[Description] , [Link] ,[File]) VALUES (? ,? ,? ,? ,? ,? ,? ,? ,?) "
    val = (company_name_tb.get('1.0', 'end'), Date_tb.get('1.0', 'end'), Product_tb.get('1.0', 'end'), Price_tb.get('1.0', 'end'), Payment_tb.get('1.0', 'end'), Guarantee_tb.get('1.0', 'end'), Description_tb.get('1.0', 'end'), Link_tb.get('1.0', 'end'), 9)
    DB.cursor.execute(query, val)
    DB.cursor.commit()
    fr_upload.destroy()
    import main

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

mainloop()
