import tkinter as tk
from tkinter import messagebox
from type import Order
from data import pizzak
from data import user as user_data
from add_order import order_window
from show_order import show_order_window


def confirm_quit():
    sure = messagebox.askyesno("Megerősítés", "Biztosan ki akar lépni?")
    if sure:
        window.quit()

def about():
    messagebox.showinfo("Készítők", "Simon Zsombor\nSzabó-Vukov Levente")

def add_order(pizza, photo):
    order = Order(pizza, user_data, 1)
    order_window(tk.Toplevel(), order, photo)
def show_order():
    show_order_window(tk.Toplevel(),pizzaPhotos)

window = tk.Tk()
window.title("A fekete ingesek Pizzéria")
window.geometry("1920x1080")

user = user_data

pizzaPhotos=[]
for i, pizza in enumerate(pizzak):
    pizzaFrame=tk.Frame(window,borderwidth=2,relief="raised",padx=20,bg="#8C7473")
    pizzaPhoto=tk.PhotoImage(file=pizza.img,width=200,height=100)
    pizzaPhotos.append(pizzaPhoto)
    pizzaPhotoPlace=tk.Label(pizzaFrame,image=pizzaPhoto,bg="#8C7473")
    pizzaPhotoPlace.pack()
    pizzaName=tk.Label(pizzaFrame,text=pizza.name,pady=5,bg="#8C7473",font="bold")
    pizzaName.pack()
    pizzaComp=tk.Label(pizzaFrame,text=pizza.components,pady=5,bg="#8C7473")
    pizzaComp.pack()
    pizzaRecipe=tk.Label(pizzaFrame,text=pizza.recipe,pady=5,bg="#8C7473")
    pizzaRecipe.pack()
    pizzaOrder=tk.Button(pizzaFrame,text=f"Rendelés - {pizza.price}Ft", pady=5, command=lambda p=pizza, i=i: add_order(p, pizzaPhotos[i]), relief="groove")
    pizzaOrder.pack()
    pizzaFrame.grid(row=0,column=i,padx=100,pady=50)

general_menu = tk.Menu()
general_menu.add_command(label="Névjegy", command=about)
general_menu.add_command(label="Kilépés", command=confirm_quit)

menu = tk.Menu(window)
menu.add_command(label="Összes rendelés",command=show_order)
menu.add_cascade(label="Általános", menu=general_menu)
menu.add_command(label="Kijelentkezés")

window.config(menu=menu,bg="grey")
window.mainloop()