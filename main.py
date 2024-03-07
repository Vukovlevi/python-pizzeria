import tkinter as tk
from tkinter import messagebox
from data import pizzak

def confirm_quit():
    sure = messagebox.askyesno("Megerősítés", "Biztosan ki akar lépni?")
    if sure:
        window.quit()

def about():
    messagebox.showinfo("Készítők", "Simon Zsombor\nSzabó-Vukov Levente")

window = tk.Tk()
window.title("A fekete ingesek Pizzéria")
window.geometry("1920x1080")

pizzaPhotos = []
for i in range(0,len(pizzak)):
    pizzaFrame=tk.Frame(window,borderwidth=2,relief="raised",padx=20)
    pizzaPhoto = tk.PhotoImage(file=pizzak[i].img)
    pizzaPhotos.append(pizzaPhoto)
    pizzaPhotoPlace=tk.Label(pizzaFrame,image=pizzaPhotos[i])
    pizzaPhotoPlace.pack()
    pizzaName=tk.Label(pizzaFrame,text=pizzak[i].name,pady=5)
    pizzaName.pack()
    pizzaComp=tk.Label(pizzaFrame,text=pizzak[i].components,pady=5)
    pizzaComp.pack()
    pizzaRecipe=tk.Label(pizzaFrame,text=pizzak[i].recipe,pady=5)
    pizzaRecipe.pack()
    pizzaOrder=tk.Button(pizzaFrame,text="Rendelés",pady=5)
    pizzaOrder.pack()
    pizzaFrame.grid(row=0,column=i,padx=100,pady=50)

order_menu = tk.Menu()
order_menu.add_command(label="Rendelés hozzáadása")
order_menu.add_command(label="Összes rendelés")

general_menu = tk.Menu()
general_menu.add_command(label="Névjegy", command=about)
general_menu.add_command(label="Kilépés", command=confirm_quit)

menu = tk.Menu(window)
menu.add_cascade(label="Rendelés", menu=order_menu)
menu.add_cascade(label="Általános", menu=general_menu)
menu.add_command(label="Kijelentkezés")

window.config(menu=menu)
window.mainloop()