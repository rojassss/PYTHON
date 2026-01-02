#Secuencias mutables de elementos que pueden contener elementos de diferentes tipos

#Creacion de listas 
print("\nCrear lista: ")
lista1 = [1, 2, 3, 4, 5] #lista de enteros 
lista2 = ["manzanas", "peras", "platanos"] #lista de cadenas
lista3 = [1, "hola", 3.14, True] #lista de tipos mixtos 


lista_vacia = []
lista_de_listas = [[1,2], [3, 4]]
matriz = [[1,2], [3, 4], [5, 6]] 

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia) 
print(lista_de_listas)
print(matriz)


#Acceso a elemetos por idndice
print("\nAcceso a elementos por indice") 
print(lista2[0])
print(lista2[1]) 
print(lista2[-1]) 
print(lista2[2])

print(lista_de_listas[0][1]) #Manera de recorrer matrices, primera posicion representa a la lista dentro de la matriz, la segunda posicionn representa a el indice del elemento al qe querramos hacer referencia 
print("\n")

#Slicing (rebanado) de listas 

###
#EJEMPLO 1
print("EJEMPLO 1")
lista1 = [1, 2, 3, 4, 5]
print(lista1[1:4])  #IMPRIME LOS ELEMENTOS DESDE EL PRIMER PARAMETRO HASTA UN ELEMENTO ANTERIOR AL SEGUNDO ELEMENTO DE LA LISTA
print ("\n")

#EJEMPLO 2 
print("EJEMPLO 2")
print(lista1[:3]) #IMRPIME LOS PRIMEROS ELEMENTOS DE LA LISTA HASTA UN ELEMENTO ANTES DEL SEGUNDO PARAMETRO INGRESADO 
print ("\n")

#EJEMPLO 3 
print("EJEMPLO 3")
print(lista1[2:]) #IMPRIME LOS ELEMENTOS DESDE EL INDICE 2 HASTA EL FINAL DE LA LISTA 
print ("\n")

#EJEMPLO 4 
print("EJEMPLO 4")
print(lista1[:]) #REALIZA UNA COPIA DE LA LISTA, IMPRIMIENDO TODOS LOS ELEMENTOS DE ESTA LISTA 
print ("\n")

# MAS RECURSOS DEL SLICING 

lista1 = [1, 2, 3, 4, 5, 6, 7, 8] 
#print(lista1[desde : hasta : paso])

print(lista1[::2]) #IMPRIME LOS ELEMENTOS DE LA LISTA PERO DE 2 EN 2

print(lista1[::-1]) #DEVUELVE LOS ELEMENTOS DE LA LISTA PERO DESDE EL FINAL HASTA EL INICIO
print ("\n")
### 

#MODIFICAR ELEMENTOS DE UNA LISTA 
print("Modificar elementos de una lista")
lista1[0] = 20 #MODIFICA EL PRIMER ELEMENTO DE LA LISTA, ANTES ERA 1 AHORA ES 20
print(lista1)
print ("\n")
#SI INTENTO INGRESAR A UNA POSICION NO EXISTENTE PYTHON SE VA A QUEJAR, POR EJEMPLO QUERER INGRESAR A AL POSICION 110 EN UNA LISTA DE APENAS 10 ELEMENTOS 

###

#AÑADIR ELEMENTOS A LA LISTA 
print("Añadir elementos a una lista\n")
#FORMA LARGA Y MENOS EFICIENTE
lista1 = lista1 + [10, 20, 30]
print (lista1)

#FORMA CORTA Y MAS EFICIENTE 
lista1 += [40, 50, 60]
print(lista1)

#RECUPERAR LA LONGITUD DE UNA LISTA 
print("\n")
print("RECUPERRA LA LONGITUD DE UNA LISTA: ")
lista = [1, 2, 3, 4] 
print("La longitud de la lista: ", len(lista))

