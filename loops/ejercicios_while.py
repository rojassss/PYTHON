###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.


# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.


# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".


# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.


# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.


######################### 


#Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("EJERCICIO 1: ")
numero = 10 
while numero > 0: 
    print(numero) 
    numero-=1 

print("\n")

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("EJERCICIO 2: ")
contador = 0 
numero = 0
while numero < 20: 
    numero +=2 
    contador = contador + numero
print(contador)

print("\n") 

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("EJERCICIO 3: ")
numero = int(input("Ingrese un numero entero positivo: "))

factorial = 1
contador = numero

while contador > 1:
    factorial *= contador
    contador -= 1

print(f"El factorial de {numero} es {factorial}")

print ("\n")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("EJERCICIO 4: ")
contraseña = ""
while len(contraseña) < 8: 
    print("La contraseña debe tener al menos 8 caracteres para ser valida")
    contraseña = input("Ingrese una contraseña: \n") 
    
  
else: 
    print("CONTRASEÑA GUARDADA CORRECTAMENTE")

print("\n") 

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("EJERCICIO 5: ")
numero = int(input("Introduce un numero y te  dire su tabal de multiplicar del 1 al 10: "))
contador = 1
while contador <= 10 : 
    print (f"{contador}:  {numero} * {contador} = {numero*contador}")
    contador +=1