import sqlite3
import pandas as pd
import matplotlib as plt


from modulo_consultas_generales import ver_tabla as ver_tabla  

def agregar_factura():
    año = int(input("Escriba el año: "))
    numero_campaña = int(input("Escriba el numero de campaña: "))
    codVendedora = input("Escriba el codigo de la vendedora: ")
    monto_factura = float(input("Escriba el monto de la factura: ")) 
    conn = sqlite3.connect('martinaDiTrento.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO Facturacion(año,numero_campaña,codVendedora,monto_factura) VALUES({año},'{numero_campaña}','{codVendedora}','{monto_factura}')")
    conn.commit()
    cursor.close()
    conn.close()
    print("Pago agregado!")
    
def eliminar_factura():
    facturaId = int(input("Ingrese el ID de la factura: "))
    conn = sqlite3.connect('martinaDiTrento.db')
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM Pagos WHERE pagosId == {facturaId}")
    conn.commit()
    cursor.close()
    conn.close()
    
def resetear_IDFactura():
    conn = sqlite3.connect('martinaDiTrento.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Facturacion")  
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='Facturacion'")
    conn.commit()
    cursor.close()

    conn.close()


def menu_facturacion():
    selector_menu_facturacion = input("""Seleccione la opción deseada: 
                          1_ Agregar Factura
                          2_ Eliminar Factura
                          3_ Ver Facturas
                          4_ Salir
                          """)
    if selector_menu_facturacion == "1":
        agregar_factura()
        repeat = input("desea seguir agregando Facturas? Si-No : ")
        while repeat == "Si":
            agregar_factura()
            repeat = input("desea seguir agregando Facturas? Si-No : ")
        else:
            menu_facturacion()
            
    elif selector_menu_facturacion == "2":
        eliminar_factura()
        repeat = input("desea eliminar otra Factura? Si-No : ")
        while repeat == "Si":
            agregar_pagos()
            repeat = input("desea eliminar otra Factura? Si-No : ")          
    elif selector_menu_facturacion == "3":
        ver_tabla("Facturacion")
        repeat = input("Seguir en menu Facturacion Si-No : ")
        while repeat == "Si":
            menu_facturacion()
            repeat = input("Seguir en menu Facturacion? Si-No : ")
    elif selector_menu_facturacion == "4":
        pass
    else:
        print("opcion incorrecta")
        menu_facturacion()