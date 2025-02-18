from tkinter import *

root = Tk()
root.config(bg="#dc0251")
root.title("Martina Di Trento")
miFrame = Frame(root)
miFrame.config(bg="#c31632")
miFrame.pack()

miImage= PhotoImage (file="C:\shinzou\python\programa_MartinaDiTrento\interfaz\imagenes\logo.png")

miLabel1 = Label(miFrame,bg="#dc0251", image=miImage, width= 600, height=120)
miLabel1.grid(row=0, column=0, columnspan=2)




cuadroApellido = Entry(miFrame, justify="center")
cuadroApellido.grid(row=1, column=1)

cuadroNombre = Entry(miFrame, justify="center")
cuadroNombre.grid(row=2, column=1)

cuadroCodigoVendedora = Entry(miFrame, justify="center")
cuadroCodigoVendedora.grid(row=3, column=1)



apellidoLabel = Label(miFrame, text="Apellido")
apellidoLabel.grid(row=1, column=0, padx=10, pady=10)

nombreLabel = Label(miFrame, text="Nombre")
nombreLabel.grid(row=2, column=0, padx=10, pady=10)

codigoVendedoraLabel = Label(miFrame, text="Codigo de Vendedora")
codigoVendedoraLabel.grid(row=3, column=0, padx=10, pady=10)


botonAgregar = Button(root, text="Agregar", justify="center",)
botonAgregar.pack()



root.mainloop()