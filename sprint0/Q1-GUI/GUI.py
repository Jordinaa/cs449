from tkinter import *
import customtkinter

# Reference https://medium.com/@fareedkhandev/modern-gui-using-tkinter-12da0b983e22

root = customtkinter.CTk()
root.geometry("500x450")

button = customtkinter.CTkButton(master=root, text="hello world")
button.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()

