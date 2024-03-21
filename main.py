import tkinter as tk
from tkinter import messagebox
from type import Order
from data import pizzak
from data import user as user_data
from add_order import order_window
from show_order import show_order_window
def log_out():
    holder.pack_forget()
    canvas_widget.pack()
def log_in():
    if(user_data.username==userEntry.get() and user_data.password==passEntry.get()):
        userEntry.delete(0,tk.END)
        passEntry.delete(0,tk.END)
        canvas_widget.pack_forget()
        holder.pack()
    else:
        messagebox.showwarning("Hiba","Hibás felhasználó vagy jelszó!")

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

canvas_widget=tk.Canvas(window,width=500,height=300,bg="#8C7473")
userLabel=tk.Label(canvas_widget,text="Felhasználónév:",bg="#8C7473",font="ariel 18")
canvas_widget.create_window(100,50,window=userLabel)
userEntry=tk.Entry(canvas_widget,width=35)
canvas_widget.create_window(300,50,window=userEntry)
passLabel=tk.Label(canvas_widget,text="Jelszó:",bg="#8C7473",font="ariel 18")
canvas_widget.create_window(100,150,window=passLabel,width=100)
passEntry=tk.Entry(canvas_widget,width=35)
canvas_widget.create_window(300,150,window=passEntry)    
logButton=tk.Button(canvas_widget,text="Bejelentkezés",command=log_in)
canvas_widget.create_window(250,230,window=logButton)
canvas_widget.pack()

user = user_data
holder=tk.Frame(window,bg="grey")
pizzaPhotos=[]
for i, pizza in enumerate(pizzak):
    pizzaFrame=tk.Frame(holder,borderwidth=2,relief="raised",padx=20,bg="#8C7473")
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
menu.add_command(label="Kijelentkezés",command=log_out)

window.config(menu=menu,bg="grey")
window.mainloop()