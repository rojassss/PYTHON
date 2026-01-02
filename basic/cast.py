#En este file veremos como se realiza el casteo de tipos de datos
#Transformar un dato de un tipo a otro
#Python no hace converciones de tipos de manera automatica, es de tipado fuerte

print ("Conversion de tipos: ")
print(type(int("100")))
print(int("100") + 2)
print("100" + str(2))
print(type(float("3.14")))
print(int(3.14))

print(int(2.5)) #Devuelve 2, porque elimina todo el contenido que este desoues del punto
print(int(3.5)) #Devulve el par mas cercano a al numero antes del punto, en este caso 4 

print("---------------------------")

print(bool(1))
print(bool(0)) #Unico numero que casteado a bool imrpime como resultado un false
print (bool (-3))

print(bool (""))
print(bool (" ")) #Unico str que casteado a bool imrpime como resultado un false
print("False")

print("---------------------------")

#No funciona 
#print(int("Hola mundo"))