
'''
Calcular la nota mínima a obtener en el acumulativo para pasar en definitiva para un estudiante
del COLVIA (trabajo en casa 20%, trabajo en clase 35%, acumulativo 20%, actitudinal 20%,
autoevaluación 5%), informar sobre su estado en base a las categorías (APROBADO, NO
APROBADO, PENDIENTE DE UNA NOTA MÍNIMA DE X). Teniendo en cuenta que se
aprueba con nota de 6.5 sobre 10.

'''

#nota minima para aprobar 

notaAprobar = 6.5

#Pedir las notas actuales del estudiante 

nota1 =float(input("Ingrese la nota del trabajo en Casa  vale el 20%: "))
nota2 =float(input("Ingrese la nota del trabajo en Clase  vale el 35%: "))
nota3 =float(input("Ingrese la nota actitudinal  vale el 20%: "))
nota4 =float(input("Ingrese la nota de autoevaluación vale el 5%: "))

# Calcular las contribuciones de cada componente a la nota actual 

trabajoCasa = (nota1 * 0.20 )
trabajoClase = (nota2 * 0.35)
actitudinal = (nota3* 0.20)
autoevaluación = (nota4* 0.05)

# Calcular la nota actual

notaActual = (trabajoCasa+trabajoClase+actitudinal+autoevaluación)

# Calcular la nota mínima necesaria en el acumulativo

notaMinimoAcumulativo = (notaAprobar-notaActual)

if notaMinimoAcumulativo >= notaAprobar:
    print("el estudiante puede perder el acumulativo y aun asi pasar la materia ")
else:
    print("el estudiante nesecita una nota minima de ",notaMinimoAcumulativo)

    