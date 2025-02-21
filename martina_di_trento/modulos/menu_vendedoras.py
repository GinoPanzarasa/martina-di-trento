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

"""
def modificar_vendedora(codigo_vendedora):
    #codigo_vendedora = input("Ingrese el Codigo de la Vendedora: ")
    conn = sqlite3.connect('martinaDiTrento.db')
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM Vendedoras WHERE codVendedora == '{codigo_vendedora}'")
    conn.commit()
    cursor.close()
    conn.close()
"""
    
