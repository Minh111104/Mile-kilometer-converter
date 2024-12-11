from tkinter import *


def calculate_clicked():
    miles = float(input.get())
    km = miles * 1.689
    result_label.config(text=f"{km}")


# Create window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=300)
window.config(padx=100, pady=100)

# Input widget
input = Entry(width=10)
input.grid(column=1, row=0)

# Miles widget
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# is_equal_to widget
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

# result widget
result_label = Label(text="0")
result_label.grid(column=1, row=1)

# Km widget
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Calculate widget
calculate_button = Button(text="Calculate", command=calculate_clicked)
calculate_button.grid(column=1, row=2)


window.mainloop()
