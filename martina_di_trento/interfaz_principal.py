import sqlite3
from tkinter import *
from tkinter import messagebox

#Modulo BBDD
from modulos.menu_vendedoras import agregar_vendedora as agregar_vendedora


#Modulo BBDD
from modulos.create_bbdd import conexion_BBDD as conexion_BBDD
from modulos.create_bbdd import limpiar_datos_BBDD as limpiar_datos_BBDD

root = Tk()
root.title("Martina Di Trento")
root.geometry("1200x600")

barraMenu=Menu(root)


#---------------------------------Ventanas Menu principal-----------------------


#--------------
#Menú Vendedora
#-----
#Agregar Vendedora

def opcion_agregar_vendedora():
    def limpiarCampos():
        miCod.set("")
        miApellido.set("")
        miNombre.set("")
        miCredito.set(False)

    def agregar():
        agregar_vendedora(miCod.get(),miApellido.get(),miNombre.get(),miCredito.get())
        limpiarCampos()
        ventana_vendAgregada()
        
    def ventana_vendAgregada():
        messagebox.showinfo("Vendedora Agregada", "Bien ahi pirulin!")

        
    miCod = StringVar()
    miApellido = StringVar()
    miNombre = StringVar()
    miCredito = BooleanVar()

    ventana_agregar_vendedora=Toplevel(root)
    ventana_agregar_vendedora.title("Agregar Vendedora")
    ventana_agregar_vendedora.geometry("+550+200")
    ventana_agregar_vendedora.config(bg="#dc0251")
    
    miFrame = Frame(ventana_agregar_vendedora)
    miFrame.config(bg="#dc0251")
    miFrame.pack(pady=30)
        
    codigoLabel = Label(miFrame, text="Codigo Vendedora: ")
    codigoLabel.grid (row=0, column=0, padx=10, pady=10, sticky="nsew")

    apellidoLabel= Label(miFrame, text="Apellido: ")
    apellidoLabel.grid (row=1, column=0, padx=10, pady=10, sticky="nsew")

    nombreLabel= Label(miFrame, text="Nombre: ")
    nombreLabel.grid (row=2, column=0, padx=10, pady=10, sticky="nsew")
    
    creditoLabel= Label(miFrame, text="Crédito: ")
    creditoLabel.grid (row=3, column=0, padx=10, pady=10, sticky="nsew")

    cuadroCodigo= Entry(miFrame, textvariable= miCod)
    cuadroCodigo.grid (row=0, column=1, padx=20, pady=10, sticky="e")

    cuadroApellido= Entry(miFrame, textvariable= miApellido)
    cuadroApellido.grid (row=1, column=1, padx=20, pady=10, sticky="e")

    cuadroNombre= Entry(miFrame, textvariable= miNombre)
    cuadroNombre.grid (row=2, column=1, padx=20, pady=10, sticky="e")
    
    creditoButton1= Radiobutton(miFrame, text=" Si ", variable= miCredito, value=1)
    creditoButton1.grid (row=3, column=1, padx=20, pady=10, sticky="n")
    
    creditoButton2= Radiobutton(miFrame, text="No", variable= miCredito, value=2)
    creditoButton2.grid (row=4, column=1, padx=20, sticky="n")

    botonAgregar=Button(miFrame, text="Agregar", command=agregar)
    botonAgregar.grid (row=5, column=0, padx=30, pady=30, sticky="e")

    botonCancelar=Button(miFrame, text="Cancelar", command=ventana_agregar_vendedora.destroy)
    botonCancelar.grid (row=5, column=1, padx=30, pady=30, sticky="n")
    
#Editar Vendedora


#Ver Vendedoras



#--------------
#Menú Vendedora
#-----
#Agregar Pago
    
def opcion_agregar_pagos():
    def limpiarCampos():
        miImporte.set("")
        miDescripcion.set("")
        miCod.set("")
        miDestino.set("")
        miCampaña.set("")

    def agregar():
        pass

    def ventana_pagoAgregado():
        pass
        """
        messagebox.showinfo("Pago Agregado", "Bien ahi pirulin!")
        """
    
    miImporte= DoubleVar()
    miDescripcion = StringVar()
    miCod = StringVar()
    miDestino = StringVar()
    miCampania = IntVar()   

    ventana_agregar_pago=Toplevel(root)
    ventana_agregar_pago.title("Agregar Pago")
    ventana_agregar_pago.geometry("+550+200")
    ventana_agregar_pago.config(bg="#dc0251")
    
    miFrame = Frame(ventana_agregar_pago)
    miFrame.config(bg="#dc0251")
    miFrame.pack(pady=30)
        
    importeLabel = Label(miFrame, text="Importe: ")
    importeLabel.grid (row=0, column=0, padx=10, pady=10, sticky="nsew")

    descripcionLabel= Label(miFrame, text="Descripción: ")
    descripcionLabel.grid (row=1, column=0, padx=10, pady=10, sticky="nsew")

    codigoLabel= Label(miFrame, text="Codigo Vendedora: ")
    codigoLabel.grid (row=2, column=0, padx=10, pady=10, sticky="nsew")
    
    destinoLabel= Label(miFrame, text="Destino: ")
    destinoLabel.grid (row=3, column=0, padx=10, pady=10, sticky="nsew")
    
    campaniaLabel= Label(miFrame, text="Campaña: ")
    campaniaLabel.grid (row=6, column=0, padx=10, pady=10, sticky="nsew")

    cuadroImporte= Entry(miFrame, textvariable= miImporte)
    cuadroImporte.grid (row=0, column=1, padx=20, pady=10, sticky="e")

    cuadroDescripcion= Entry(miFrame, textvariable= miDescripcion)
    cuadroDescripcion.grid (row=1, column=1, padx=20, pady=10, sticky="e")
    
    cuadroCodVendedora= Entry(miFrame, textvariable=miCod)
    cuadroCodVendedora.grid (row=2, column=1, padx=20, pady=10, sticky="e")

    creditoButton1= Radiobutton(miFrame, text="Empresa", variable= miDestino, value="Empresa")
    creditoButton1.grid (row=3, column=1, padx=20,  pady=10, sticky="n")
    
    creditoButton2= Radiobutton(miFrame, text=" Zulma ", variable= miDestino, value="Zulma")
    creditoButton2.grid (row=4, column=1, padx=20,  pady=10, sticky="n")

    creditoButton3= Radiobutton(miFrame, text="  Otro  ", variable= miDestino, value="Otro")
    creditoButton3.grid (row=5, column=1, padx=20,  pady=10,sticky="n")
    
    cuadroCampania= Entry(miFrame, textvariable= miCampania)
    cuadroCampania.grid (row=6, column=1, padx=20, pady=10, sticky="e")
    
    botonAgregar=Button(miFrame, text="Agregar")
    botonAgregar.grid (row=7, column=0, padx=30, pady=30, sticky="e")

    botonCancelar=Button(miFrame, text="Cancelar", command=ventana_agregar_pago.destroy)
    botonCancelar.grid (row=7, column=1, padx=30, pady=30, sticky="n")
    
    
    
    
    
