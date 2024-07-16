import tkinter as tk
from tkinter import messagebox
from password_generator import generate_password

#this function will generate the password and show it in the entry widget
#it will get the length and the choice of the user and call the generate_password function with these values
#then it will insert the generated password in the entry widget
def generate_password_gui():
    length = int(entry_length.get())
    choice = int(var_choice.get())
    password = generate_password(length, choice)
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

#creating the main window of the application and setting its title
root = tk.Tk()
root.title("Password Generator")

#creating the widgets that will be used in the application
label_length = tk.Label(root, text="Password Length:")
label_length.pack(pady=5)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)
entry_length.insert(0, "")

#creating the radio buttons that will be used to choose the type of characters that will be used in the password
#the choices are: only letters, only numbers, letters and numbers, letters, numbers and special characters
var_choice = tk.StringVar()
choices = [
    ("Letters", 1),
    ("Numbers", 2),
    ("Letters e numbers", 3),
    ("Letters, numbers and special characters", 4)
]
#creating the radio buttons with the choices that were defined before
#the variable that will be used to store the choice of the user is var_choice
for text, value in choices:
    tk.Radiobutton(root, text=text, variable=var_choice, value=value).pack(pady=5)

#creating the button that will call the generate_password_gui function
#this button will generate the password and show it in the entry widget
button_generate = tk.Button(root, text="Generate password", command=generate_password_gui)
button_generate.pack(pady=20)

#creating the entry widget that will show the generated password
#this widget will be used to copy the password to the clipboard
entry_password = tk.Entry(root, width=10)
entry_password.pack(pady=5)

#this function will copy the password to the clipboard
root.mainloop()
