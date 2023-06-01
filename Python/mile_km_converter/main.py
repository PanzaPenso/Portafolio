from tkinter import *


def button_calculate():
    new_text = float(num_entry.get())
    result = round(new_text * 1.609)
    lb_result.config(text=f"{result}")


window = Tk()
window.title("Mile To Km Converter")
window.config(padx=20, pady=20)

lb_miles = Label(text="Miles")
lb_miles.config(font=("Arial", 24))
lb_miles.grid(column=3, row=1)

num_entry = Entry(width=10)
num_entry.config(font=("Arial", 24))
num_entry.grid(column=2, row=1)

lb_equals = Label(text="is equal to")
lb_equals.config(font=("Arial", 24))
lb_equals.grid(column=1, row=2)

lb_result = Label(text="0")
lb_result.config(font=("Arial", 24))
lb_result.grid(column=2, row=2)

lb_km = Label(text="Km")
lb_km.config(font=("Arial", 24))
lb_km.grid(column=3, row=2)

bt_calculate = Button(text="Calculate", command=button_calculate)
bt_calculate.config(font=("Arial", 24))
bt_calculate.grid(column=2, row=3)

window.mainloop()
