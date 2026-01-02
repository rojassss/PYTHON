#METODOS

### 


lista = [1, 2, 3, 4, 5] 

#AÑADIR UN ELEMENTO AL FINAL DE LA LISTA
print("Añadir elemento al final de una lista")
lista.append(6)
print(lista) #AHORA TENEMOS LA LISTA ORIGINAL CON EL 6 AGREGADO AL FINAL DE LA LISTA 

#INSERTAR UN ELEMENTO EN UN INDICE CUALQUIERA DE LA LISTA 
print("Insertar un elemento en un indice cualquiera")
lista.insert(1, 0) #Inserta el elemento que le indiquemos en la posicion que respecta al primer parametro 
print(lista) 

#AÑADIR VARIOS ELEMENTOS AL INLA DE LA LISTA 
print("Añadir elementos al final de la lista")
lista.extend([10, 20]) 
print(lista)


### 


#ELIMINAR ELEMENTOS DE LA LISTA 
#NO SE INGRESA EL INDICE DONDE SE ENCUENTRA EL ELEMENTO SINO DIRECTAMENTE EL ELEMENTO
print("Eliminar la primera aparicion de un elemento de una lista") 
lista.remove(1)
print(lista)

#ELIMINAR EL ULTIMO ELEMENTO DE LA LISTA 
lista.pop() #ELIMINA EL ULTIMO ELEMENTO DE LA LISTA (POR DEFECTO) Y TE LO DEVUELVE 
print(lista)

lista.pop(1) #TAMBIEN SIRVE PARA ELIMINAR UN ELEMENTO DE LA LISTA POR SU INDICE
print(lista) 

#ELIMINAR ELEMENTOS A LO BESTIA 
del lista[-1] #ELIMINA EL ULTIMO ELEMENTO DE LA LISTA
print(lista)
lista.clear() #ELIMINAR TODOS LOS ELEMENTOS DE LA LISTA 

#ELIMINAR UN RANGO DE ELEMENTOS 
lista = [10, 20, 30, 40, 50] 
del lista [1:3] 
print(lista) 

#MAS METODOS IMPORTANTES 

#ORDENAR ELEMENTOS DE UNA LISTA MODIFICANDO LA MISMA
print("\nOrdenar elementos de una lista modificando la original")
numeros = [10, 15, 5, 4, 23] 
numeros.sort() #ESTO MODIFICA LA LISTA
print(numeros) 

#ORDENAR LOS ELEMENTOS DE UNA LISTA SIN MODIFICAR LA ORIGINAL
print("\nOrdenar los elementos de una lista sin modificar la lista original") 
numeros = [10, 15, 5, 4, 23]
sorted_numbers = sorted(numeros) 
print(sorted_numbers) #Lista ordenada
print(numeros) #Lista original 

#ORDENAR LISTA DE CADENAS DE TEXTO 
print("\nOrdenar listas de cadenas de texto " ) 
frutas = ["peras", "bananas", "manzana"]
print("ORIGINAL: ", frutas) 
sorted_frutas = sorted(frutas) 
print("LISTA MODIFICADA: ", sorted_frutas) 

#ORDENAR LISTA DE CADENAS DE TEXTOS CUANDO ESTAN PRESENTES LAS MAYUSCULAS 
frutas = ["peras", "manzanas", "bananas", "Peras", "Bananas", "Manzanas"]
print("\nORIGINAL: ", frutas) 
frutas.sort(key=str.lower) 
print("MODIFICADA: ", frutas)


#MAS METODOS UTILES 
print("Mas metodos utiles: ")
animales = ["perro", "gato", "tortuga", "jirafa"] 
print((animales)) #ESTO DEVUELVE LA CANTIDAD DE ELEMENTOS DE LA LISTA 
print("\n", animales.count("perro")) #DEVUELVE LA CANTIDAD DE VECES QUE APARECE UN ELEMENTO EN LA LISTA 
print("\n", "perro" in animales) #DEVUELVE SI EXISTE O NO UN ELEMENTO EN LA LISTA

