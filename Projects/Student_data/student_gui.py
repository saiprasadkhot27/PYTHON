import tkinter as tk
from tkinter import ttk
import json
import os

root = tk.Tk()
root.title("Student Data")
root.geometry("650x500")


# Save data
def save_data():
    data = {
        "Name": name.get(),
        "Roll No": roll.get(),
        "Division": division.get(),
        "Subject": subject.get()
    }

    if os.path.exists("student_data.json"):
        with open("student_data.json", "r") as file:
            students = json.load(file)
    else:
        students = []

    students.append(data)

    with open("student_data.json", "w") as file:
        json.dump(students, file, indent=4)

    table.insert(
        "",
        "end",
        values=(
            data["Name"],
            data["Roll No"],
            data["Division"],
            data["Subject"]
        )
    )

    name.delete(0, tk.END)
    roll.delete(0, tk.END)
    division.delete(0, tk.END)
    subject.delete(0, tk.END)


# Heading styling
tk.Label(
    root,
    text="Student Information",
    font=("Arial", 18, "bold")
).grid(row=0, column=0, columnspan=2, pady=20)



tk.Label(root, text="Name").grid(row=1, column=0, padx=20, pady=8, sticky="e")
name = tk.Entry(root, width=30)
name.grid(row=1, column=1, pady=8)

tk.Label(root, text="Roll No").grid(row=2, column=0, padx=20, pady=8, sticky="e")
roll = tk.Entry(root, width=30)
roll.grid(row=2, column=1, pady=8)

tk.Label(root, text="Division").grid(row=3, column=0, padx=20, pady=8, sticky="e")
division = tk.Entry(root, width=30)
division.grid(row=3, column=1, pady=8)

tk.Label(root, text="Subject").grid(row=4, column=0, padx=20, pady=8, sticky="e")
subject = tk.Entry(root, width=30)
subject.grid(row=4, column=1, pady=8)


# Submit button code
tk.Button(
    root,
    text="Submit",
    command=save_data,
    width=12
).grid(row=5, column=0, columnspan=2, pady=15)


# Table
table = ttk.Treeview(
    root,
    columns=("Name", "Roll No", "Division", "Subject"),
    show="headings"
)

table.heading("Name", text="Name")
table.heading("Roll No", text="Roll No")
table.heading("Division", text="Division")
table.heading("Subject", text="Subject")

table.column("Name", width=130)
table.column("Roll No", width=100)
table.column("Division", width=100)
table.column("Subject", width=150)

table.grid(row=6, column=0, columnspan=2, padx=20, pady=10)



if os.path.exists("student_data.json"):
    with open("student_data.json", "r") as file:
        students = json.load(file)

    for data in students:
        table.insert(
            "",
            "end",
            values=(
                data["Name"],
                data["Roll No"],
                data["Division"],
                data["Subject"]
            )
        )


root.mainloop()