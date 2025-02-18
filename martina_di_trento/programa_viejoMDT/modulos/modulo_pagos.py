import sqlite3
import pandas as pd
import matplotlib as plt


from modulo_consultas_generales import ver_tabla as ver_tabla  

def agregar_pagos():
    importe = float(input("Escriba el importe: "))
    descripcion = input("Descripcion del pago: ")
    codVendedora = input("Escriba el codigo de la vendedora: ")
    destino_pago = input("Escriba el destino del pago: ") 
    conn = sqlite3.connect('martinaDiTrento.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO Pagos(importe,descripcion,codVendedora,destino) VALUES({importe},'{descripcion}','{codVendedora}','{destino_pago}')")
    conn.commit()
    cursor.close()
    conn.close()
    print("Pago agregado!")
     

def eliminar_pago():
    pagosId = int(input("Ingrese el ID del pago: "))
    conn = sqlite3.connect('martinaDiTrento.db')
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM Pagos WHERE pagosId == {pagosId}")
    conn.commit()
    cursor.close()
    conn.close()

def pagos_por_vendedora():
    vendedora = input("Introduzca el código de la Vendedora o el Apellido: ")
    vista = "CREATE VIEW pagos_de_vendedora AS SELECT * FROM Pagos p INNER JOIN Vendedoras v ON p.CodVendedora = v.CodVendedora"          
    consulta = (f"SELECT CodVendedora, importe, apellido FROM pagos_de_vendedora WHERE CodVendedora LIKE '{vendedora}' OR apellido LIKE '{vendedora}'")
    conn = sqlite3.connect('martinaDiTrento.db')
    cursor = conn.cursor()
    cursor.execute(vista)
    conn.commit()
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    resultado_db = pd.DataFrame(resultado)
    print(resultado_db)
    cursor.execute('DROP VIEW pagos_de_vendedora')
    conn.commit()
    cursor.close()     
    conn.close()


def ver_pagos():
    vista = "CREATE VIEW pagos_de_vendedora AS SELECT * FROM Pagos p JOIN Vendedoras v ON p.CodVendedora = v.CodVendedora"          
    consulta = "SELECT * FROM pagos_de_vendedora"
    conn = sqlite3.connect('martinaDiTrento.db')
    cursor = conn.cursor()
    cursor.execute(vista)
    conn.commit()
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    resultado_db = pd.DataFrame(resultado)
    print(resultado_db)
    cursor.execute('DROP VIEW pagos_de_vendedora')
    conn.commit()
    cursor.close()     
    conn.close()







def resetear_IDPago():
    conn = sqlite3.connect('martinaDiTrento.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Pagos")  
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='Pagos'")
    conn.commit()
    cursor.close()
    conn.close()
     

def borrar_vista():
    conn = sqlite3.connect('martinaDiTrento.db')
    cursor = conn.cursor()
    cursor.execute("DROP VIEW pagos_de_vendedora")  
    conn.commit()
    cursor.close()
    conn.close()
     



def menu_pagos():
    selector_menu_pagos = input("""Seleccione la opción deseada: 
                          1_ Agregar Pago
                          2_ Eliminar Pago
                          3_ Ver Pagos
                          4_ Salir
                          """)
    if selector_menu_pagos == "1":
        agregar_pagos()
        repeat = input("desea seguir agregando pagos? Si-No : ")
        while repeat == "Si":
            agregar_pagos()
            repeat = input("desea seguir agregando pagos? Si-No : ")
    elif selector_menu_pagos == "2":
        eliminar_pago()
        repeat = input("desea eliminar otro pago? Si-No : ")
        while repeat == "Si":
            agregar_pagos()
            repeat = input("desea eliminar otro pago? Si-No : ")
    elif selector_menu_pagos == "3":
        submenu_pagos = input("""
                              1_ Total Pagos
                              2_ Pagos por vendedora
                              3_ Salir
                              
                              -----------------------
                              
                              """)
        if submenu_pagos == "1":
            ver_pagos()
            repeat = input("Seguir en menu Pago? Si-No : ")
            while repeat == "Si":
                menu_pagos()
                repeat = input("Seguir en menu Pago? Si-No : ")
        elif submenu_pagos == "2":
            pagos_por_vendedora()
            repeat = input("Seguir en menu Pago? Si-No : ")
            while repeat == "Si":
                menu_pagos()
                repeat = input("Seguir en menu Pagos? Si-No : ")
        else:
            print("No es una opcion válida")
    elif selector_menu_pagos == "4":
        pass
    else:
        print("opcion incorrecta")
        menu_pagos()




#borrar_vista()
