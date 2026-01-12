### 
#BUCLES FOR 

#PERMITE EJECUTAR UN BLOQUE DE CODIGO REPETIDAMENTE MIENTRAS ITERA UN ITERABLE O UNA LISTA 

print("\nBucle for: ")

#iterar una lista 
print("Iterando una lista: ")
frutas = ["manzana", "peras", "mandarina"] 
for fruta in frutas: 
    print (fruta)

#iterar cualquier cosa que sea iterable 
print("\nIterando cualquier cosa que pueda ser iterable: ")
cadena = "franco" 
for caracter in cadena : 
    print (caracter)


#enumerate() 
print("\nUtilizado enumerate()")
frutas = ["manzana", "peras", "mandarina"] 
for index, fruta in enumerate(frutas):
    print(f"El indice es {index} y la fruta es {fruta}")


#BUCLES ANIDADOS 
print("\nBucles anidados") 
letras = ["A", "B", "C"]
numeros = [1, 2, 3]
for letra in letras:
    for numero in numeros: 
        print(f"{letra}{numero} ")


##Uso de BREAK 
print("\nUso de break: ")
animales = ["perro", "gato", "jirafa", "loro", "halcon", "raton"]  

for idx, animal in enumerate(animales):
    print(animal)
    if animal ==  "loro": 
        print(f"El loro esta escondido en el indice {idx}")
        break


#Uso del CONTINUE 
print("\nUso de continue: ")
animales = ["perro", "gato", "jirafa", "loro", "halcon", "raton"]  

for idx, animal in enumerate(animales):
    if animal ==  "loro": 
        continue   #Lo que pasa con esta linea de codigo es que el continue ignora la iteracion donde animal == loro entonces no lo imprime por pantalla y continua con las demas iteraciones 
    print(animal)

#Comprension de listas - list comprehension
print("\nEspacio para comprension de listas: ")

print("\nObtener una lista con los elementos en mayuscula a partir de otra lista: ")
animales = ["perro", "gato", "jirafa", "loro", "halcon", "raton"]  
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus) 

### 

#Devolver los numeros pares de una lista de numeros con comprension de listas 
print("\nNumeros pares de una lista con comprension de listas")
pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(pares)