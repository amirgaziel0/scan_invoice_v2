from sys import version_info

if version_info.major == 2:
    import Tkinter as tk
elif version_info.major == 3:
    import tkinter as tk

from functools import partial

app = tk.Tk()
labelExample = tk.Button(app, text="0")

def test22(num):
    print(num)

def testt(num):
    test22(num)

buttonExample = tk.Button(app, text="Increase", width=30,
                            command=testt(3))


labelExample.pack()
app.mainloop()