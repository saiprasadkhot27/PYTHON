import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror("Login", "Invalid Username or Password")


window = tk.Tk()

window.title("Login System")
window.geometry("400x300")

tk.Label(window, text="Username").pack(pady=10)

username_entry = tk.Entry(window)
username_entry.pack()

tk.Label(window, text="Password").pack(pady=10)

password_entry = tk.Entry(window, show="*")
password_entry.pack()

tk.Button(
    window,
    text="Login",
    command=login
).pack(pady=20)

window.mainloop()