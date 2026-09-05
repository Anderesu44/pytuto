__author__ = "Andev"
#*Clase 3

#Suficiente de declaraciones y operaciones #* Vamos a programar *#

#La programación tiene sus bases en la toma de deciciones 

#para tomar deciciones tenemos condiciones que se evalúan
#*Sentencias*
#*If y Else:
print("¿Cuál es tu edad?")
edad = int(input("introduce tu edad: "))#?int() convierte a entero el valor ingresado por el usuario
#?La función input() es una finción del sistema que imprime el valor que le mandes como 1er argumento y espera en consola un valor del usuario y lo devuelve como str
#?Para mas información puedes consultar la documentación oficial de python o "anexos/system_function.py" 

print("Tu edad es,",edad)
#?usamos un operador de comparacion pq devuelve un bool y el if evalua datos como booleanos

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

switch = True #?Prueba cambiar el valor a False para ver que pasa

if switch:
    print("Ensendido")

#?El if es una estructura condicional, se ejecuta si la condición es verdadera
#?Si no se cumple la condición, se ejecutan las instrucciones del else (si hay uno)
#?Ojo que el else solo se ejecutará si el if es falso

#?La sentencia if se puede anidar
if edad >= 18:
    print("Eres Adulto")
else:
    if edad >= 13:
        print("Eres Adolescente")
    else:
        print("Eres un Niño")
#*Elif*
#?Esto puede ser muy engorroso si c necesitan comprobar muchas condiciones
#?En python existe la sentencia elif q es una forma sensilla de anidar condiciones
#?El elif solo c ejecuta si el if o elif superior es falso y logra evaluar True

if edad >= 18:
    print("Eres Adulto")
elif edad >= 13:
    print("Eres Adolecente")
else:
    print("Eres un niño")

#?==============Ejercisio==============?
#Debes crear un programa que pida al usuario su nombre y su edad y los datos de su acompañante en caso de tenerlo si alguno de los dos es mayor de edad darle la bienvenida en caso contrario denegarle el acceso
#? usa input() para pedirle datos al usuario puedes usar tantos como necesites
#? usa int() para convertir los tipos de datos a numeros si lo necesitas

#*Buena Suerte*#