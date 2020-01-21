import pickle

class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Persona nueva, de nombre ", self.nombre)
    
    def __str__(self):
        return "{}{}{}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:

    personas=[]

    def __init__(self):
        listaDePersonas=open("ficheroExterno","ab+")
        listaDePersonas.seek(0)

        try:
            self.personas=pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero está vacío")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)


    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)
    
    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas=open("ficheroExterno","wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarInfoFicheroExterno(self):
        print("La info del fichero externo: ")
        for p in self.personas:
            print(p)


miLista=ListaPersonas()

p=Persona("Sandra", "Femenino",39)
miLista.agregarPersonas(p)
p=Persona("Antonio", "Masculino",19)
miLista.agregarPersonas(p)
p=Persona("Ana", "Femenino",29)
miLista.agregarPersonas(p)

miLista.mostrarPersonas()

