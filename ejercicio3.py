'''
Algoritmo para determinar el mayor entre 4 números; suponga que estos números son de valores
diferentes.
'''

# Solicitar al usuario que ingrese cuatro números

num1 =int(input("Ingrese el numero 1 : "))
num2 =int(input("Ingrese el numero 2 : "))
num3 =int(input("Ingrese el numero 3 : "))
num4 =int(input("Ingrese el numero 4 : "))

'''
 Este ejercicio fue facil era parecido al anterior la diferencia es que en este caso se agrega un elif para hacer otra comparación y en general se crean variables que van a guardar la información que ingrese el usuario y a su vez van a mostrar la pregunta .
'''

# Determinar el número mayor

if num1>num2 and num1 > num3 and num1 > num4:
    print("el numero",num1,"es el mayor de los cuatro numeros")
    # Si num1 es mayor a todos los demás números, imprimir este mensaje.
elif num2>num1 and num2 > num3 and num2 > num4:
    print("el numero",num2,"es el mayor de los cuatro numeros")
    # Si num2 es mayor a todos los demás números, imprimir este mensaje.
elif num3>num1 and num3 > num2 and num3 > num4:
    print("el numero",num3,"es el mayor de los cuatro numeros")
    # Si num3 es mayor a todos los demás números, imprimir este mensaje.
else:
    # Si ninguno de los números anteriores es el mayor, significa que num4 es el mayor.
    print("el numero",num4,"es el mayor de los tres numeros")
    

