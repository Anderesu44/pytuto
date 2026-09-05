__author__ = "Andev"
#*Clase 3
#*Bucles y Estructuras de datos
#*while
# el bucle while se considera una sentencia y mientras evalue un True va a ejecutar el bloque de codigo que contenga
# la condicion c evalue en cada iteracion del bucle
switch = True
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
print("Bucle terminado") #?Al concluir se ejecuta el siguiente codigo de forma natural

