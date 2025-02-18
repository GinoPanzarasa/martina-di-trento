import sqlite3
import pandas as pd
import matplotlib as plt

#Modulo_Vendedoras:
from modulo_vendedoras import menu_vendedoras as menu_vendedoras   

# Modulo_pagos:
from modulo_pagos import menu_pagos as menu_pagos 

# Modulo_facturacion:
from modulo_facturacion import menu_facturacion as menu_facturacion

# Modulo_Saldos:
from modulo_saldos import menu_saldos as menu_saldos

# Modulo_Cambios:
from modulo_cambios import menu_cambios as menu_cambios   


# Menú de acceso
def menu():
    selector_menu = input("""Seleccione la opción deseada: 
                          1_ Vendedoras
                          2_ Pagos
                          3_ Facturacion
                          4_ Saldo Vendedoras
                          5_ Cambios
                          6_ Salir
                          """)
    if selector_menu == "1":
        menu_vendedoras()
        menu()
        
    elif selector_menu == "2":
        menu_pagos()
        menu()
        
    elif selector_menu == "3":
        menu_facturacion()
        menu()
    
    elif selector_menu == "4":
        menu_saldos()
        menu()
    
    elif selector_menu == "5":
        menu_cambios()
        menu()
            
    elif selector_menu == "6":
        print("Felicidades aventurero, que te garue finito")
        
    else:
        print("esa opcion no va, no te hagas el pirulin")
        menu()




#------------------------------------------------------------------

# Inicio del Programa


menu()