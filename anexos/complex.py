__author__ = "Andev"
#*Números complejos*

print("""Los números complejos se caracterizan por tener una parte real y una imaginaria.
En Python tratamos un número como complejo desde que se le agrega una parte imaginaria con j o J.""")

#?Usaremos la función type() para conocer el tipo de dato; para más información: "anexos/system_function.py".
print(type(2j)) #<class 'complex'>
#?Aquí tenemos solo la parte imaginaria del número, lo que sería el equivalente a 0+2i.
print(type(-2.2j))#? Por supuesto, esta parte imaginaria puede ser decimal o negativa, y se expresa así.

print(type(2+3j))#? Como normalmente usamos los números imaginarios es con una parte real mayor que 0, solo debemos sumarle a un número real la parte imaginaria.
print(type(-3.14+4j))#? Y, por supuesto, dicha parte real puede ser decimal y negativa.

#*Operaciones con números complejos*
print("""Las operaciones matemáticas son las mismas que en los números reales, solo que se debe tener en cuenta la parte imaginaria.""")

print(2+2j + 3+3j)#? 5j
print(-4.1j - 7)#? No da (-11.1j), sino (-7+-4.1), porque no operas en la parte real aunque no esté textualmente declarada.
print(-4.1j - 7j)#? Sí da (-11.1j). Para operar con la parte imaginaria hay que usar la j o J.

#*División de números complejos*
print("""La división de números complejos es igual a la multiplicación por el conjugado del divisor, dividida entre el divisor.""")
div=2j+3/(-4.1j-7) #? -0.5689795918367347

#*Exponenciación de un número complejo*
print("""La exponenciación de números complejos es igual a la multiplicación por el exponente.""")
expo=2j+3**(-4.1j-7) #? -0.5689795918367347

#*Raíz cuadrada de un número complejo*
print("""La raíz cuadrada de números complejos es igual a la potenciación con exponente 0.5.""")
expo=2j+3**(0.5) #? 1.732050807568877

#?Para más información, consulta la documentación oficial de Python.