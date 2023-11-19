from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# windows.config(padx=100, pady=200)

# Label

my_label = Label(text="New Text")
my_label.grid(column=0, row=0)


# Button

def button_clicked():
    my_label.config(text=input.get())


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)


# Entry
input = Entry(width=10)
input.grid(column=3, row=2)


# New Button
def new_button_clicked():
    my_label.config(text="New Button Clicked")


new_button = Button(text="Click Me", command=new_button_clicked)
new_button.grid(column=2, row=0)






window.mainloop()