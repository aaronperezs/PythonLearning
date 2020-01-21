from io import open
"""
archivo_texto=open("archivo.txt","w")

frase="Estupendo dia para estudiar Python \nDia de Reyes"

archivo_texto.write(frase)
archivo_texto.close()
"""
#############################################
"""
archivo_texto=open("archivo.txt","r")

lineas_texto=archivo_texto.readlines()

archivo_texto.close()

print(lineas_texto[0])
"""
#############################################
"""
archivo_texto=open("archivo.txt","a")

archivo_texto.write("\nSiempre es buena ocasion para estudiar Python")

archivo_texto.close()
"""
#############################################
"""
archivo_texto=open("archivo.txt","r+") # Lectura y escritura

print(archivo_texto.read())

archivo_texto.seek(0)

print(archivo_texto.read(11))

archivo_texto.seek(len(archivo_texto.read())/2)

archivo_texto.seek(len(archivo_texto.readline()))

print(archivo_texto.read())

archivo_texto.seek(0)
archivo_texto.write("Comienzo del texto")

archivo_texto.close()
"""

############################################

archivo_texto=open("archivo.txt","r+") # Lectura y escritura

lista_texto=archivo_texto.readlines()

lista_texto[1]="Esta linea ha sido incluido desde el exterior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()

