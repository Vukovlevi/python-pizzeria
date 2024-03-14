from storage import orders
import tkinter as tk


def show_order_window(window,photo):
    window.title("Rendelések")
    window.geometry("400x700")
    window.config(bg="grey")
    for i,rendelese in enumerate(orders):
        rendelesFrame=tk.Frame(window,borderwidth=2,relief="raised",bg="#8C7473")
        rendelesPhotoPlace=tk.Label(rendelesFrame,image=photo[i],bg="#8C7473")
        rendelesPhotoPlace.pack()
        label1=tk.Label(rendelesFrame,text=rendelese.pizza.name,bg="#8C7473",font="bold")
        label1.pack()
        label2=tk.Label(rendelesFrame,text=rendelese.user.name,bg="#8C7473")
        label2.pack()
        label3=tk.Label(rendelesFrame,text=f"{rendelese.price}Ft",bg="#8C7473")
        label3.pack()
        gomb=tk.Button(rendelesFrame,text="Rendelés szerkesztése")
        gomb.pack()
        rendelesFrame.grid(row=i,column=0,padx=100,pady=30)