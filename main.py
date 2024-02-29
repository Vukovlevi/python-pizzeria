import tkinter as tk
from type import Pizza

pizza1 = Pizza("Margaréta", "paradicsom szósz, sajt, oregano", "Meg kell csinálni az összetevők segítségével!", "paradicsomszósz,mozarella,sonka,kukorica", 2390)
pizza2 = Pizza("Kukoricás", "paradicsom szósz, kukorica, sajt, oregano", "Meg kell csinálni az összetevők segítségével!", "paradicsomszósz,mozarella,sonka,kukorica", 2390)
pizza3 = Pizza("Sonkás", "paradicsom szósz, sonka, sajt, oregano", "Meg kell csinálni az összetevők segítségével!", "paradicsomszósz,mozarella,sonka,kukorica", 2390)
pizza4 = Pizza("Bolognai", "bolognai szósz, paradicsom szósz, sajt, oregano", "Meg kell csinálni az összetevők segítségével!", "paradicsomszósz,mozarella,sonka,kukorica", 2390)
pizzak = [pizza1, pizza2, pizza3, pizza4]

window = tk.Tk()
window.title("A fekete ingesek Pizzéria")
window.geometry("1920x1080")

label = tk.Label(window, text="Hello World")
label.pack(fill=tk.X, expand=tk.Y)

window.mainloop()