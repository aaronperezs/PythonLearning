import sqlite3

miConexion=sqlite3.connect("/home/aaron/Documentos/Python Learning/BBDD/PrimeraBaseDatos")

miCursor=miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('PELOTA', 15, 'DEPORTES')")

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall()

for producto in variosProductos:
    if(producto[1]<50):
        print(producto)


"""
variosProductos = [

    ("Camiseta",10,"Deportes"),
    ("Short",70,"Moda"),
    ("Juguete",20,"Jugueteria")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)
"""
miConexion.commit()

miConexion.close()