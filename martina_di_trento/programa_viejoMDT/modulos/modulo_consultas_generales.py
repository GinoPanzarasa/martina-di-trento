import sqlite3
import pandas as pd
import matplotlib as plt


def ver_tabla(tabla):
    instruccion = tabla
    conn = sqlite3.connect('martinaDiTrento.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM '{instruccion}'")
    resultado = cursor.fetchall()
    resultado_db = pd.DataFrame(resultado)
    print(resultado_db)
    cursor.close()
    conn.close()


def borrar():
    instruccion = input("Ingrese la instruccion para borrar: ")
    conn = sqlite3.connect('martinaDiTrento.db')
    cursor = conn.cursor()
    cursor.execute(instruccion)
    conn.commit()
    cursor.close()
    conn.close()



