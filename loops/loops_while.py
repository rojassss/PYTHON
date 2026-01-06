###
#BUCLE WHILE 
#BUCLE CON CONDICION DE INGRESO 

print("\nBucle while") 

#Bucle con una simple condicion 
contador = 0 
while contador < 5: 
    print(contador) 
    contador += 1 #importante incrementar el contador para no ingresar en un bi¿ucle infinito 

#Utilizando la palabra break para romper el bucle 
    while True: 
        print(contador) 
        contador+=1
        if contador == 5: 
         break #se sale del bucle
###
        
#CONTINUE, lo que hace es saltar esa iteracion en concreto 
#y continuar con el bucle 
print("\nBucle con continue ")
contador = 0 
while contador < 10: 
   contador+= 1

   if contador % 2 == 0: 
      continue 
    
print (contador)


###

#WHILE TIENE ELSE
#ESTA CONDICION CUANDO SE EJECUTA 
print("\nBucle while con else: ")
contador = 5 
while contador <= 5: 
   print(contador) 
   contador += 1
else: 
   print("El bucle ha terminado") 
#ESTE EJEMPLO SIRVE PARA CUANDO NECESITAS SABER EN QUE MOMENTO EL BUCLE TERMINA PORQUE LA CONDICION PASÓ A SER FALSA 
#SI DENTRO DE EL BLOQUE WHILE UTILIZAMOS UN BREAK, NUNCA ENTRARA AL ELSE 
   

### 
   
#EJERCICO PRACTICO 
#PEDIRLE AL USUARIO UN NUMERO ENTERO QUE TIENE QUE SER POSITIVO PARA PODER SALIR DEL BUCLE 
print("\nEJERCICIO PRACTICO")
numero = -1 
while numero < 0 : 
   numero = int(input("Usuario quiero que ingreses un numero entero positivo (numero mayor o igual que 0)\n"))
   if numero < 0: 
      print("El numero que ingreses debe ser positivo, intenta otra vez")
print(f"El numero ingresado es {numero}, saliste del bucle")


### 

#EJERCICIO PRACTICO CON TRY-EXCEPT 
print("\nEJERCICIO PRACTICO CON TRY EXCEPT: ") 
numero = -1 
while numero < 0: 
    try: 
      numero = int (input("Usuario quiero que u¿ingreses un numero entero positivo: "))
    except: 
      print("El valor que ingreses debe ser un numero") 
    if numero < 0: 
      print("El numero que ingreses debe ser positivo, intenta otra vez")
print(f"El numero ingresado es {numero}, saliste del bucle")
#BASICAMENTE EL TRY DICE "INTENTA CORRER LA SIGUEINTE LINEA DE CODIGO", DE NO SER POSIBLE EXCEPT DICE: "ENTONCES CORRE LA SIGUEUINTE LINEA DE CODIGO" 
#ESTO LO QUE HACE ES TRATAR ERRORES SIN QUE EL USUARIO PUEDE VER QUE EN REALIDAD EL PROGRAMA EXPLOTO 