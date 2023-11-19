from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=25, pady=25)


# Entry
input = Entry(width=10)
input.grid(column=1, row=0)

# Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_to = Label(text="is equal to")
equal_to.grid(column=0, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)


# Button

def conversion():
    sum = input.get()
    result.config(text=(float(sum) * 1.609))


calculate = Button(text="Calculate", command=conversion)
calculate.grid(column=1, row=2)







window.mainloop()