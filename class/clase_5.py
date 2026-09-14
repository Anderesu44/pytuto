__author__ = "Andev"
#*Clase 5
#* Funciones

#*En Python existe la palabra clave def para definir funciones. Una función es un bloque de código que realiza una tarea específica
def saludar(): #~ignora este comentario  #pyright: ignore[reportRedeclaration] 
    print("Hola\n")

saludar() #?Al ejecutar esta línea se llama a la funcion para ejecutar una funcion tenemos q llamarla usando ()
#*Argumentos

#*Los argumentos son los valores que se pasan a las funciones cuando se invocan. Los parámetros son las variables declaradas en la función.
def saludar(nombre):#asi pedimos un argumento en la funcion #~ignora este comentario  #pyright: ignore[reportRedeclaration] 
    print("Hola",nombre,"\n")#esta linea depende del valor que le pasemos como argumento a la funcion

saludar("Liz")#le pasamos un valor a la funcion dentro de los ()
saludar("Juan") #le pasamos otro valor a la funcion y c comporta distinto pero es el mismo bloque de codigo

"Las funcines son bloques de codigo algo distinto a bucles y condicionales"
"Pues estan ademas de poder llamarse en cualquier momento pueden devolver un valor"
"Ahora explico mejor:"

def saludar(nombre):
    lista_negra = ["Mario","Diaz Canel","Pam"] #has una lista de gente q te caia mal
    if nombre in lista_negra:# cuando usamos in sobre una lista busca el valor en cada uno d ss elementos si esta devuelve True y False si no
        return False#devolvemos false pq nos cae mal
        print("nada")#despues de un retur la funcion se acaba y devuelve el valor nada despues se ejecuta
    print("hola",nombre)#imprime el saludo
    return True

gente_a_saludar = ["Juan","Paco","Pam","Maria"]
for nombre in gente_a_saludar: #la variable nombre ocupa cada lugar d la lista en cada iteracion
    retorno = saludar(nombre)#enviamos el valor d la variable como argumento de la funcion
    if not retorno: #con "not" invertimos el valor de la variable bool si es true devolvemos False y viceversa
        print("Me cae mal") #si no se saluda al nombre que estamos iterando entonces imprime esto
