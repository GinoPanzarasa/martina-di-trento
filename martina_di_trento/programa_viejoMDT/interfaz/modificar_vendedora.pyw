import sqlite3
from tkinter import *
from tkinter import messagebox

def limpiarCampos():
    miCod.set("")
    miApellido.set("")
    miNombre.set("")

def modificar():
    conn = sqlite3.connect('martinaDiTrento.db')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE Vendedoras SET apellido = ?, nombre = ? WHERE codVendedora = ?", (miApellido.get(), miNombre.get(), miCod.get()))
    conn.commit()
    cursor.close()
    conn.close()
    limpiarCampos()
    ventana_vendModificada()

def ventana_vendModificada():
    messagebox.showinfo("Vendedora Modificada", "Bien ahi pirulin x2!")
   

root = Tk()
root.geometry("350x300")
#root.resizable(0,0)
root.title("Agregar Vendedora")
root.config(bg="#c31632")

miCod = StringVar()
miApellido = StringVar()
miNombre = StringVar()



miFrame = Frame(root, width=1000, height=1800)
miFrame.config(bg="#dc0251")
miFrame.pack(pady=30)

codigoLabel = Label(miFrame, text="Codigo Vendedora: ")
codigoLabel.grid (row=0, column=0, padx=10, pady=10, sticky="nsew")

apellidoLabel= Label(miFrame, text="Apellido: ")
apellidoLabel.grid (row=1, column=0, padx=10, pady=10, sticky="nsew")

nombreLabel= Label(miFrame, text="Nombre: ")
nombreLabel.grid (row=2, column=0, padx=10, pady=10, sticky="nsew")

cuadroCodigo= Entry(miFrame, textvariable= miCod)
cuadroCodigo.grid (row=0, column=1, padx=20, pady=10, sticky="e")

cuadroApellido= Entry(miFrame, textvariable= miApellido)
cuadroApellido.grid (row=1, column=1, padx=20, pady=10, sticky="e")

cuadroNombre= Entry(miFrame, textvariable= miNombre)
cuadroNombre.grid (row=2, column=1, padx=20, pady=10, sticky="e")

botonAgregar=Button(miFrame, text="Modificar", command=modificar)
botonAgregar.grid (row=3, column=0, padx=30, pady=30, sticky="e")

botonCancelar=Button(miFrame, text="Cancelar", command=root.destroy)
botonCancelar.grid (row=3, column=1, padx=30, pady=30, sticky="n")


root.mainloop()