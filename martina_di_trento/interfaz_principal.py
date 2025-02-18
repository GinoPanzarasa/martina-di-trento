from tkinter import *

root = Tk()
root.title("Martina Di Trento")
root.geometry("1200x600")


barraMenu=Menu(root)


#Menu Vendedora
vendedoraMenu=Menu(barraMenu, tearoff=0)
vendedoraMenu.add_command(label="Agregar Vendedora")
vendedoraMenu.add_command(label="Editar Vendedora")
vendedoraMenu.add_command(label="Eliminar Vendedora")
vendedoraMenu.add_command(label="Ver Vendedoras")

#Menu Pagos
pagosMenu=Menu(barraMenu, tearoff=0)
pagosMenu.add_command(label="Agregar Pago")
pagosMenu.add_command(label="Editar Pago")
pagosMenu.add_command(label="Eliminar Pago")
pagosMenu.add_command(label="Ver Pagos")

#Menu Cambios
cambiosMenu=Menu(barraMenu, tearoff=0)
cambiosMenu.add_command(label="Agregar Cambio")
cambiosMenu.add_command(label="Editar Cambio")
cambiosMenu.add_command(label="Eliminar Cambio")
cambiosMenu.add_command(label="Ver Cambios")

#Menu Facturación
facturacionMenu=Menu(barraMenu, tearoff=0)
facturacionMenu.add_command(label="Agregar Factura")
facturacionMenu.add_command(label="Editar Factura")
facturacionMenu.add_command(label="Eliminar Factura")
facturacionMenu.add_command(label="Ver Facturas")

#Menu Saldos
saldoMenu=Menu(barraMenu, tearoff=0)
saldoMenu.add_command(label="Saldo por campaña")
saldoMenu.add_command(label="Total")

#Menu Personal
personalMenu=Menu(barraMenu, tearoff=0)
personalMenu.add_command(label="opcion1")
personalMenu.add_command(label="opcion2")

barraMenu.add_cascade(label="Vendedoras", menu=vendedoraMenu)
barraMenu.add_cascade(label="Pagos", menu=pagosMenu)
barraMenu.add_cascade(label="Cambios", menu=cambiosMenu)
barraMenu.add_cascade(label="Facturación", menu=facturacionMenu)
barraMenu.add_cascade(label="Saldos", menu=saldoMenu)
barraMenu.add_cascade(label="Personal", menu=personalMenu)


root.config(bg="#c31632", menu=barraMenu)

miFrame = Frame(root)
miFrame.pack()

miImage= PhotoImage (file="C:\shinzou\python\programa_MartinaDiTrento\interfaz\imagenes\logo.png")
miLabel1 = Label(root,bg="#dc0251", image=miImage, width= 600, height=120)
miLabel1.place(relx=0.25, rely=0.5)

root.mainloop()