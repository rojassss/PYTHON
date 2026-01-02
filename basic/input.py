# La funcion input sirve para obtener datos ingresados por el usuario a traves de teclado 

print("Como te llamas?") 
nombre = input()

print(f"Hola {nombre} encantado de conocerte")

#TAMBIN FUNCIONA 

edad = input("Cuantos años tienes? \n")
print (f"Tienes {edad} años")


#Para obtener multiples valores a la vez 
pais, ciudad = input ("En que pais vives?\n").split() 

print(f"Vives en {ciudad}, {pais}")
