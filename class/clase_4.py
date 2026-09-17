__author__ = "Andev"
#*Clase 4
#*Bucles y estructuras de datos*
#*while
# El bucle while se considera una sentencia; mientras evalúe un True, va a ejecutar el bloque de código que contenga.
# La condición se evalúa en cada iteración del bucle.
switch = False
while switch:
    print("Inicio de una iteración")
    if input("¿Deseas continuar? (s/n)") == "n":
        switch = False
    print("Fin de una iteración") #? Aunque el valor de la variable es True, no se evalúa hasta que termina el bloque de código.
print("Fuera del bucle\n") #? Al concluir, se ejecuta el siguiente código de forma normal.

#*for
# El for se considera una estructura de control y permite recorrer un conjunto de datos, como listas o tuplas.
# Ejemplo: un bucle que itere sobre cada elemento de la colección.
lista = [1, 2, 3]
for i in lista: #? Durante cada iteración, el valor de la variable declarada en el bucle (en este caso "i") se asigna a un elemento del iterable.
    print("Inicio de una iteración")
    print("Iteración número:", i)
    print("Fin de una iteración")
print("Bucle terminado\n") #? Al concluir, se ejecuta el siguiente código de forma natural.

#*Estructuras de datos*
#*Listas:
#*La estructura de datos más simple de entender es guardar datos uno detrás de otro.
#*Las listas en Python son estructuras de datos indexadas y pueden contener cualquier tipo de dato.
my_int_list = [1, 2, 3, 4, 5]
my_str_list = ["uno", "dos", "tres", "cuatro", "cinco"]
my_list = ["uno", 2, "tres", 4.0, 5+1j, "y cualquier dato que se te ocurra"]
#*Las listas son muy útiles, pero para eso debes entender cómo funcionan.
#* Puedes acceder a cada elemento de la lista usando un índice.
#* El 1er elemento de una lista se encuentra en el índice 0.
print(my_str_list[0]) #? Imprime "uno"
print(my_str_list[1]) #? Imprime "dos"
print(my_int_list[-2]) #? Imprime "3" (el -2 es la posición del penúltimo elemento)
print(my_list)

#*Puedes modificar los elementos de una lista.
print(my_list[0])
my_list[0] = 999 #? Modifica el primer elemento a 999.
print(my_list[0])

#*Y lo más importante: puedes recorrer una lista usando "for".
#*El for se usa para iterar sobre cada elemento de una colección, como una lista en el ejemplo pasado.
my_int_list = [1, 2, 3, 4, 5]
for i in my_int_list:
    print(i)

#*Tuplas:
#*Las tuplas son similares a las listas, pero no se pueden modificar después de ser creadas.
#*Una vez que una tupla es creada, sus elementos no pueden cambiar ni añadirse o eliminarse.
my_tuple = (1, 2, 3) #* Una tupla se declara usando paréntesis "()" en vez de corchetes "[]".
print(my_tuple[0]) #? Imprime "1"
#*Puedes volver inmutable una lista en cualquier momento convirtiéndola en una tupla con el método tuple.
my_tuple = tuple(my_list)
print(my_tuple)
# my_tuple[0] = 999 #! Intentar modificar un elemento de una tupla genera un error.

#! Dato importante: como los paréntesis se usan para dar prioridad a expresiones, no puedes crear una tupla con un solo elemento así: (1)
#! Ya que esto se considera una expresión y no una tupla. Para crear una tupla con un solo elemento, debes hacerlo así: (1,) o tuple([1]).
my_tuple = (1)
print(type(my_tuple)) #? Imprime "int"
my_tuple = (1,)
print(type(my_tuple)) #? Imprime "tuple"

#*Set:
#*Los sets son estructuras de datos no indexadas porque no tienen un orden fijo, por lo tanto no puedes acceder a ellos por índice.
#*Los sets no soportan elementos repetidos. Son útiles para almacenar valores sin preocuparte por el orden o si existen duplicados.
#*Los sets se crean usando llaves "{}" en vez de corchetes "[]".
my_set = {1, 2, 3, 4, 4, 4} #? Un set es una colección de datos que no tiene un orden específico ni duplicados.
print(my_set)
# print(my_set[1]) #! Intentar acceder a los elementos de un set usando índices da error.

#*Diccionarios:
#*Los diccionarios son estructuras de datos indexadas, pero tienen una asociación entre claves y valores.
#*Los diccionarios se crean usando llaves "{}" en vez de corchetes "[]"; separamos claves y valor por ":" y cada relación con ",".
my_dict = {"nombre": "Liz", "edad": "23", "ciudad": "Bogota"}
print(my_dict["nombre"]) #* Para acceder a los elementos de un diccionario usamos su clave entre corchetes "[]".

#! Dato importante: al igual que las tuplas, puede existir conflicto al intentar crear un set vacío así: {}
#! Ya que esto se considera un diccionario y no un set. Para crear un set vacío, debes hacerlo así: set().
my_set = {}

print(type(my_set)) #? Imprime "dict"
