# sentencia condicional, permite bifurcar el codigo dependiendo de condiciones 

import os
os.system("clear")


print("Sentecia simple condicional\n")

edad = 18 #La variable edad tiene un valor necesario para poder hacer uso efectivo del if y del print
if edad >= 18: 
    print ("Eres mayor de edad\n")

edad = 15 #En este caso la variable edad es modificada para que su valor sea menor que 18 e imrpima el mensaje
if edad <= 18: 
    print("Eres menor de edad")

print("Sentencia condicional con else") 
edad = 15 
if edad >= 18: 
    print ("Eres mayor de edad\n")
else: 
    print("Eres menor de edad")


print("Sentencia condicional con elif")
nota = 7
if nota >= 9: 
    print("Sobresaliente")
elif nota >= 7: 
    print("Notable") 
elif nota == 6: 
    print("Aprobado")
else: print("Desaprobado")

print("\nCondiciones multiples: ")
edad = 26 
tiene_carnet = True 
if edad >= 18 and tiene_carnet: 
    print("Puedes conducir")
else: 
    print("No puede conducir")

#Probando el uso del or 
print("PROBANDO LA FUNCIONALIDAD DEL OR\n")
if edad >= 18 or tiene_carnet: 
    print("Puedes conducir")
else: 
    print("Paga coima")

#Probando el uso de la negacion 
print("\nProbando el uso de la negacion")
es_fin_de_semana = False 
if not es_fin_de_semana: 
    print("Hay que programar")


#If anidados 
print ("\nProbando los if anidados")
edad = 20 
tiene_dinero = True 


#Este bloque de codigo nom es recomendado, por lo general, puede ser mejorado
if edad >= 18: 
    if tiene_dinero: 
        print("Puedes ir a la discoteca")
    else: 
        print("Quedate en casa")
else: 
    print("No puedes ingresar a la discoteca")

#ESTE ES UN EJEMPLO DE COMO HCAERLLO MAS FACIL Y MAS LEGIBLE 
if edad < 18: 
    print("No puedes ingresar a la discoteca")
elif tiene_dinero:
    print("Puedes ir a la discoteca")
else: 
    print("Quedate en casa")
#Si tiene mas de 18 no ingresa en el primer if, pasa al elif, si tiene dinero puede ir, si no tiene dinero mejor que se quede en casa
    


    