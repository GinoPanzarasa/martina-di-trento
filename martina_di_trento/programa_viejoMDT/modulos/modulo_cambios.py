import sqlite3
import pandas as pd
import matplotlib as plt


from modulo_consultas_generales import ver_tabla as ver_tabla  


def agregar_cambio():
    codVendedora = input("Escriba el codigo de la vendedora: ")
    prenda = input("Escriba la prenda: ")
    talle = int(input("Escriba el talle de la prenda: "))
    cantidad = int(input("Escriba la cantidad: "))
    precio = float(input("Escriba el precio: "))
    descuento = float(input("Escriba el descuento de la prenda: "))
    numero_campaña = int(input("Introduzca la campaña: "))
    conn = sqlite3.connect('martinaDiTrento.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO Cambios(codVendedora, prenda, talle, cantidad, precio, descuento, numero_campaña) VALUES('{codVendedora}','{prenda}',{talle},{cantidad},{precio},{descuento},{numero_campaña})")
    conn.commit()
    cursor.close()
    conn.close()
    print("prenda agregada!")


def eliminar_cambio():
    pagosId = int(input("Ingrese el ID del Cambio: "))
    conn = sqlite3.connect('martinaDiTrento.db')
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM Cambios WHERE cambioId == {cambioId}")
    conn.commit()
    cursor.close()
    conn.close()

def menu_cambios():
    selector_menu_cambios = input("""Seleccione la opción deseada: 
                          1_ Agregar Cambio
                          2_ Eliminar Cambio
                          3_ Ver Cambios
                          4_ Salir
                          """)
    if selector_menu_cambios == "1":
        agregar_cambio()
        repeat = input("desea seguir agregando cambios de prendas? Si-No : ")
        while repeat == "Si":
            agregar_cambio()
            repeat = input("desea seguir agregando cambios de prendas? Si-No : ")
    elif selector_menu_cambios == "2":
        eliminar_cambio()
        repeat = input("desea eliminar otro Cambio? Si-No : ")
        while repeat == "Si":
            eliminar_cambio()
            repeat = input("desea eliminar otro Cambio? Si-No : ")
    elif selector_menu_cambios == "3":
        ver_tabla("Cambios")
        repeat = input("Seguir en menu Cambios? Si-No : ")
        while repeat == "Si":
            menu_cambios()
            repeat = input("Seguir en menu Cambios? Si-No : ")
    elif selector_menu_cambios == "4":
        pass
    else:
        print("opcion incorrecta")
        menu_cambios()




