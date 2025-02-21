import sqlite3
import pandas as pd
import matplotlib as plt



def agregar_vendedora(codVendedora,apellido,nombre,credito):
    conn = sqlite3.connect('martinaDiTrento.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO Vendedoras(codVendedora,apellido,nombre,credito) VALUES(?,?,?,?)", (codVendedora, apellido, nombre, credito))
    conn.commit()
    cursor.close()
    conn.close()



def leer_vendedora(codigo_vendedora):
    conn = sqlite3.connect('martinaDiTrento.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT FROM Vendedoras WHERE codVendedora == '{codigo_vendedora}'")
    mi_vendedora=cursor.fetchall() #devuelve la consulta almacenada en un array

    for vendedora in mi_vendedora:
        miCod.set(vendedora[0])
        miApellido.set(vendedora[1])
        miNombre.set(vendedora[2])
        miCredito.set(vendedora[3])
        return miCod, miApellido, miNombre, miCredito
    conn.commit()
    cursor.close()
    conn.close()



def borrar_vendedora(codigo_vendedora):
    conn = sqlite3.connect('martinaDiTrento.db')
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM Vendedoras WHERE codVendedora == '{codigo_vendedora}' OR ")
    mi_vendedora=cursor.fetchall() #devuelve la consulta almacenada en un array
    for vendedora in mi_vendedora:
        miCod.set(vendedora[0])
        miApellido.set(vendedora[1])
        miNombre.set(vendedora[2])
        miCredito.set(vendedora[3])
    conn.commit()
    cursor.close()
    conn.close()

    
