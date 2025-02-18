import sqlite3
import pandas as pd
import matplotlib as plt

from modulo_consultas_generales import ver_tabla as ver_tabla


# Vista total pagos, facturas y cambios
def total_pagos_facturas():
    vista = "CREATE VIEW tabla_completa AS SELECT * FROM Facturacion AS f FULL OUTER JOIN Vendedoras v on v.CodVendedora = f.CodVendedora FULL OUTER JOIN Pagos p on p.CodVendedora = v.CodVendedora FULL OUTER JOIN Cambios c on c.CodVendedora = f.CodVendedora"
    consulta = "SELECT CodVendedora, apellido, nombre, SUM(importe) as pagos_totales, SUM(monto_factura) as total_facturación, SUM(PRECIO) - SUM(descuento) as total_cambios FROM tabla_completa ORDER BY CodVendedora"
    conn = sqlite3.connect('martinaDiTrento.db')
    cursor = conn.cursor()  
    cursor.execute(vista)
    conn.commit()
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    resultado_db = pd.DataFrame(resultado)
    print(resultado_db)
    cursor.execute('DROP VIEW tabla_completa')
    conn.commit()
    cursor.close()     
    conn.close()
    
# muestra total pagos, facturas y cambios POR CAMPAÑA
def total_pagos_campaña():
    campaña = int(input("Ingrese el número de la campaña: "))
    vista = "CREATE VIEW tabla_completa AS SELECT * FROM Facturacion AS f FULL OUTER JOIN Vendedoras v on v.CodVendedora = f.CodVendedora FULL OUTER JOIN Pagos p on p.CodVendedora = v.CodVendedora FULL OUTER JOIN Cambios c on c.CodVendedora = f.CodVendedora"
    consulta = f"SELECT CodVendedora, apellido, nombre, SUM(importe) as pagos_totales, SUM(monto_factura) as total_facturación, SUM(PRECIO) - SUM(descuento) as total_cambios FROM tabla_completa WHERE numero_campaña LIKE {campaña} ORDER BY CodVendedora"
    conn = sqlite3.connect('martinaDiTrento.db')
    cursor = conn.cursor()  
    cursor.execute(vista)
    conn.commit()
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    resultado_db = pd.DataFrame(resultado)
    print(resultado_db)
    cursor.execute('DROP VIEW tabla_completa')
    conn.commit()
    cursor.close()     
    conn.close()

#Muestra el total de la Deuda de todas vendedora
def total_resto_vendedoras():
    vista = "CREATE VIEW restos_vendedora AS SELECT * FROM Facturacion AS f FULL OUTER JOIN Vendedoras v on v.CodVendedora = f.CodVendedora FULL OUTER JOIN Pagos p on p.CodVendedora = v.CodVendedora FULL OUTER JOIN Cambios c on c.CodVendedora = f.CodVendedora"
    consulta = "SELECT CodVendedora, apellido, nombre, SUM(precio) - SUM(descuento) as total_cambio, SUM(importe) as pagos_totales, SUM(monto_factura) as total_facturación, SUM(monto_factura) - SUM(importe) - SUM(precio) + SUM(descuento) as Saldo_Restante FROM restos_vendedora GROUP BY CodVendedora"
    conn = sqlite3.connect('martinaDiTrento.db')
    cursor = conn.cursor()  
    cursor.execute(vista)
    conn.commit()
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    resultado_db = pd.DataFrame(resultado)
    print(resultado_db)
    cursor.execute('DROP VIEW restos_vendedora')
    conn.commit()
    cursor.close()     
    conn.close()


def menu_saldos():
    selector_menu_saldos = input("""Seleccione la opción deseada: 
                          1_ Saldo Vendedoras por campaña
                          2_ Saldo Vendedoras total
                          3_ Salir
                          """)
    if selector_menu_saldos == "1":
        total_pagos_campaña()
        repeat = input("desea ver algo mas? Si-No : ")
        while repeat == "Si":
            menu_saldos()
            repeat = input("desea ver algo mas? Si-No : ")
    elif selector_menu_saldos == "2":
        total_resto_vendedoras()
        repeat = input("desea ver algo mas? Si-No : ")
        while repeat == "Si":
            selector_menu_saldos()
            repeat = input("desea ver algo mas? Si-No : ")
    elif selector_menu_saldos == "3":
        pass
    else:
        print("opcion incorrecta")
        menu_saldos()


