"""
def generaPares(limite):

	num=1

	miLista=[]

	while num<limite:

		miLista.append(num*2)
		num+=1

	return miLista

print(generaPares(10))

############ GENERADOR ################

def generaPares(limite):

	num=1

	while num<limite:
		yield num*2
		num+=1

devuelvePares=generaPares(10)

print(next(devuelvePares))

print(next(devuelvePares))

print(next(devuelvePares))

print(next(devuelvePares))

"""

####################################

def devuelve_ciudades(*ciudades):
	for elemento in ciudades:
		for subElemento in elemento:
			yield subElemento

ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))