from tkinter import *

root = Tk()
root.title("Martina Di Trento")
miFrame = Frame(root)
miFrame.config(bg="#c31632")
miFrame.pack()

miImage= PhotoImage (file="C:\shinzou\python\programa_MartinaDiTrento\interfaz\imagenes\logo.png")
miLabel1 = Label(root,bg="#dc0251", image=miImage, width= 600, height=120)
miLabel1.pack()



"""
botonVendedoras = Button(miFrame, text="Vendedoras", justify="center", width=20)
botonVendedoras.pack()

botonPagos = Button(miFrame, text="Pagos", width=20)
botonPagos.pack()

botonFacturacion = Button(miFrame, text="Facturacion", width=20)
botonFacturacion.pack()

botonSaldo = Button(miFrame, text="Saldo Vendedoras", width=20)
botonSaldo.pack()

botonCambios = Button(miFrame, text="Cambios", width=20)
botonCambios.pack()

botonSalir = Button(miFrame, text="Salir", width=20)
botonSalir.pack()



"""

root.mainloop()