#Menu Base de Datos
#Crear BBDD
def crear_bbdd():
    try:
        conexion_BBDD()
        messagebox.showinfo("Creacion de Base de Datos", "La Base de Datos ha sido creada")
    except:
        messagebox.showinfo("Error de Base de Datos", "La Base de Datos no pudo crearse")

#Vaciar BBDD
def vaciar_bbdd():
    try:
        limpiar_datos_BBDD()
        messagebox.showinfo("Limpieza de Base de Datos", "La Base de Datos ha sido limpiada")
    except:
        messagebox.showinfo("Error Limpieza de Base de Datos", "La Base de Datos no pudo limpiarse")

    
    
    
#--------------------------------------------------------------

#Menu Principal

#Menu Vendedora
vendedoraMenu=Menu(barraMenu, tearoff=0)
vendedoraMenu.add_command(label="Agregar Vendedora", command=opcion_agregar_vendedora)
vendedoraMenu.add_command(label="Editar Vendedora (no conf)") #no configurado
vendedoraMenu.add_command(label="Ver Vendedoras (no conf)") #no configurado

#Menu Pagos
pagosMenu=Menu(barraMenu, tearoff=0)
pagosMenu.add_command(label="Agregar Pago", command=opcion_agregar_pagos)
pagosMenu.add_command(label="Editar Pago (no conf)") #no configurado
pagosMenu.add_command(label="Ver Pagos (no conf)") #no configurado

#Menu Cambios
cambiosMenu=Menu(barraMenu, tearoff=0)
cambiosMenu.add_command(label="Agregar Cambio (no conf)") #no configurado
cambiosMenu.add_command(label="Editar Cambio (no conf)") #no configurado
cambiosMenu.add_command(label="Ver Cambios (no conf)") #no configurado

#Menu Facturación
facturacionMenu=Menu(barraMenu, tearoff=0)
facturacionMenu.add_command(label="Agregar Factura (no conf)") #no configurado
facturacionMenu.add_command(label="Editar Factura (no conf)") #no configurado
facturacionMenu.add_command(label="Ver Facturas (no conf)") #no configurado

#Menu Saldos
saldoMenu=Menu(barraMenu, tearoff=0)
saldoMenu.add_command(label="Saldo por campaña (no conf)") #no configurado
saldoMenu.add_command(label="Total (no conf)") #no configurado

#Menu Personal
personalMenu=Menu(barraMenu, tearoff=0)
personalMenu.add_command(label="opcion1 (no conf)") #no configurado
personalMenu.add_command(label="opcion2 (no conf)") #no configurado

#Menu Base de Datos
bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Crear BBDD", command=crear_bbdd)
bbddMenu.add_command(label="Exportar BBDD (no conf)")
bbddMenu.add_command(label="Vaciar BBDD", command=vaciar_bbdd)

barraMenu.add_cascade(label="Vendedoras", menu=vendedoraMenu)
barraMenu.add_cascade(label="Pagos", menu=pagosMenu)
barraMenu.add_cascade(label="Cambios", menu=cambiosMenu)
barraMenu.add_cascade(label="Facturación", menu=facturacionMenu)
barraMenu.add_cascade(label="Saldos", menu=saldoMenu)
barraMenu.add_cascade(label="Personal", menu=personalMenu)
barraMenu.add_cascade(label="BBDD", menu=bbddMenu)

root.config(bg="#c31632", menu=barraMenu)

miFrame = Frame(root)
miFrame.pack()

miImage= PhotoImage (file="C:\shinzou\python\programa_MartinaDiTrento\interfaz\imagenes\logo.png")
miLabel1 = Label(root,bg="#dc0251", image=miImage, width= 600, height=120)
miLabel1.place(relx=0.25, rely=0.5)

root.mainloop()

