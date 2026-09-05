__author__ = "Andev"
#*Numeros Complejos
print("""Los numeros complejos c caracterizan por tener una parte real y una imaginaria
en python tratamos un numero como complejo desde que se le agrega una parte imaginaria con j o J""")

#?Usaremos la funcion type() para conocer el tipo de dato del dato para mas info: "anexos/system_function.py"
print(type(2j)) #<class 'complex'>
#?aqui tenemos solo la parte imaginaria del numero lo que seria el equivalente a 0+2i 
print(type(-2.2j))#? porsupuesto esta parte imaginaria puede ser decimal o negativa y se expresa asi

print(type(2+3j))#?como normalmente usamos los numeros imaginarios es con una parte real q sea mas q 0 y para eso solo debemos sumarle a un numero real la parte imaginaria
print(type(-3.14+4j))#? y porsupuesto dicha parte real puede ser decimal y negativa

#*Operaciones con numeros complejos
print("""Las operaciones matematicas son las mismas que en los numeros reales solo que se deben tener encuenta la parte imaginaria""")

print(2+2j + 3+3j)#? 5j
print(-4.1j - 7)#? no da (-11.1j) da (-7+-4.1) si no operas en la parte real aunque no este textualmente declarada
print(-4.1j - 7j)#?si da (-11.1j) para operar con la parte imaginaria hay q usar la j o J 

#*División de numeros complejos
print("""La division de numeros complejos es igual a la multiplicación por el conjugado del divisor dividido""")
div=2j+3/(-4.1j-7) #? -0.5689795918367347

#*Exponenciacion de un numero complejo
print("""La exponenciación de numeros complejos es igual a la multiplicación por el exponente""")
expo=2j+3**(-4.1j-7) #? -0.5689795918367347

#*Raiz cuadrada de un numero complejo
print("""La raiz cuadrada de numeros complejos es igual a la multiplicación por el exponente""")
expo=2j+3**(0.5) #? 1.732050807568877

#?Para mas informacion buscar en la documentacion oficial de python