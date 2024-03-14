import tkinter as tk
from tkinter import messagebox
from storage import orders

def add_topping(topping, toppings):
    if topping not in toppings:
        toppings.append(topping) 
    else:
        toppings.remove(topping)

def add_order(order, countEntry, window, toppings):
    count = 0
    try:
        count = int(countEntry.get()) 
    except:
        messagebox.showwarning("Mennyiség hiba", "Kérem egész számot adjon meg a pizzák darabdszámának!")
        window.grab_set()
        return
    
    if len(toppings) > 2:
        messagebox.showwarning("Feltét hiba", "Nem lehet egy pizzán 2-nél több feltét!") 
        window.grab_set()
        return

    order.toppings = toppings

    order.price = order.pizza.price * count
    orders.append(order)

    messagebox.showinfo("Siker", "Rendelés sikeresen hozzáadva!")
    window.destroy()

def order_window(window, order, photo):
    window.title("Rendelés hozzáadása")
    window.geometry("400x400")
    window.grab_set()
    window.config(bg="grey")
    
    frame = tk.Frame(window,bg="#8C7473",relief="raised",borderwidth=2)
    current_toppings = []

    pizzaPhotoPlace=tk.Label(frame,image=photo)
    pizzaPhotoPlace.pack()

    pizzaName=tk.Label(frame,text=order.pizza.name,pady=5,bg="#8C7473")
    pizzaName.pack()

    pizzaComp=tk.Label(frame,text=order.pizza.components,pady=5,bg="#8C7473")
    pizzaComp.pack()

    pizzaRecipe=tk.Label(frame,text=order.pizza.recipe,pady=5,bg="#8C7473")
    pizzaRecipe.pack()

    pizzaOrder=tk.Label(frame,text=f"Rendelés - {order.pizza.price}Ft / db", pady=5,bg="#8C7473")
    pizzaOrder.pack()

    toppingFrame = tk.Frame(frame,bg="#8C7473")
    for topping in order.pizza.toppings:
        int_var = tk.IntVar()
        checkbox = tk.Checkbutton(toppingFrame, text=topping, variable=int_var, onvalue=1, offvalue=0, command=lambda topping=topping, toppings=current_toppings: add_topping(topping, toppings),bg="#8C7473")
        checkbox.pack(side=tk.LEFT)

    toppingFrame.pack()

    entryFrame = tk.Frame(frame)

    count_label = tk.Label(entryFrame, text="Pizzák száma:",bg="#8C7473")
    count_label.pack(side=tk.LEFT)

    countEntry = tk.Entry(entryFrame)
    countEntry.pack(side=tk.RIGHT)

    entryFrame.pack(pady=10)

    button = tk.Button(frame, text="Rendelés hozzáadása", command=lambda: add_order(order, countEntry, window, current_toppings))
    button.pack()

    frame.pack()