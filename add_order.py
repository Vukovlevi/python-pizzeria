import tkinter as tk
from tkinter import messagebox
from storage import orders

def add_order(order, countEntry, window):
    count = 0
    try:
        count = int(countEntry.get()) 
    except:
        messagebox.showwarning("Mennyiség hiba", "Kérem egész számot adjon meg a pizzák darabdszámának!")
        window.grab_set()
        return
    
    order.price = order.pizza.price * count
    orders.append(order)

    messagebox.showinfo("Siker", "Rendelés sikeresen hozzáadva!")
    window.destroy()

def order_window(window, order, photo):
    window.title("Rendelés hozzáadása")
    window.geometry("400x400")
    window.grab_set()

    frame = tk.Frame(window)

    pizzaPhotoPlace=tk.Label(frame,image=photo)
    pizzaPhotoPlace.pack()

    pizzaName=tk.Label(frame,text=order.pizza.name,pady=5)
    pizzaName.pack()

    pizzaComp=tk.Label(frame,text=order.pizza.components,pady=5)
    pizzaComp.pack()

    pizzaRecipe=tk.Label(frame,text=order.pizza.recipe,pady=5)
    pizzaRecipe.pack()

    pizzaOrder=tk.Label(frame,text=f"Rendelés - {order.pizza.price}Ft / db", pady=5)
    pizzaOrder.pack()

    entryFrame = tk.Frame(frame)

    count_label = tk.Label(entryFrame, text="Pizzák száma:")
    count_label.pack(side=tk.LEFT)

    countEntry = tk.Entry(entryFrame)
    countEntry.pack(side=tk.RIGHT)

    entryFrame.pack(pady=10)

    button = tk.Button(frame, text="Rendelés hozzáadása", command=lambda: add_order(order, countEntry, window))
    button.pack()

    frame.pack()