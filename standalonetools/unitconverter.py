# Author: Nico Schmidt
# Date: December 11 2020

from tkinter import *

# List to choose which Unit to convert from
Unit_fromList = [
    "Meter",
    "Kilometer",
    "Millimeter",
    "Centimeter",
    "Miles",
    "Inch",
    "Foot"
]

# List to choose which Unit to convert to
Unit_toList = [
    "Meter",
    "Kilometer",
    "Millimeter",
    "Centimeter",
    "Miles",
    "Inch",
    "Foot"
]

root = Tk()
root.geometry("400x400")
root.title("Unit Converter")
root.config(bg="#061f38")

# Define Variables
unit1 = StringVar()
result = StringVar()

unit_from = StringVar(root)
unit_from.set(Unit_fromList[0])

unit_to = StringVar(root)
unit_to.set(Unit_toList[0])


# funtions
def convert():
    unit1f = unit1.get()
    unit_fromf = str(unit_from.get())
    unit_tof = str(unit_to.get())

    if unit_fromf == "Meter":

        if unit_tof == "Kilometer":
            ans = float(unit1f) / 1000
        elif unit_tof == "Millimeter":
            ans = float(unit1f) * 1000
        elif unit_tof == "Centimeter":
            ans = float(unit1f) * 100
        elif unit_tof == "Miles":
            ans = float(unit1f) * 0.00062137
        elif unit_tof == "Inch":
            ans = float(unit1f) * 39.37
        elif unit_tof == "Foot":
            ans = float(unit1f) * 3.2808

    elif unit_fromf == "Kilometer":

        if unit_tof == "Meter":
            ans = float(unit1f) * 1000
        elif unit_tof == "Millimeter":
            ans = float(unit1f) * 1000000
        elif unit_tof == "Centimeter":
            ans = float(unit1f) * 100000
        elif unit_tof == "Miles":
            ans = float(unit1f) * 0.62137
        elif unit_tof == "Inch":
            ans = float(unit1f) * 39370.1
        elif unit_tof == "Foot":
            ans = float(unit1f) * 3280.84

    elif unit_fromf == "Millimeter":

        if unit_tof == "Meter":
            ans = float(unit1f) / 1000
        elif unit_tof == "Kilometer":
            ans = float(unit1f) / 1000000
        elif unit_tof == "Centimeter":
            ans = float(unit1f) / 10
        elif unit_tof == "Miles":
            ans = float(unit1f) * 0.00000062137
        elif unit_tof == "Inch":
            ans = float(unit1f) * 0.0393701
        elif unit_tof == "Foot":
            ans = float(unit1f) * 0.00328084

    elif unit_fromf == "Centimeter":

        if unit_tof == "Meter":
            ans = float(unit1f) / 100
        elif unit_tof == "Kilometer":
            ans = float(unit1f) / 100000
        elif unit_tof == "Millimeter":
            ans = float(unit1f) * 10
        elif unit_tof == "Miles":
            ans = float(unit1f) * 0.0000062137
        elif unit_tof == "Inch":
            ans = float(unit1f) * 0.393701
        elif unit_tof == "Foot":
            ans = float(unit1f) * 0.0328084

    elif unit_fromf == "Miles":

        if unit_tof == "Meter":
            ans = float(unit1f) * 1609.34
        elif unit_tof == "Kilometer":
            ans = float(unit1f) * 1.60934
        elif unit_tof == "Millimeter":
            ans = float(unit1f) * 1609344
        elif unit_tof == "Centimeter":
            ans = float(unit1f) * 160934.4
        elif unit_tof == "Inch":
            ans = float(unit1f) * 63360
        elif unit_tof == "Foot":
            ans = float(unit1f) * 5280

    elif unit_fromf == "Inch":

        if unit_tof == "Meter":
            ans = float(unit1f) * 0.0254
        elif unit_tof == "Kilometer":
            ans = float(unit1f) * 0.0000254
        elif unit_tof == "Millimeter":
            ans = float(unit1f) * 25.4
        elif unit_tof == "Centimeter":
            ans = float(unit1f) * 2.54
        elif unit_tof == "Miles":
            ans = float(unit1f) * 0.0000157828
        elif unit_tof == "Foot":
            ans = float(unit1f) * 0.0833333

    elif unit_fromf == "Foot":

        if unit_tof == "Meter":
            ans = float(unit1f) * 0.3048
        elif unit_tof == "Kilometer":
            ans = float(unit1f) * 0.0003048
        elif unit_tof == "Millimeter":
            ans = float(unit1f) * 304.8
        elif unit_tof == "Centimeter":
            ans = float(unit1f) * 30.48
        elif unit_tof == "Miles":
            ans = float(unit1f) * 0.000189394
        elif unit_tof == "Inch":
            ans = float(unit1f) * 12

    resultV.config(text=ans)


# GUI
title = Label(root, text="Unit Converter", fg='blue', bg="#061f38")
title.config(font=("Courier", 30))
title.place(x=30, y=10)

label_from = Label(root, text="Enter Value", font=("Arial", 11, "bold"), fg="white", bg="#061f38")
label_from.place(x=30, y=75)

label_unit_to = Label(root, text="Unit to convert from:", font=("Arial", 11, "bold"), fg="white", bg="#061f38")
label_unit_to.place(x=140, y=75)

unit1entry = Entry(root, textvariable=unit1, width=15, font=(18))
unit1entry.place(x=30, y=100)

from_unit = OptionMenu(root, unit_from, *Unit_fromList)
from_unit.place(x=210, y=100)

label_to = Label(root, text="Choose unit to covert to:", font=("Arial", 11, "bold"), fg="white", bg="#061f38")
label_to.place(x=30, y=178)

to_unit = OptionMenu(root, unit_to, *Unit_toList)
to_unit.place(x=30, y=200)

resultE = Label(root, text="Result:", font=("Arial", 15), fg='red', bg="#061f38")
resultE.place(x=30, y=232)

resultV = Label(root, text="", font=("Arial", 15, "bold"), fg="white", bg="#061f38")
resultV.place(x=30, y=265)

convert_btn = Button(root, text="Convert!", font=("Arial", 15, "bold"), fg="white", bg="red", command=convert)
convert_btn.place(x=30, y=300)

author = Label(root, text="made by @its_just_chloe "
                          "(Twitter)", font=("Arial", 8, "bold"), fg="yellow", bg="#061f38")
author.place(x=175, y=380)

root.mainloop()
