import tkinter as tk

def order_window(window, order):
    window.title("Rendelés hozzáadása")
    window.geometry("400x400")

    frame = tk.Frame(window)
    pizzaPhoto=tk.PhotoImage(file=order.pizza.img,width=200,height=100)
    pizzaPhotoPlace=tk.Label(frame,image=pizzaPhoto)
    pizzaPhotoPlace.pack()
    pizzaName=tk.Label(frame,text=order.pizza.name,pady=5)
    pizzaName.pack()
    pizzaComp=tk.Label(frame,text=order.pizza.components,pady=5)
    pizzaComp.pack()
    pizzaRecipe=tk.Label(frame,text=order.pizza.recipe,pady=5)
    pizzaRecipe.pack()
    pizzaOrder=tk.Label(frame,text=f"Rendelés - {order.pizza.price}Ft / db", pady=5)
    pizzaOrder.pack()
    count_label = tk.Label(frame, text="Pizzák száma:")
    count_label.pack(side=tk.LEFT)
    count = tk.Entry(frame)
    count.pack(side=tk.RIGHT)
    frame.pack()