import tkinter as tk
from data import pizzak

window = tk.Tk()
window.title("A fekete ingesek Pizzéria")
window.geometry("1920x1080")

for i in range(0,len(pizzak)):
    pizzaFrame=tk.Frame(window,borderwidth=2,relief="raised",padx=20)
    pizzaPhoto=tk.PhotoImage(file="./Img/placeholder.png",width=200,height=100)
    pizzaPhotoPlace=tk.Label(pizzaFrame,image=pizzaPhoto)
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

window.mainloop()