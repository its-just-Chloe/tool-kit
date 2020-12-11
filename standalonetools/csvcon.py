# Author: Nico Schmidt
# Date: December 10th 2020
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd

root = Tk()
root.geometry("450x150")
root.title("CSV Converter")

filecsv = StringVar()

filename = ""


# Converts , to ; and . to ,
def us_to_eu():
    fname = filecsv.get()
    print(fname)
    data = ""
    with open(fname, 'r') as file:
        data = file.read().replace(',', ';').replace('.', ',')

    with open(fname, "w") as out_file:
        out_file.write(data)


# converts , to . and ; to ,
def eu_to_us():
    fname = filecsv.get()
    data = ""
    with open(fname, 'r') as file:
        data = file.read().replace(',', '.').replace(';', ',')

    with open(fname, "w") as out_file:
        out_file.write(data)


entry = Label(root, text="Enter File Path:")
entry.place(x=30, y=10)

fileentry = Entry(root, width=20, font=("Arial", 18, ""), textvariable=filecsv)
fileentry.place(x=30, y=45)


def setentry():
    name = fd.askopenfilename()
    fileentry.delete(0, END)
    fileentry.insert(0, name)
    return


fileex = Button(text='Click to Open File', command=setentry)
fileex.place(x=300, y=45)

btn1 = Button(root, text="US to EU", command=us_to_eu)
btn1.place(x=30, y=85)

btn2 = Button(root, text="EU to US", command=eu_to_us)
btn2.place(x=120, y=85)

root.mainloop()
