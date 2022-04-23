import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-640V7J3;'
                      'Database=ScanInvoiceDB;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
