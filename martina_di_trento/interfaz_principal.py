from tkinter import *

root = Tk()
root.title("Martina Di Trento")
root.geometry("1200x600")
root.config(bg="#c31632")
miFrame = Frame(root)
miFrame.pack()

miImage= PhotoImage (file="C:\shinzou\python\programa_MartinaDiTrento\interfaz\imagenes\logo.png")
miLabel1 = Label(root,bg="#dc0251", image=miImage, width= 600, height=120)
miLabel1.place(relx=0.25, rely=0.5)

root.mainloop()