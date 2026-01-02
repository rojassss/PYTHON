#Variables
#Las variables son espacios de memoria que sirven para almacenar datos con valores volatiles

#asignar una variable
# solo hace falta poner esto 

my_name = "Franco"
print (my_name)

mi_edad = 26 
print(mi_edad)
mi_edad = 23
print(mi_edad)

#puthon es de tipado dinamico
#los valores y los tipos de datos de las variables pueden cambiar en tiempon de ejecuciion
anio_actual = 2025 
print(type(anio_actual))
anio_actual = "dos mil veinticinco"
print(type(anio_actual))

#python es de tipado fuerte: no realiza conversiones de tipos de manera automatica {

# f-string (literal de cadenaa de formato)
print (f"Hola {my_name}, tengo {mi_edad} años")

#NO RECOMENDADA FORMA DE ASIGNAR VARIABLES 

name, age, city = "Franco", 23, "Resistencia"

# Convenciones de nombres de variables 
mi_nombre_de_variable = "ok" # snake_case

MiNombreDeVariable = "ko" # PascalCase
minombredevariable = "ko" # todojunto
mi_nombre_de_variable_123 = "ok"
MI_CONSTANTE = 3.14 # UPPER_CASE para constantes

#Fomas no validas de asignar una variable
#123_variable = "ko"
#mi-varianle = "ko"
#mi variable = "ko"


is_user_logged_in: bool = True #NOTACION: se docuemnta de que la variable es de tipo booleana, aunque en tiempo de ejeccucion se pueda cambiar su tipo de dato dependiendo de tu configuracion de ide 
print(is_user_logged_in)

