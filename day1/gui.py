import tkinter as tk

def greet():
    name = entry.get()
    greeting = f"Hello, {name}!"
    label.config(text=greeting)

root = tk.Tk()
root.title("Greeting App")

label = tk.Label(root, text="Enter your name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Greet", command=greet)
button.pack()

root.mainloop()
