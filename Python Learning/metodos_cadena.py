"""
edad=input("Introduce tu edad: ")

while(edad.isdigit()==False):
    print("Por favor, introduce un valor numerico: ")
    edad=input("Introduce tu edad: ")

if(int(edad)<18):
    print("No puede pasar")
else:
    print("Puede pasar")
"""
################## EJERCICIO CORREO ELECTRONICO #################

email=input("Introduzca un email: ")
valido=False

if(email.endswith("@") or email.startswith("@")):
    valido=False
else:
    numero=email.count('@')
    if(numero<2):
        valido=True

print(valido)

