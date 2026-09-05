__author__ = "Andev"
#*Clase 2

#*Operadores*
#*Operadores aritméticos:

#*En python usamos operadores aritmeticos para operar on valores tipo numericos*
my_num = 4
my_num_1 = 5
#?Cambia los valores de esas variable y observa como se comporta el programa

print(my_num + my_num_1) #Suma
print(my_num - my_num_1) #Resta
print(my_num * my_num_1) #Multiplicación
print(my_num / my_num_1) #División
print(my_num // my_num_1) #Division entera (sin decimales)
print(my_num % my_num_1) #Modulo (residuo de la división)

#*Operadores de comparación:
#*Los operadores de comparación siempre devuelven un booleano (True o False)*

print(my_num == my_num_1) #Igualdad (=)
print(my_num != my_num_1) #Diferencia (!=)

#*Operadores relacionales:

#*En python usamos operadores relacionales para comparar valores tipo numericos*
print(my_num > my_num_1) #Mayor que (>)
print(my_num < my_num_1) #Menor que (<)
print(my_num >= my_num_1) #Mayor o igual que (>=)
print(my_num <= my_num_1) #Menor o igual que (<=)

#*Operadores lógicos:

#*En python usamos operadores lógicos para combinar valores booleanos*
my_bool = True
my_bool_1 = False

#?And (si ambos son verdaderos, devuelve verdadero)
print(my_bool and my_bool_1) #True && False => False
print(my_bool_1 and my_bool) #False && True => False
print(my_bool and my_bool) #True && True => True
print(my_bool_1 and my_bool_1) #False && False => False

#?Or (si uno de los dos es verdadero, devuelve verdadero)
print(my_bool or my_bool_1) #True || False => True
print(my_bool_1 or my_bool) #False || True => True
print(my_bool or my_bool) #True || True => True
print(my_bool_1 and my_bool_1) #False || False => False

#?Not (invierte el valor del booleano)
print(not my_bool) # => False
print(not my_bool_1) # => True

#*Operadores de asignación:

#*En python usamos operadores de asignación para asignar valores a variables*
my_num = 4 #asigna el valor a la variable tal cual

my_num += 1 #Suma y asignación == my_num = my_num + 1
my_num -= 1 #Resta y asignación == my_num = my_num - 1
my_num *= 2 #Multiplicación y asignación == my_num = my_num * 2
my_num /= 2 #División y asignación == my_num = my_num / 2

#?Funciona con los demas operadores aritmeticos tambien

