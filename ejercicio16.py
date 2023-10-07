'''
A partir de un año capturado por la entrada, determinar si este es o no bisiesto. Considerando
que un año es bisiesto si es divisible por 4 y no es divisible por 100 o es divisible por 400.
'''

bisiesto = float(input("Ingrese un año para saber si es bisiesto o no : "))

if (bisiesto % 4 == 0 and bisiesto % 100 != 0) or (bisiesto % 400 == 0):
    print("El año",bisiesto ,"es bisiesto.")
else:
    print("El año", bisiesto," no es bisiesto.")
