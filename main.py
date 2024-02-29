import tkinter as tk

window = tk.Tk()
window.title("A fekete ingesek Pizzéria")
window.geometry("1920x1080")

frame = tk.Label(window, text="Hello World")
frame.pack(fill=tk.X, expand=tk.Y)

window.mainloop()