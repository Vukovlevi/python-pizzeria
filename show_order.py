from storage import orders
import tkinter as tk


def show_order_window(window,photo):
    window.title("Rendelések")
    window.geometry("400x700")
    window.config(bg="grey")

    canvas = tk.Canvas(window, bg="grey")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.config(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda _: canvas.config(scrollregion=canvas.bbox("all")))

    holder = tk.Frame(canvas, bg="grey")
    holder.bind("<Configure>", lambda _: canvas.config(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=holder)

    for i,rendelese in enumerate(orders):
        rendelesFrame=tk.Frame(holder,borderwidth=2,relief="raised",bg="#8C7473")
        rendelesPhotoPlace=tk.Label(rendelesFrame,image=photo[i],bg="#8C7473")
        rendelesPhotoPlace.pack()
        label1=tk.Label(rendelesFrame,text=rendelese.pizza.name,bg="#8C7473",font="bold")
        label1.pack()
        label2=tk.Label(rendelesFrame,text=rendelese.user.name,bg="#8C7473")
        label2.pack()
        label3=tk.Label(rendelesFrame,text=f"{rendelese.price}Ft",bg="#8C7473")
        label3.pack()
        label5=tk.Label(rendelesFrame,text="Feltétek:",bg="#8C7473")
        label5.pack()
        toppingFrame=tk.Frame(rendelesFrame)
        for j in range(len(rendelese.toppings)):
            label4=tk.Label(toppingFrame,text=rendelese.toppings[j],bg="#8C7473")
            label4.pack(side="left")
        toppingFrame.pack()
        gomb1=tk.Button(rendelesFrame,text="Rendelés szerkesztése",pady=5)
        gomb1.pack()
        rendelesFrame.grid(row=i,column=0,padx=100,pady=30)
