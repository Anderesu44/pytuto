__author__ = "Andev"
#*Clase 4
#*Bucles y Estructuras de datos
#*while
# el bucle while se considera una sentencia y mientras evalue un True va a ejecutar el bloque de codigo que contenga
# la condicion c evalue en cada iteracion del bucle
switch = False
while switch:
    print("Inicio de una iteracion")
    if input("Deseas continuar? (s/n)") == "n":
        switch = False
    print("Fin de una iteracion")#? aunque el valor d la variable es True no la evalua si no hasta q c acaba el bloque de codigo
print("Fuera del Bucle\n")#?AL concluir se ejecuta el siguiente codigo de forma normal

#*for
# el for se considera una estructura de control y permite recorrer un conjunto de datos, como listas o tuplas,
# Ejemplo utilizando un bucle que itere sobre cada elemento en la colección.
lista = [1, 2, 3]
for i in lista:#?Durante cada iteracion el valor de la variable declarada en el bucle (en este caso "i") se asigna a un elemento del iterable)
    print("Inicio de una iteracion")
    print("Iteracion numero:", i)
    print("Fin de una iteracion")
print("Bucle terminado\n") #?Al concluir se ejecuta el siguiente codigo de forma natural

#*Estructuras de datos*
#*Listas:
#*La estructura de datos mas simple de entender simplemente puedes guardar datos uno atras del otro
#*Las listas en python son estructuras de datos indexadas y pueden contener cualquier tipo de dato
my_int_list = [1,2,3,4,5]
my_str_list = ["uno","dos","tres","cuatro","cinco"]
my_list = ["uno",2,"tres",4.0,5+1j,"y cualquier dato que se te ocurra"]
#*las son muy utiles pero para eso debes enender como funionan
#* Puedes acceder a cada elemento d la lista usando un indice
#* El 1er elemento d una lista c encuentra en el indice 0
print(my_str_list[0]) #?Imprime "uno"
print(my_str_list[1]) #?Imprime "dos"
print(my_int_list[-2]) #?Imprime "3" (el -2 es la posicion del penultimo elemento)
print(my_list)

#*Puedes modificar los elementos de una lista
print(my_list[0])
my_list[0] = 999 #?Modifica el primer elemento a 999
print(my_list[0])

#*Y o mas importante puedes recorer una lista usando "for":
#*El for se usa para iterar sobre cada elemento de una colección, como una lista en el ejemplo pasado
my_int_list = [1,2,3,4,5]
for i in my_int_list:
    print(i)

#*Tuplas: 
#*Las tuplas son similares a las listas pero no se pueden modificar después de ser creadas
#*Una vez que una tupla es creada, sus elementos no pueden cambiar ni añadirse o eliminarse.
my_tuple = (1,2,3) #*una tupla se declara usando parentesis "()" en vez de corchetes "[]"
print(my_tuple[0]) #?Imprime "1"
#*Puedes volver inmutable una lista en cualquier momento convirtiendola en una tupla con el metodo tuple
my_tuple = tuple(my_list)
print(my_tuple)
# my_tuple[0] = 999 #!Intentar modificar un elemento de una tupla genera un error

#!Dato importante como los parentesis se usan para dar prioridad a expresiones no puedes creare una tupla con un solo elemento asi : (1)
#!Ya que esto es considerado una expresion y no una tupla. Para crear una tupla con un solo elemento, debes hacerlo así: (1,) o tuple([1])
my_tuple = (1)
print(type(my_tuple))#?Imprime "int"
my_tuple = (1,)
print(type(my_tuple))#?Imprime "tuple"

#*Set: 
#*Los sets son estructuras de datos no indexadas porque no tienen un orden fijo, por lo tanto no puedes acceder
#*Los sets no soportan repetidos elementos. Los sets son útiles para almacenar valores sin preocuparte por el orden o si existen duplicados.
#*Los sets se crean usando llaves "{}" en vez de corchetes "[]"
my_set = {1,2,3,4,4,4} #?Un set es una colección de datos que no tiene un orden específico ni duplicados
print(my_set)
# print(my_set[1])#!Intentar acceder a los elementos de un set usando inidces da error

#*Diccionarios: 
#*Los diccionarios son estructuras de datos indexadas poro tienen una asociación entre claves y valores.
#*Los diccionarios se crean usando llaves "{}" en vez de corchetes "[]" pero separamos claves y valor por ":" y cada relacion con ","
my_dict = {"nombre":"Liz","edad":"23", "ciudad":"Bogota"}
print(my_dict["nombre"])#*Para acceder a los elementos de un diccionario usamos su clave entre corchetes "[]"

#!Dato importante al igual q las tuplas puede existir conflictos al intentar crear un set vacio asi : {}
#!Ya que esto es considerado una dictionario y no un set. Para crear un set vacio, debes hacerlo así: set()
my_set = {}

print(type(my_set)) #?Imprime "dict"
