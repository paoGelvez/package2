'''
Para un número comprendido entre 1 y 9999; elaborar un algoritmo que indique la cantidad de
dígitos que lo componen.

'''

# Solicitar al usuario que ingrese un número entre 1 y 9999
numero = int(input("Ingrese un número entre 1 y 9999: "))

# Verificar si el número está en el rango válido
if 1 <= numero <= 9999:
    #  Inicializar una variable para contar los dígitos
    cantidadDigitos = 0

    #  Verificar si el número tiene 4 dígitos
    if numero >= 1000:
        cantidadDigitos = 4
    #  Verificar si el número tiene 3 dígitos
    elif numero >= 100:
        cantidadDigitos = 3
    # Paso 6: Verificar si el número tiene 2 dígitos
    elif numero >= 10:
        cantidadDigitos = 2
    elif numero <= 9:
        cantidadDigitos = 1
    #  Si no tiene 4, 3 o 2 dígitos, debe tener 1 dígito

    #  Mostrar la cantidad de dígitos
    print("El número tiene", cantidadDigitos,"dígito.")
else:
    print("Número fuera del rango válido (1-9999).")
