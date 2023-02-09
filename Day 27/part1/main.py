from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=210, height=110)
window.config(pady=20, padx=20)

my_label = Label(text="Miles")
my_label.grid(column=2, row=0)

my_label_equal = Label(text="is equal to")
my_label_equal.grid(column=0, row=1)

my_label_answer = Label(text="0")
my_label_answer.grid(column=1, row=1)

my_label_km = Label(text="km")
my_label_km.grid(column=2, row=1)

input = Entry(width=10)
input.grid(row=0, column=1)


def button_clicked():
    my_label_answer.config(text=float(input.get()) * 1.609)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
