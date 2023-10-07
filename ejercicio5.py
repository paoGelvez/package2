'''
Algoritmo que permita tomar las 3 notas obtenidas por cada uno de los dos estudiantes y
determinar quién tiene la nota definitiva mayor y quien la menor.
'''
# primero se solicitan  las notas de los dos estudiantes
print("Ingrese las notas del primer estudiante: ")
nota1Estudiante1=float(input("Nota 1 : "))
nota2Estudiante1=float(input("Nota 2 : "))
nota3Estudiante1=float(input("Nota 3 : "))

print("Ingrese las notas del segundo estudiante: ")
nota1Estudiante2=float(input("Nota 1 : "))
nota2Estudiante2=float(input("Nota 2 : "))
nota3Estudiante2=float(input("Nota 3 : "))

# segundo se Calcula la nota promedio de cada estudiante

promedioEstudiante1 = (nota1Estudiante1+nota2Estudiante1+nota3Estudiante1)/3

promedioEstudiante2 = (nota1Estudiante2+nota2Estudiante2+nota3Estudiante2)/3

# Determinar quién tiene la nota definitiva mayor y quién la menor

if promedioEstudiante1 > promedioEstudiante2:
     print("El primer estudiante tiene la nota definitiva mayor:", promedioEstudiante1)
     print("El segundo estudiante tiene la nota definitiva menor:", promedioEstudiante2)
elif promedioEstudiante2 > promedioEstudiante1:
     print("El segundo estudiante tiene la nota definitiva mayor:", promedioEstudiante2)
     print("El primer estudiante tiene la nota definitiva menor:", promedioEstudiante1)
else :
     print("Ambos estudiantes tienen la misma nota ")