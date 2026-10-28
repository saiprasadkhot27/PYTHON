import tkinter as tk
from tkinter import ttk, messagebox
import os


# Create main window
root = tk.Tk()
root.title("Student Data Management System")
root.geometry("800x600")


#  SAVE DATA 
def save_data():

    
    name_value = name_entry.get().strip()
    roll_value = roll_entry.get().strip()
    division_value = division_entry.get().strip()
    subject_value = subject_entry.get().strip()

   
    if name_value == "" or roll_value == "" or division_value == "" or subject_value == "":
        messagebox.showwarning(
            "Warning",
            "Please enter all student information."
        )
        return

    # Save data into text file
    with open("student_data.txt", "a") as file:

        file.write(
            name_value + " | " +
            roll_value + " | " +
            division_value + " | " +
            subject_value + "\n"
        )

    # Show success message
    messagebox.showinfo(
        "Success",
        "Student data saved successfully!"
    )

    # Clear input fields
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    division_entry.delete(0, tk.END)
    subject_entry.delete(0, tk.END)


# ---------------- READ DATA ----------------
def read_data():

    # Delete existing rows from table
    for row in table.get_children():
        table.delete(row)

    # Check whether file exists
    if not os.path.exists("student_data.txt"):
        messagebox.showinfo(
            "Information",
            "No student data found."
        )
        return

    # Read data from text file
    with open("student_data.txt", "r") as file:

        for line in file:

            line = line.strip()

            # Skip empty lines
            if line == "":
                continue

            # Split data using |
            data = line.split("|")

            # Make sure data has 4 values
            if len(data) == 4:

                table.insert(
                    "",
                    tk.END,
                    values=(
                        data[0],
                        data[1],
                        data[2],
                        data[3]
                    )
                )


#  CLEAR TABLE 
def clear_table():

    for row in table.get_children():
        table.delete(row)


#HEADING 

heading = tk.Label(
    root,
    text="Student Data Management System",
    font=("Arial", 20, "bold")
)

heading.pack(pady=20)


# INPUT FRAME 

input_frame = tk.Frame(root)
input_frame.pack(pady=10)


# Name
tk.Label(
    input_frame,
    text="Name:",
    font=("Arial", 12)
).grid(
    row=0,
    column=0,
    padx=10,
    pady=8,
    sticky="e"
)

name_entry = tk.Entry(
    input_frame,
    width=35,
    font=("Arial", 12)
)

name_entry.grid(
    row=0,
    column=1,
    padx=10,
    pady=8
)


# Roll No
tk.Label(
    input_frame,
    text="Roll No:",
    font=("Arial", 12)
).grid(
    row=1,
    column=0,
    padx=10,
    pady=8,
    sticky="e"
)

roll_entry = tk.Entry(
    input_frame,
    width=35,
    font=("Arial", 12)
)

roll_entry.grid(
    row=1,
    column=1,
    padx=10,
    pady=8
)


# Division
tk.Label(
    input_frame,
    text="Division:",
    font=("Arial", 12)
).grid(
    row=2,
    column=0,
    padx=10,
    pady=8,
    sticky="e"
)

division_entry = tk.Entry(
    input_frame,
    width=35,
    font=("Arial", 12)
)

division_entry.grid(
    row=2,
    column=1,
    padx=10,
    pady=8
)


# Subject
tk.Label(
    input_frame,
    text="Subject:",
    font=("Arial", 12)
).grid(
    row=3,
    column=0,
    padx=10,
    pady=8,
    sticky="e"
)

subject_entry = tk.Entry(
    input_frame,
    width=35,
    font=("Arial", 12)
)

subject_entry.grid(
    row=3,
    column=1,
    padx=10,
    pady=8
)


#  BUTTON FRAME 

button_frame = tk.Frame(root)
button_frame.pack(pady=15)


# Submit button
submit_button = tk.Button(
    button_frame,
    text="Submit",
    command=save_data,
    width=15,
    font=("Arial", 11, "bold")
)

submit_button.grid(
    row=0,
    column=0,
    padx=5
)


# Read button
read_button = tk.Button(
    button_frame,
    text="Read Data",
    command=read_data,
    width=15,
    font=("Arial", 11, "bold")
)

read_button.grid(
    row=0,
    column=1,
    padx=5
)


# # Clear button
# clear_button = tk.Button(
#     button_frame,
#     text="Clear Table",
#     command=clear_table,
#     width=15,
#     font=("Arial", 11, "bold")
# )

# clear_button.grid(
#     row=0,
#     column=2,
#     padx=5
# )


 

table_frame = tk.Frame(root)
table_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)


table = ttk.Treeview(
    table_frame,
    columns=(
        "Name",
        "Roll No",
        "Division",
        "Subject"
    ),
    show="headings"
)


# Table headings
table.heading(
    "Name",
    text="Name"
)

table.heading(
    "Roll No",
    text="Roll No"
)

table.heading(
    "Division",
    text="Division"
)

table.heading(
    "Subject",
    text="Subject"
)


# Column width
table.column(
    "Name",
    width=180,
    anchor="center"
)

table.column(
    "Roll No",
    width=100,
    anchor="center"
)

table.column(
    "Division",
    width=100,
    anchor="center"
)

table.column(
    "Subject",
    width=180,
    anchor="center"
)


# Display table
table.pack(
    fill="both",
    expand=True
)


# ---------------- START APPLICATION ----------------

root.mainloop()