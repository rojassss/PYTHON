#EJERCICIOS 
###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

######
import os 

import os

os.system("clear")

print("Ejercicio 1")
numero1 = int(input("Ingrese el primer numero")) 
numero2 = int(input("Ingrese el segundo numero"))
if numero1 > numero2: 
    print(f"El numero {numero1} es mayor al numero {numero2}")
elif numero2 > numero1: 
    print(f"El numero {numero2} es mayor que {numero1}")
else: 
    print ("Los numeros son iguales")

print("\n-----------\n")

print("Ejercicio 2")
numero1 = int(input("Ingrese el primer numero para poder operar")) 
numero2 = int(input("Ingrese el segundo numero para poder operar"))
signo = input("Ingrese una operacion matematica: \n1.Suma\n2.Resta\n3.Division\n4.Multiplicacion")
if signo == "1": 
    resultado = numero1 + numero2
    print("El resultado es ", resultado )
elif signo == "2": 
    resultado = numero1 - numero2
    print("El resultado es ", resultado)
elif signo == "3": 
    resultado = numero1 / numero2
    print ("El resultado es ", resultado)
elif signo == "4":
    resultado = numero1 * numero2
    print("El resultado es ", resultado)
else: 
    print ("La opcion ingresada no se encuetra en el menu")


print("\n-----------\n")


print("\nEjercicio 3")
año = int(input("Ingrese un año para comprobar si es año bisisesto o no:"))
if año / 4: 
    año_bisisesto = True 
if año_bisisesto: 
    print(f"El año {año} es bisiesto")
else: 
    print(f"El año {año} no es bisiesto")


print("\n-----------\n")


print("\nEjercicio4")
edad = int(input(print("Ingrese una edad para poder categorizarla: ")))

if edad<=2 and edad >=0: 
    print("La edad determina que la persona es un bebe")
elif edad > 2 and edad <= 3 and edad<13:
    print("La edad determina que la persona es un niño")
elif edad > 12 and edad < 18: 
    print ("La edad determina que la persona es un adolescente") 
elif edad > 17 and edad < 65: 
    print("La edad de la persona determina que es un adulto")
else: print("La edad de la persona determina que es un adulto mayor")







