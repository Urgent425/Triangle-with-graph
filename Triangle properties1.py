from tkinter import *

# Function to calculate area, hypotenuse, and plot the triangle
def solution():
    try:
        base = float(input_base.get())
        height = float(input_height.get())
        surface = round(0.5 * base * height, 2)
        hypotenuse = round((base**2 + height**2)**0.5, 2)

        # Update results
        area_result.config(text=f'{surface} m²')
        hyppo_result.config(text=f'{hypotenuse} m')

        # Plot triangle
        canvas.delete("all")  # Clear previous drawings
        scaling_factor = 200 / max(base, height)  # Scale to fit canvas
        x_base = base * scaling_factor
        y_height = height * scaling_factor

        # Draw the triangle
        canvas.create_line(50, 200, 50 + x_base, 200, fill="blue", width=2)  # Base
        canvas.create_line(50, 200, 50, 200 - y_height, fill="green", width=2)  # Height
        canvas.create_line(50 + x_base, 200, 50, 200 - y_height, fill="red", width=2)  # Hypotenuse
    except ValueError:
        area_result.config(text='Error')
        hyppo_result.config(text='Error')

# Create the main window
window = Tk()
window.title('Right Triangle Properties')
window.config(padx=20, pady=20, bg='sky blue')

# Widgets for base input
triangle_base = Label(text='Base:', bg='sky blue')
triangle_base.grid(column=0, row=0, padx=5, pady=5)
input_base = Entry(width=10)
input_base.grid(column=1, row=0, padx=5, pady=5)

# Widgets for height input
triangle_height = Label(text='Height:', bg='sky blue')
triangle_height.grid(column=2, row=0, padx=5, pady=5)
input_height = Entry(width=10)
input_height.grid(column=3, row=0, padx=5, pady=5)

# Results for area and hypotenuse
triangle_area = Label(text='Area:', bg='orange')
triangle_area.grid(column=0, row=1, padx=5, pady=5)
area_result = Label(text='0', bg='sky blue')
area_result.grid(column=1, row=1, padx=5, pady=5)

triangle_hyppo = Label(text='Hypotenuse:', bg='green')
triangle_hyppo.grid(column=2, row=1, padx=5, pady=5)
hyppo_result = Label(text='0', bg='sky blue')
hyppo_result.grid(column=3, row=1, padx=5, pady=5)

# Calculate button
calculate_button = Button(text='Calculate', bg='yellow', command=solution)
calculate_button.grid(column=1, row=2, columnspan=2, pady=10)

# Canvas for triangle plot
canvas = Canvas(window, width=300, height=220, bg='white')
canvas.grid(column=0, row=3, columnspan=4, pady=20)

window.mainloop()
