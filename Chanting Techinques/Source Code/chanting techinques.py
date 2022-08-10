from tkinter import filedialog
from tkinter import *

import dhandapatha
import dwajapatha
import ghanapatha
import jathapatha
import kramapatha
import malapatha
import rathapatha
import Rekhapatha
import sikhapatha

window = Tk()
window.geometry('600x500')

pa = StringVar()
var = StringVar()
out = StringVar()

a: str = '1'


def printf(x):
    for a in x:
        l = ' '.join(a)
        intext.insert(INSERT, str(l))
        intext.insert(INSERT, '\n')


def call(line, type):
    if (type == "Ghanapatha"):
        a = ghanapatha.ghanapatha(line)
        printf(a)
    elif (type == "Jathapatha"):
        a = jathapatha.jathapatha(line)
        printf(a)
    elif (type == "Rekhapatha"):
        a = Rekhapatha.rekhapatha(line)
        printf(a)
    elif (type == "Kramapatha"):
        a = kramapatha.kramapatha(line)
        printf(a)
    elif (type == "Malapatha"):
        a = malapatha.malapatha(line)
        printf(a)
    elif (type == "Sikhapatha"):
        a = sikhapatha.sikhapatha(line)
        printf(a)
    elif (type == "Dwajapatha"):
        a = dwajapatha.dwajapatha(line)
        printf(a)
    elif (type == "Rathapatha"):
        a = rathapatha.rathapatha(line)
        printf(a)
    elif (type == "Dhandapatha"):
        a = dhandapatha.dhandapatha(line)
        printf(a)


def path():
    window.filename = filedialog.askopenfilename(initialdir="/", title="Select file",

                                                 filetypes=(("txt files", "*.txt"), ("all files", "*.*")))

    a = window.filename
    entry1.insert(10, a)


def textfile():
    txtpath = pa.get()
    filetxt = open(txtpath, 'r', encoding="utf8")
    tychant = var.get()
    for line in filetxt:
        call(line, tychant)


window.title("chanting techniques in sanskrit slokas")

label1 = Label(window, text="select the text file :", width=15, font=("arial", 10, "bold"))
label1.place(x=10, y=14)

entry1 = Entry(window, textvariable=pa, width=50)
entry1.place(x=150, y=14)

button1 = Button(window, text="Browser", width=10, font=("arial", 10, "bold"), bg="red", fg="white", command=path)
button1.place(x=470, y=10)

button2 = Button(window, text="Output", width=10, font=("arial", 10, "bold"), bg="red", fg="white", command=textfile)
button2.place(x=470, y=120)

list1 = ["Ghanapatha", "Jathapatha", "Rekhapatha", "Kramapatha", "Malapatha", "Sikhapatha", "Dwajapatha", "Rathapatha",
         "Dhandapatha"]
droplist = OptionMenu(window, var, *list1)
var.set("Select chanting type")
droplist.config(width=20, font=("arial", 10, "bold"))

droplist.place(x=10, y=40)

scroll = Scrollbar(window)
intext = Text(window, height=10, width=70, yscrollcommand=scroll.set)
intext.place(x=10, y=180)

window.mainloop()