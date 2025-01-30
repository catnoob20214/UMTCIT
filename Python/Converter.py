import tkinter as tk
from tkinter import messagebox
import math

#main window
windows = tk.Tk()
windows.geometry("400x700")
windows.title("Converter")

# Frame
main_frame = tk.Frame(windows)
main_frame.pack(fill="both", expand=True)
watermark_label = tk.Label(main_frame, text="Lagunday", font=("Arial", 12, "italic"), fg="gray", anchor="se")
watermark_label.place(relx=1.0, rely=1.0, anchor="se") 

# Page 1
page1 = tk.Frame(main_frame)
page1watermark=tk.Label(watermark_label)

page1lbl1 = tk.Label(page1, text="Welcome to the Converter!", font=("Bold", 20))
page1lbl1.pack()

# Page 2 (Geometry Converter)
page2 = tk.Frame(main_frame)

page2lbl1 = tk.Label(page2, text="Geometry Converter", font=("Bold", 20))
page2lbl1.pack(pady=10)

# Dynamic inputs and results
def clear_inputs():
    for widget in input_frame.winfo_children():
        widget.destroy()
    result_label.config(text="")

def calculate_circle():
    try:
        radius = float(radius_entry.get())
        area = math.pi * radius ** 2
        circumference = 2 * math.pi * radius
        diameter = 2 * radius
        result_label.config(text=f"Circle:\nArea: {area:.2f}\nCircumference: {circumference:.2f}\nDiameter: {diameter:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def calculate_triangle():
    try:
        base = float(base_entry.get())
        height = float(height_entry.get())
        side1 = float(side1_entry.get())
        side2 = float(side2_entry.get())
        area = 0.5 * base * height
        perimeter = base + side1 + side2
        result_label.config(text=f"Triangle:\nArea: {area:.2f}\nPerimeter: {perimeter:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def calculate_rectangle():
    try:
        length = float(length_entry.get())
        width = float(width_entry.get())
        area = length * width
        perimeter = 2 * (length + width)
        diagonal = math.sqrt(length ** 2 + width ** 2)
        result_label.config(text=f"Rectangle:\nArea: {area:.2f}\nPerimeter: {perimeter:.2f}\nDiagonal: {diagonal:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def calculate_square():
    try:
        side = float(side_entry.get())
        area = side ** 2
        perimeter = 4 * side
        diagonal = math.sqrt(2) * side
        result_label.config(text=f"Square:\nArea: {area:.2f}\nPerimeter: {perimeter:.2f}\nDiagonal: {diagonal:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Geometry Options
def show_circle():
    clear_inputs()
    global radius_entry
    tk.Label(input_frame, text="Radius:").pack()
    radius_entry = tk.Entry(input_frame)
    radius_entry.pack()
    tk.Button(input_frame, text="Calculate Circle", command=calculate_circle).pack()

def show_triangle():
    clear_inputs()
    global base_entry, height_entry, side1_entry, side2_entry
    tk.Label(input_frame, text="Base:").pack()
    base_entry = tk.Entry(input_frame)
    base_entry.pack()
    tk.Label(input_frame, text="Height:").pack()
    height_entry = tk.Entry(input_frame)
    height_entry.pack()
    tk.Label(input_frame, text="Side 1:").pack()
    side1_entry = tk.Entry(input_frame)
    side1_entry.pack()
    tk.Label(input_frame, text="Side 2:").pack()
    side2_entry = tk.Entry(input_frame)
    side2_entry.pack()
    tk.Button(input_frame, text="Calculate Triangle", command=calculate_triangle).pack()

def show_rectangle():
    clear_inputs()
    global length_entry, width_entry
    tk.Label(input_frame, text="Length:").pack()
    length_entry = tk.Entry(input_frame)
    length_entry.pack()
    tk.Label(input_frame, text="Width:").pack()
    width_entry = tk.Entry(input_frame)
    width_entry.pack()
    tk.Button(input_frame, text="Calculate Rectangle", command=calculate_rectangle).pack()

def show_square():
    clear_inputs()
    global side_entry
    tk.Label(input_frame, text="Side:").pack()
    side_entry = tk.Entry(input_frame)
    side_entry.pack()
    tk.Button(input_frame, text="Calculate Square", command=calculate_square).pack()

# Buttons to select geometry type
geometry_buttons = tk.Frame(page2)
geometry_buttons.pack(pady=10)

tk.Button(geometry_buttons, text="Circle", command=show_circle).pack(side=tk.LEFT, padx=5)
tk.Button(geometry_buttons, text="Triangle", command=show_triangle).pack(side=tk.LEFT, padx=5)
tk.Button(geometry_buttons, text="Rectangle", command=show_rectangle).pack(side=tk.LEFT, padx=5)
tk.Button(geometry_buttons, text="Square", command=show_square).pack(side=tk.LEFT, padx=5)

# Input and Result Section
input_frame = tk.Frame(page2)
input_frame.pack(pady=10)

result_label = tk.Label(page2, text="", font=("Arial", 12), justify=tk.LEFT)
result_label.pack(pady=10)

# Page 3 (Money Converter)
page3 = tk.Frame(main_frame)

page3lbl1 = tk.Label(page3, text="Money Converter", font=("Bold", 20))
page3lbl1.pack(pady=10)

# Currency conversion functionality
currencies = {
    "USD": 1.0,
    "EUR": 0.9,
    "GBP": 0.8,
    "INR": 82.0,
    "AUD": 1.5,
    "CAD": 1.35,
    "JPY": 140.0,
    "CNY": 7.3,
    "CHF": 0.92,
    "SGD": 1.4
}

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()
        if from_currency == to_currency:
            result_label_money.config(text=f"Converted Amount: {amount:.2f} {to_currency}")
        else:
            converted_amount = amount * (currencies[to_currency] / currencies[from_currency])
            result_label_money.config(text=f"Converted Amount: {converted_amount:.2f} {to_currency}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")

# Input fields for the Money Converter
amount_label = tk.Label(page3, text="Amount:")
amount_label.pack()
amount_entry = tk.Entry(page3)
amount_entry.pack()

from_currency_var = tk.StringVar(value="USD")
to_currency_var = tk.StringVar(value="EUR")

from_currency_label = tk.Label(page3, text="From:")
from_currency_label.pack()
from_currency_menu = tk.OptionMenu(page3, from_currency_var, *currencies.keys())
from_currency_menu.pack()

to_currency_label = tk.Label(page3, text="To:")
to_currency_label.pack()
to_currency_menu = tk.OptionMenu(page3, to_currency_var, *currencies.keys())
to_currency_menu.pack()

convert_button = tk.Button(page3, text="Convert", command=convert_currency)
convert_button.pack(pady=10)

result_label_money = tk.Label(page3, text="", font=("Arial", 12), justify=tk.LEFT)
result_label_money.pack(pady=10)


page4 = tk.Frame(main_frame)

page4lbl1 = tk.Label(page4, text="Unit Converter", font=("Bold", 20))
page4lbl1.pack(pady=10)

# Unit conversion functionality
def convert_units():
    try:
        value = float(unit_value_entry.get())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()

        # Length conversion (meters to other units)
        conversions = {
            "meters": {"meters": 1, "kilometers": 0.001, "feet": 3.28084, "inches": 39.3701},
            "kilometers": {"meters": 1000, "kilometers": 1, "feet": 3280.84, "inches": 39370.1},
            "feet": {"meters": 0.3048, "kilometers": 0.0003048, "feet": 1, "inches": 12},
            "inches": {"meters": 0.0254, "kilometers": 0.0000254, "feet": 0.0833333, "inches": 1},
            "celsius": {"celsius": lambda x: x, "fahrenheit": lambda x: x * 9/5 + 32, "kelvin": lambda x: x + 273.15},
            "fahrenheit": {"celsius": lambda x: (x - 32) * 5/9, "fahrenheit": lambda x: x, "kelvin": lambda x: (x - 32) * 5/9 + 273.15},
            "kelvin": {"celsius": lambda x: x - 273.15, "fahrenheit": lambda x: (x - 273.15) * 9/5 + 32, "kelvin": lambda x: x}
        }

        if from_unit in conversions and to_unit in conversions[from_unit]:
            if callable(conversions[from_unit][to_unit]):
                result = conversions[from_unit][to_unit](value)
            else:
                result = value * conversions[from_unit][to_unit]
            result_label_unit.config(text=f"Converted Value: {result:.2f} {to_unit}")
        else:
            messagebox.showerror("Error", "Invalid conversion units.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Unit selection and input
unit_value_label = tk.Label(page4, text="Enter Value:")
unit_value_label.pack()
unit_value_entry = tk.Entry(page4)
unit_value_entry.pack()

from_unit_var = tk.StringVar(value="meters")
to_unit_var = tk.StringVar(value="kilometers")

from_unit_label = tk.Label(page4, text="From Unit:")
from_unit_label.pack()
from_unit_menu = tk.OptionMenu(page4, from_unit_var, "meters", "kilometers", "feet", "inches", "celsius", "fahrenheit", "kelvin")
from_unit_menu.pack()

to_unit_label = tk.Label(page4, text="To Unit:")
to_unit_label.pack()
to_unit_menu = tk.OptionMenu(page4, to_unit_var, "meters", "kilometers", "feet", "inches", "celsius", "fahrenheit", "kelvin")
to_unit_menu.pack()

convert_unit_button = tk.Button(page4, text="Convert", command=convert_units)
convert_unit_button.pack(pady=10)

result_label_unit = tk.Label(page4, text="", font=("Arial", 12), justify=tk.LEFT)
result_label_unit.pack(pady=10)

# Show the first page initially
page1.pack(pady=100)

pages = [page1, page2, page3, page4]
labels = [
    "Click Next to proceed to Geometry Converter -->>",
    "Click Next to proceed to Money Converter -->>",
    "Click Next to proceed to Unit Converter -->>",
    "Back to Money Converter <<--"
]
count = 0

count = 0

def update_bottom_label():
    bottomlabel.config(text=labels[count])

def move_next_page():
    global count
    if not count > len(pages) - 2:
        count += 1
        for p in pages:
            p.pack_forget()
        page = pages[count]
        page.pack(pady=100)
        update_bottom_label()

def move_previous_page():
    global count
    if count > 0:
        count -= 1
        for p in pages:
            p.pack_forget()
        page = pages[count]
        page.pack(pady=100)
        update_bottom_label()

def add_watermark(page, text="Lagunday"):
    
    watermark_label = tk.Label(page, text=text, font=("Arial", 12, "italic"), fg="gray")
    watermark_label.pack(anchor="ne", padx=10, pady=5)  # Positions at the top-right

# Buttons
bottomframe = tk.Frame(windows)
bottomframe.pack(side=tk.BOTTOM, pady=10)

bottomlabel = tk.Label(bottomframe, text=labels[count])
bottomlabel.pack(pady=20)

nextbtn = tk.Button(bottomframe, text="Next", width=8, command=move_next_page)
nextbtn.pack(side=tk.RIGHT, padx=40)

backbtn = tk.Button(bottomframe, text="Back", width=8, command=move_previous_page)
backbtn.pack(side=tk.LEFT, padx=40)

windows.mainloop()