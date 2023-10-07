'''
En la escuela “Winny Poo”, se desean convertir notas alfabéticas A, B, C, D ,E y F a
calificaciones de tipo numéricas 10, 9, 8, 7, 6 y 5 respectivamente.
'''

#  Solicitar al usuario que ingrese una nota alfabética (A, B, C, D, E o F)
notaAlfabetica = input("Ingrese una nota alfabética (A, B, C, D, E o F): ")

# Realizar la conversión utilizando estructuras condicionales
if notaAlfabetica == 'A':
    calificacionNumerica = 10
elif notaAlfabetica == 'B':
    calificacionNumerica = 9
elif notaAlfabetica == 'C':
    calificacionNumerica = 8
elif notaAlfabetica == 'D':
    calificacionNumerica = 7
elif notaAlfabetica == 'E':
    calificacionNumerica = 6
elif notaAlfabetica == 'F':
    calificacionNumerica = 5
else:
    print("Nota alfabética no válida. Por favor, ingrese una nota válida (A, B, C, D, E o F).")
    #Al asignar None, estamos estableciendo un valor nulo o sin definir en la variable.
    calificacionNumerica = None

# Mostrar la calificación numérica si es válida
if calificacionNumerica is not None:
    print("La calificación numérica equivalente para ", calificacionNumerica,"es", calificacionNumerica)
