import sqlite3
import pandas as pd
import matplotlib as plt

def conexion-BBDD():
    try:
        #creando tabla Vendedoras
        conn = sqlite3.connect('martinaDiTrento.db')
        cursor = conn.cursor()
        cursor.execute(f"""
                        CREATE TABLE "Vendedoras" (
                            "CodVendedora"	TEXT,
                            "apellido"	TEXT,
                            "nombre"	TEXT,
                            "credito"   BOOLEAN,
                            PRIMARY KEY("CodVendedora")
                        )
                    """)
        conn.commit()
        
        #creando tabla Cambios
        cursor.execute(f"""
                        CREATE TABLE "Cambios" (
                            "cambioId"	INTEGER,
                            "CodVendedora"	text,
                            "prenda"	text,
                            "talle"	text,
                            "cantidad"	real DEFAULT 0,
                            "precio"	real DEFAULT 0,
                            "descuento"	real DEFAULT 0,
                            "numero_campaña"	INTEGER,
                            PRIMARY KEY("cambioId" AUTOINCREMENT),
                            FOREIGN KEY("CodVendedora") REFERENCES "Vendedoras"("CodVendedora"),
                            FOREIGN KEY("numero_campaña") REFERENCES "Campaña"("numero_campaña")
                        )
                    """)
        conn.commit()

        #creando tabla Pagos
        cursor.execute(f"""
                        CREATE TABLE "Pagos" (
                            "pagosId"	INTEGER,
                            "importe"	REAL DEFAULT 0,
                            "descripcion"	TEXT,
                            "CodVendedora"	TEXT,
                            "destino"	TEXT,
                            "numero_campaña"	INTEGER,
                            PRIMARY KEY("pagosId" AUTOINCREMENT),
                            FOREIGN KEY("CodVendedora") REFERENCES "Vendedoras"("CodVendedora"),
                            FOREIGN KEY("numero_campaña") REFERENCES "Campaña"("numero_campaña")
                        )
                    """)
        conn.commit()

        #creando tabla Facturacion
        cursor.execute(f"""
                        CREATE TABLE "Facturacion" (
                            "facturaId"	INTEGER,
                            "año"	INTEGER,
                            "numero_campaña"	INTEGER,
                            "CodVendedora"	TEXT,
                            "monto_factura"	REAL,
                            PRIMARY KEY("facturaId" AUTOINCREMENT),
                            FOREIGN KEY("CodVendedora") REFERENCES "Vendedoras"("CodVendedora"),
                            FOREIGN KEY("numero_campaña") REFERENCES "Campaña"("numero_campaña")
                        )
                    """)
        conn.commit()

        #creando tabla Campaña
        cursor.execute(f"""
                        CREATE TABLE "Campaña" (
                            "numero_campaña"	INTEGER,
                            "año"	INTEGER,
                            PRIMARY KEY("numero_campaña")
                        )
                    """)
        conn.commit()
        cursor.close()
        conn.close()
        print("La Base de Datos ha sido creada")
    
    except:
        print("La Base de Datos ya existe")


