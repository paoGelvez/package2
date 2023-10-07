'''
Indique si dentro de una lista de 10 números, se encuentra el valor de X.
'''

X = int(input("Ingrese el valor que desea buscar: "))

# Definir 10 variables para los números (puedes modificarlas según tus datos)
num1 = 1
num2 = 3
num3 = 5
num4 = 7
num5 = 9
num6 = 2
num7 = 4
num8 = 6
num9 = 8
num10 = 10

# Utilizar condicionales para verificar si X es igual a alguno de los números
if X == num1 or X == num2 or X == num3 or X == num4 or X == num5 or X == num6 or X == num7 or X == num8 or X == num9 or X == num10:
    print(f"{X} se encuentra en la lista.")
else:
    print(f"{X} no se encuentra en la lista.")