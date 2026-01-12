###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")
pares = [num for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] if num % 2 == 0]
print (pares)



# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")
numeros = [10, 20, 30, 40, 50]
cont = 0
for num in numeros: 
    cont = cont + num
print (f"la media de la lista numeros es {cont/2}") 

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")
numeros = [15, 5, 25, 10, 20]
mayor = numeros [0]
for num in numeros:
    if num > mayor :
        mayor = num 
print(f"El mayor numero de la lista es {mayor}")

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")
palabras = ["casa", "arbol", "sol", "elefante", "luna"]
new_palabras = [palabra for palabra in palabras if len(palabra) > 4]
print(new_palabras)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")
opcion = input("Ingrese una letra para mostrar por pantalla cuantas palabras de la lista empiezan con esa letra: ").lower( )
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"] 
cont = 0
for palabra in palabras: 
    if palabra.startswith(opcion):
        cont += 1
print(f"La cantidad de palabras dentro de la lista que comienzan con la letra {opcion} son {cont}")
