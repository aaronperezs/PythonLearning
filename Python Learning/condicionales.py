
#nota_alumno=input("Introduce la nota del alumno: ")

def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
		calificacion=7

	return valoracion

#print(evaluacion(int(nota_alumno)))

################################################################

#nota_alumno=int(input("Introduce tu edad: "))

def evaluar(nota):
	if nota_alumno<5:
		print("Insuficiente")
	elif nota_alumno<6:
		print("Suficiente")
	elif nota_alumno<7:
		print("Bien")
	elif nota_alumno<9:
		print("Notable")
	else:
		print("Sobresaliente")

#evaluar(nota_alumno)

################################################################

salario_administrativo=1000
salario_jefe_area=2000
salario_director=3000
salario_presidente=4000

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente and salario_presidente<5000:
	print("Todo funciona correctamente")
else:
	print("Algo falla en esta empresa")

################################################################

print("FOL", "AD", "PSP", "SGE", "EIE")
opcion=input("Escribe la asignatura escogida: ")
asignatura=opcion.lower()

if asignatura in ("fol", "AD", "PSP", "SGE", "EIE"):
	print("Asignatura elegida " + asignatura)
else:
	print("Asignatura no contemplada")