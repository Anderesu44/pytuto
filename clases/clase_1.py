__author__ = "Andev"

#* Bienvenida a la clase 1 del curso*
#* Temas: Variables y Tipos de Datos*

#*Texto
#*En python el tipo de dato para el texxto plano es string o str y existen varias formas de declararlo*

#! Una variable es un espacio en memoria que contiene algun tipo de dato

#*las cadenas de texto se pueden expresar usanco comillas simples >'< o dobles >"< *
print("Cadena de texto con coillas dobles")
print('Cadena de texto con coillas simples')
#*Existen otras formas de declarar cadenas de texto pero las veremos luego*

#* un valor no tiene q ser algo esfimero puedes guardarlo en una variable y operar con el*
my_string = "Cadena de texto" #?Para declarar una variable podemos usar el operador de aignasion
print(my_string) #?Imprimimos la variable en pantalla

#* Guardar Datos nos permite usarlos luego un Ejemplo simle seria con un nombre*

name = "Andev"#? Prueba poner tu nombre y observa como se comporta el programa

print("mi nombre es:",name)

#*Números*
#*En python existen tres tipos de números enteros (int), decimales (float) y complejos (complex)*
my_int = 10 #? Para declarar un número entero podemos usar los numeros tal cual sin comillas
print(my_int)

my_float = 3.14 #? Para declarar un número decimal se usa el punto "." para separar la parte decimal
print(my_float)

my_complex = 2+3j #? Para declarar un número complejo se debe expresar la parte imaginaria mediante una j al final del numero
print(my_complex)#? Los numeros complejos son algo complejos puedes ver el aenxo de la documentacion de python para mas detalles o en "./anexos/complex.py"

#*Operaciones con números*

#*Suma, resta, multiplicación y división*
#? puedes operar con todos los tipos de numeros combinandolos entre ellos sin problemas

#Ejemplo:
num1 = 5 #?usa floats o complexs para probar
num2 = 3

sum_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2

print("Suma:", sum_result)
print("Resta:", sub_result)
print("Multiplicación:", mul_result)
print("División:", div_result)

#*Logica
#* En python el tipo de dato bool es el asignado a la logica*

my_bool = True #? Podemos declarar variables booleanas con los valores true o false
print(my_bool)
my_bool = False
print(my_bool)

#*para operar con bools no usamos operadores aritmeticos usamos operadores logicos*
#Ejemplo:
print(my_bool and True)
print(my_bool or False)

#*Existen otros tipos de datos pero los veras mas adelante en las clases o en "./anexos/types.py"*

#*Reglas de las variables*
#*Crear variables parece simple en python pero tiene un par de reglas importantes
#!Una variable en python debe ser escrita SOLO con carcateres alfanumericos en ingles (a-z,A-Z,0-9) incluyendo el guion bajo "_" y esta nunca puede empezar por un numero
#? Se recomienda que los nombres de las variables sean descriptivos y no contengan espacios o caracteres especiales
#? Una buena practica es evitar usar mayusculas en un nombre, ya que esto puede confundir a otros programadores
#? En python declaramos variables corrientes en snake_case constantes en UPPER_CASE y las Clases en PascalCase
#! El nombre de una Variable en python no puede contener niguna palabra reservada
reserved_words = ['and', 'assert', 'async', 'await', 'break', 'case', 'class', 'continue', 'def', 'del', 'else', 'False', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'match', 'nonlocal', 'not', 'None', 'or', 'pass', 'raise', 'return', 'try', 'True', 'while', 'with', 'yield']
#?Consejo personal: si necesitas usar esas palabras usa un guion bajo atras o alante d esas palabras:
#continue = "dato"#!Error
continue_ = "dato"#*Correcto

#*Fin de la Clase*

