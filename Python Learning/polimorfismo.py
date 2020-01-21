class Coche():

    def desplazamiento(self):
        print("Me desplazo con 4 ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo con 2 ruedas")

class Camion():

    def desplazamiento(self):
        print("Me desplazo con 6 ruedas")


def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


miVehiculo=Camion()
miVehiculo2=Coche()
miVehiculo3=Moto()

desplazamientoVehiculo(miVehiculo)
desplazamientoVehiculo(miVehiculo2)
desplazamientoVehiculo(miVehiculo3)

"""
miVehiculo=Moto()

miVehiculo.desplazamiento()


miVehiculo2=Coche()

miVehiculo2.desplazamiento()


miVehiculo3=Camion()

miVehiculo3.desplazamiento()
""" 