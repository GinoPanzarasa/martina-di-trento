import sqlite3
import pandas as pd
import matplotlib as plt

from modulo_consultas_generales import ver_tabla as ver_tabla  


def agregar_vendedora(codVendedora,apellido,nombre):
    """codVendedora = input("Escriba el Código de la Vendedora: ")
    apellido = input("Escriba el apellido de la Vendedora: ")
    nombre = input("Escriba el nombre vendedora: ")"""
    conn = sqlite3.connect('martinaDiTrento.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO Vendedoras(codVendedora,apellido,nombre) VALUES(?,?,?)", (codVendedora, apellido, nombre))
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_vendedora(codigo_vendedora):
    #codigo_vendedora = input("Ingrese el Codigo de la Vendedora: ")
    conn = sqlite3.connect('martinaDiTrento.db')
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM Vendedoras WHERE codVendedora == '{codigo_vendedora}'")
    conn.commit()
    cursor.close()
    conn.close()
    
def menu_vendedoras():
    selector_menu_vendedoras = input("""Seleccione la opción deseada: 
                          1_ Agregar Vendedora
                          2_ Eliminar Vendedora
                          3_ Ver Vendedoras
                          4_ Salir
                          """)
    if selector_menu_vendedoras == "1":
        agregar_vendedora()
        repeat = input("desea seguir agregando vendedoras? Si-No : ")
        while repeat == "Si":
            agregar_vendedora()
            repeat = input("desea seguir agregando vendedoras? Si-No : ")
    elif selector_menu_vendedoras == "2":
        eliminar_vendedora()
        repeat = input("desea eliminar otra vendedora? Si-No : ")
        while repeat == "Si":
            agregar_pagos()
            repeat = input("desea eliminar otra vendedora? Si-No : ")
    elif selector_menu_vendedoras == "3":
        ver_tabla("Vendedoras")
        repeat = input("Seguir en menu Vendedoras? Si-No : ")
        while repeat == "Si":
            menu_vendedoras()
            repeat = input("Seguir en menu Vendedoras? Si-No : ")
    elif selector_menu_vendedoras == "4":
        pass
    else:
        print("opcion incorrecta")
        menu_vendedoras()