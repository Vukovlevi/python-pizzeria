import tkinter as tk
from tkinter import messagebox

def confirm_quit():
    sure = messagebox.askyesno("Megerősítés", "Biztosan ki akar lépni?")
    if sure:
        window.quit()

def about():
    messagebox.showinfo("Készítők", "Simon Zsombor\nSzabó-Vukov Levente")

window = tk.Tk()
window.title("A fekete ingesek Pizzéria")
window.geometry("1920x1080")

pizzaFrame=tk.Frame(window,borderwidth=2,relief="raised",padx=20)
pizzaPhoto=tk.PhotoImage(file="./Img/placeholder.png",width=200,height=100)
pizzaPhotoPlace=tk.Label(pizzaFrame,image=pizzaPhoto)
pizzaPhotoPlace.pack()
pizzaName=tk.Label(pizzaFrame,text="Placeholder",pady=5)
pizzaName.pack()
pizzaComp=tk.Label(pizzaFrame,text="Placeholder",pady=5)
pizzaComp.pack()
pizzaRecipe=tk.Label(pizzaFrame,text="Placeholder",pady=5)
pizzaRecipe.pack()
pizzaOrder=tk.Button(pizzaFrame,text="Placeholder",pady=5)
pizzaOrder.pack()
pizzaFrame.grid(row=0,column=0,padx=100,pady=50)

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