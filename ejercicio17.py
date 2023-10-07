'''
Conociendo que los días de la semana son 7; diseñe un algoritmo que a partir del número del día,
indique a cual día corresponde, 1 es lunes, 7 domingo; cualquier número por fuera de este rango
es “error”.
'''

# Paso 1: Solicitar al usuario que ingrese el número del día
dia = int(input("Ingrese un número del día (1-7): "))

# Paso 2: Verificar a qué día corresponde
if dia == 1:
    print("El número", dia, "corresponde a lunes.")
elif dia == 2:
    print("El número", dia, "corresponde a martes.")
elif dia == 3:
    print("El número", dia, "corresponde a miércoles.")
elif dia == 4:
    print("El número", dia, "corresponde a jueves.")
elif dia == 5:
    print("El número", dia, "corresponde a viernes.")
elif dia == 6:
    print("El número", dia, "corresponde a sábado.")
elif dia == 7:
    print("El número", dia, "corresponde a domingo.")
else:
    print("Error. El número debe estar en el rango del 1 al 7.")

