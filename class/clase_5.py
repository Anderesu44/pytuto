__author__ = "Andev"
#*Clase 5*
#*Funciones*

#*En Python existe la palabra clave def para definir funciones. Una función es un bloque de código que realiza una tarea específica.
def saludar(): #~ignora este comentario  #pyright: ignore[reportRedeclaration]
    print("Hola\n")

saludar() #? Al ejecutar esta línea se llama a la función; para ejecutar una función necesitamos llamarla usando paréntesis "()".
#*Argumentos

#*Los argumentos son los valores que se pasan a las funciones cuando se invocan. Los parámetros son las variables declaradas en la función.
def saludar(nombre): # asi pedimos un argumento en la función #~ignora este comentario  #pyright: ignore[reportRedeclaration]
    print("Hola", nombre, "\n") # esta línea depende del valor que le pasemos como argumento a la función.

saludar("Liz") # le pasamos un valor a la función dentro de los ()
saludar("Juan") # le pasamos otro valor a la función y se comporta distinto, pero es el mismo bloque de código.

"Las funciones son bloques de código, algo distinto a bucles y condicionales."
"Además, pueden llamarse en cualquier momento y devolver un valor."
"Ahora explico mejor:"

def saludar(nombre):
    lista_negra = ["Mario", "Diaz Canel", "Pam"] # haz una lista de gente que te caiga mal XD
    if nombre in lista_negra: # cuando usamos "in" sobre una lista, busca el valor en cada uno de sus elementos; si está devuelve "True" o "False".
        return False # devolvemos False porque nos cae mal
        print("nada") # después de un return, la función acaba y devuelve el valor; nada después se ejecuta.
    print("hola", nombre) # imprime el saludo si el nombre no está en la lista negra, porque el return no se ejecuta y el código sigue.
    return True

gente_a_saludar = ["Juan", "Paco", "Pam", "Maria"]
for nombre in gente_a_saludar: # la variable nombre ocupa cada lugar de la lista en cada iteración.
    retorno = saludar(nombre) # enviamos el valor de la variable como argumento de la función y en la variable retorno recibimos un dato de parte de la función.
    if not retorno: # con "not" invertimos el valor de la variable bool; si es true devolvemos False y viceversa.
        print("Me cae mal") # si no se saluda al nombre que estamos iterando, entonces imprime esto.
