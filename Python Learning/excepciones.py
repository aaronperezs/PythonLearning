def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):  
	
	try:
		return num1/num2
	except ZeroDivisionError as e:
		print("No se puede dividir entre 0")
		return "Operacion erronea"

while True:
	try:
		op1=(int(raw_input("Introduce el primer numero: ")))
		
		op2=(int(raw_input("Introduce el segundo numero: ")))  

		break

	except ValueError as va:
		print("Valores no numericos")
	finally:
		print("Siempre se ejecuta el finally, para cerrar lo conexion por ejemplo")

operacion=raw_input("Introduce la operacion a realizar (suma,resta,multiplica,divide): ")


if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operacion no contemplada")

print("Operacion ejecutada. Continuacion de ejecucion del programa ")

#########################################################3

def evaluaEdad(edad):

	if edad<0 or edad>130:
		raise TypeError("No se permiten edades irreales")

	if edad<20:
		return "Eres joven"
	elif edad<40:
		return "Eres flor"
	elif edad<60:
		return "Eres yayo"
	elif edad<80:
		return "Eres fosil"
	else:
		return "Larga vida al rey"


print(evaluaEdad(124))