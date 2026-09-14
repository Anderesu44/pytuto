__author__ = "Andev"
#*Clase 3

#Suficiente de declaraciones y operaciones. #* ¡Vamos a programar! *#

#La programación tiene sus bases en la toma de decisiones.

#Para tomar decisiones tenemos condiciones que se evalúan.
#*Sentencias*
#*If y else:*
print("¿Cuál es tu edad?")
edad = int(input("Introduce tu edad: "))#?int() convierte a entero el valor ingresado por el usuario.
#?La función input() es una función del sistema que imprime el valor que le mandes como primer argumento, espera en consola un valor del usuario y lo devuelve como str.
#?Para más información puedes consultar la documentación oficial de Python o "anexos/system_function.py".

print("Tu edad es,",edad)
#?Usamos un operador de comparación porque devuelve un bool y el if evalúa datos como booleanos.

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

switch = True #?Prueba cambiar el valor a False para ver qué pasa.

if switch:
    print("Encendido")

#?El if es una estructura condicional: se ejecuta si la condición es verdadera.
#?Si no se cumple la condición, se ejecutan las instrucciones del else (si hay uno).
#?Ojo: el else solo se ejecutará si el if es falso.

#?La sentencia if se puede anidar.
if edad >= 18:
    print("Eres Adulto")
else:
    if edad >= 13:
        print("Eres Adolescente")
    else:
        print("Eres un Niño")
#*Elif*
#?Esto puede ser muy engorroso si se necesitan comprobar muchas condiciones.
#?En Python existe la sentencia elif, que es una forma sencilla de anidar condiciones.
#?El elif solo se ejecuta si el if o elif superior es falso y logra evaluar True.

if edad >= 18:
    print("Eres Adulto")
elif edad >= 13:
    print("Eres Adolescente")
else:
    print("Eres un niño")

#?==============Ejercicio==============?
#Debes crear un programa que pida al usuario su nombre y su edad, y los datos de su acompañante en caso de tenerlo. Si alguno de los dos es mayor de edad, dale la bienvenida; en caso contrario, deniega el acceso.
#? Usa input() para pedirle datos al usuario; puedes usar tantos como necesites.
#? Usa int() para convertir los tipos de datos a números si lo necesitas.

#*¡Buena suerte!*#