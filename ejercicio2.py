'''
Algoritmo para determinar el mayor entre 3 números; suponga que estos números son de valores
diferentes.
'''

'''
 primero se va a preguntar al usuario cierta información es por eso que se  crean 3 variables para guardar la información que se va a preguntar se usa el int para convertir lo que el usuario ingrese en un numero entero y asi no queden guardados como decimales.
'''

num1 =int(input("Ingrese el numero 1 : "))
num2 =int(input("Ingrese el numero 2 : "))
num3 =int(input("Ingrese el numero 3 : "))

'''
 se usa el elif para hacer la comparación en caso de que la primera condición sea falsa.
'''

if num1>num2 and num1 > num3:
    print("el numero",num1,"es el mayor de los tres numeros")
elif num2>num1 and num2 > num3:
    print("el numero",num2,"es el mayor de los tres numeros")
else:
    print("el numero",num3,"es el mayor de los tres numeros")

