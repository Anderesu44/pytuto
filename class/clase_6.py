__author__ = "Andev"
#*Clase 6*
#*Clases y objetos*

# Una clase es un molde para crear objetos.

# Creamos la clase Persona.
class Persona: #? Usamos la palabra reservada class.
    nombre = "default" # valores por defecto
    edad = 0 # valores por defecto

    #? Usamos el constructor __init__ para inicializar los atributos del objeto.
    #? El constructor es el método que se va a llamar al momento de iniciar la clase.
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #? Métodos: son funciones dentro de una clase.
    #? El primer argumento "self" es el objeto que se está llamando al método.

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")

    def despedirse(self):
        print("Adios")

# Creamos un objeto a partir de la clase Persona.
persona1 = Persona("Andev", 30)

# Llamamos los métodos del objeto.
persona1.saludar()
persona1.despedirse()

# Accedemos a los atributos del objeto.
print(persona1.nombre)
print(persona1.edad)


