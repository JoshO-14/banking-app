import tkinter as tk

# Create the main window
window = tk.Tk()
# Add title
window.title =('Banking App')


# Create a label widget
label = tk.Label(window, text="Welcome to Joshua's Bank!")


# Add the label to the window
label.grid()


userName = tk.Entry(window, text="Enter Your User ID")
# Define an event handler for the button
def button_click():
   print("Button clicked!")


# Create a button widget
button = tk.Button(window, text="Click me!", command=button_click)


# Add the button to the window
button.grid()




# Start the main event loop
window.mainloop()