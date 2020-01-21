import math

"""
@@@@@@@@@@@@@@@@@@@ FOR @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

for i in [1,2,3]:
	print(i)

for i in ["Primavera", "Verano", "Otonio", "Invierno"]:
	print(i)

##########################################################

email=False

miEmail=raw_input("Email: ")

for i in miEmail:
	if(i=="@"):
		email=True

if email:
	print("Email correcto")
else:
	print("Email no correcto")
    
##########################################################

for i in range(5,10,3):
	print(i)

##########################################################

@@@@@@@@@@@@@@@@ WHILE @@@@@@@@@@@@@@@@@@@@@@@

variable=raw_input("True(T) or False(F)?")

while variable.upper()=="F":
	print("Hola")
	break

i=1

while i<=10:
	print("Ejecucion " + str(i))
	i+=1

####################################################3

print("Programa de calculo de raiz cuadrada")
numero=int(raw_input("Introduce un numero"))

intentos=0

while numero<0:
	print("No se puede hallar la raiz de un numero negativo")

	if intentos==2:
		print("Has consumido demasiados intentos. El programa ha finalizado")
		break

	numero=int(raw_input("Introduce un numero"))
	if numero<0:
		intentos+=1

if intentos<2:
	solucion=math.sqrt(numero)
	print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))


######################################################################

for letra in "Python":

	if letra=="h":
		continue

	print("Letra " + letra)
"""

#######################################################################

nombre="Pildoras Informaticas"
nombrefinal=""

for letra in nombre:
	if letra==" ":
		continue
	nombrefinal+=letra

print(nombrefinal)

##########################################################

email=raw_input("Introduce tu email")

for i in email:
	if i =="@":
		arroba=True
		break
else:

	arroba=False
print(arroba)