import tkinter as tk

def add_numbers():
    a = int(entry1.get())
    b = int(entry2.get())
    result.config(text="Result: " + str(a + b))


window = tk.Tk()

window.title("Addition")
window.geometry("400x300")

tk.Label(window, text="First Number").pack()

entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="Second Number").pack()

entry2 = tk.Entry(window)
entry2.pack()

tk.Button(
    window,
    text="Add",
    command=add_numbers
).pack(pady=20)

result = tk.Label(window, text="Result:")
result.pack()

window.mainloop()