__author__ = "Andev"

#* Bienvenida a la clase 1 del curso *
#* Temas: variables y tipos de datos *

#*Texto
#*En Python, el tipo de dato para el texto plano es string o str, y existen varias formas de declararlo.*

#! Una variable es un espacio en memoria que contiene algún tipo de dato.

#*Las cadenas de texto se pueden expresar usando comillas simples >'< o dobles >"<.*
print("Cadena de texto con comillas dobles")
print('Cadena de texto con comillas simples')
#*Existen otras formas de declarar cadenas de texto, pero las veremos luego.*

#*Un valor no tiene que ser algo efímero: puedes guardarlo en una variable y operar con él.*
my_string = "Cadena de texto" #?Para declarar una variable podemos usar el operador de asignación.
print(my_string) #?Imprimimos la variable en pantalla.

#*Guardar datos nos permite usarlos luego. Un ejemplo simple sería con un nombre.*

name = "Andev"#? Prueba poner tu nombre y observa cómo se comporta el programa.

print("mi nombre es:",name)

#*Números*
#*En Python existen tres tipos de números: enteros (int), decimales (float) y complejos (complex).*
my_int = 10 #? Para declarar un número entero podemos usar los números tal cual, sin comillas.
print(my_int)

my_float = 3.14 #? Para declarar un número decimal se usa el punto "." para separar la parte decimal.
print(my_float)

my_complex = 2+3j #? Para declarar un número complejo se debe expresar la parte imaginaria mediante una j al final del número.
print(my_complex)#? Los números complejos son algo complejos. Puedes ver el anexo de la documentación de Python para más detalles o consultar "./anexos/complex.py".

#*Operaciones con números*

#*Suma, resta, multiplicación y división*
#? Puedes operar con todos los tipos de números, combinándolos entre ellos sin problemas.

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

#*Lógica
#* En Python, el tipo de dato bool es el asignado a la lógica.*

my_bool = True #? Podemos declarar variables booleanas con los valores true o false
print(my_bool)
my_bool = False
print(my_bool)

#*Para operar con bools no usamos operadores aritméticos, sino operadores lógicos.*
#Ejemplo:
print(my_bool and True)
print(my_bool or False)

#*Existen otros tipos de datos, pero los verás más adelante en las clases o en "./anexos/types.py".*

#*Reglas de las variables*
#*Crear variables parece simple en python pero tiene un par de reglas importantes
#!Una variable en Python debe escribirse SOLO con caracteres alfanuméricos en inglés (a-z, A-Z, 0-9), incluido el guion bajo "_", y nunca puede empezar por un número.
#? Se recomienda que los nombres de las variables sean descriptivos y no contengan espacios ni caracteres especiales.
#? Una buena práctica es evitar usar mayúsculas en un nombre, ya que esto puede confundir a otros programadores.
#? En Python declaramos las variables corrientes en snake_case, las constantes en UPPER_CASE y las clases en PascalCase.
#! El nombre de una variable en Python no puede contener ninguna palabra reservada.
reserved_words = ['and', 'assert', 'async', 'await', 'break', 'case', 'class', 'continue', 'def', 'del', 'else', 'False', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'match', 'nonlocal', 'not', 'None', 'or', 'pass', 'raise', 'return', 'try', 'True', 'while', 'with', 'yield']
#?Consejo personal: si necesitas usar esas palabras, usa un guion bajo delante o detrás de ellas:
#continue = "dato"#!Error
continue_ = "dato"#*Correcto

#*Fin de la clase.*

