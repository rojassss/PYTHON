###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

print("EJERICIO 1")
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
print(mensaje[7:])

print("\n") 

print("EJERCICIO 2") 
numeros = [10, 20, 30, 40, 50]
numero1 = numeros[0]
numero2 = numeros[4]
numeros[0] = numero2
numeros[4] = numero1
print(numeros)

print("\n")  

print("EJERCICIO 3") 
pan = ["pan arriba"]
ingredientes = ["jamon", "queso", "tomate"]
pan_abajo = ["pan abajo"]
sandwich = [pan, ingredientes, pan_abajo]
print(sandwich[0],"\n",sandwich[1],"\n",sandwich[2])

print("\n") 
print("EJERCICIO 4") 
lista = [1, 2, 3]
lista_duplicada = lista + lista
print(lista_duplicada)
 
print("\n")
print("EJERCICIO 5") 
lista = [10, 20, 30, 40, 50] 
centro  = lista[len(lista) // 2: len(lista) // 2  +1]
print(centro[0])

print("\n") 
print("EJERCICO 6") 
lista = [1, 2, 3, 4, 5, 6]
print(lista[2::-1] + lista[3:])

