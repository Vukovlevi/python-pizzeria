from storage import orders
import tkinter as tk


def show_order_window(window,photo):
    window.title("Rendelések")
    window.geometry("400x700")
    for i,rendelese in enumerate(orders):
        rendelesFrame=tk.Frame(window,borderwidth=2,relief="raised")
        rendelesPhotoPlace=tk.Label(rendelesFrame,image=photo[i])
        rendelesPhotoPlace.pack()
        label1=tk.Label(rendelesFrame,text=rendelese.pizza.name)
        label1.pack()
        label2=tk.Label(rendelesFrame,text=rendelese.user.name)
        label2.pack()
        label3=tk.Label(rendelesFrame,text=rendelese.price)
        label3.pack()
        gomb=tk.Button(rendelesFrame,text="Rendelés Szerkesztése")
        gomb.pack()
        rendelesFrame.grid(row=i,column=0,padx=100,pady=30)