from storage import orders
import tkinter as tk


def show_order_window(window):
    window.title("Rendelések")
    window.geometry("400x700")
    label=tk.Label(window,text=orders)
    label.pack()