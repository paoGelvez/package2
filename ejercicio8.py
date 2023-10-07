'''
Algoritmo que a partir de 4 números indique sí existen dos números dentro de los cuatro que al
sumarlos de igual a uno de ellos; adicionalmente cuantos cumplen con esta regla. Ejemplo: 2 4
3 2, respuesta SI 1.
'''
#solicitar al usuario que ingrese los 4 números 

num1=int(input("Ingrese el primer número : "))
num2=int(input("Ingrese el segundo número : "))
num3=int(input("Ingrese el tercer número : "))
num4=int(input("Ingrese el cuarto número : "))

#Inicializar una variable para contar cuantos cumplen con las regla
contador = 0

#Comprobar todas las combinaciones de pares de números
#Utilizamos cuatro bucles anidados para recorrer todas las combinaciones posibles 

if (num1 + num2 == num3):
    contador += 1
    print("si hay ",contador,"cuando se suman los dos numeros",num1,"+",num2,"=",num3)
if (num1 + num2 == num4):
    contador = contador + 1
    print( "si hay ",contador,"cuando se suman los dos numeros",  num1, "+", num2, "=",num4)
if (num1 + num3 == num2):
    contador = contador + 1
    print( "si hay ",contador,"cuando se suman los dos numeros", num1, "+", num3, "=",num2)
if (num1 + num3 == num4):
    contador = contador + 1
    print( "si hay ",contador,"cuando se suman los dos numeros",  num1, "+", num3, "=",num4)
if (num1 + num4 == num2):
    contador = contador + 1
    print( "si hay ",contador,"cuando se suman los dos numeros", num1, "+", num4, "=",num2)
if (num1 + num4 == num3):
    contador = contador + 1
    print( "si hay ",contador,"cuando se suman los dos numeros", num1, "+", num4, "=",num3)
if (num2 + num3 == num4) :
    contador = contador + 1
    print( "si hay ",contador,"cuando se suman los dos numeros", num2, "+", num3, "=",num4)

if (num2 + num3 == num1) :
    contador = contador + 1
    print( "si hay ",contador,"cuando se suman los dos numeros", num2, "+", num3, "=",num1)

if (num2 + num4 == num3) :
    contador = contador + 1
    print( "si hay ",contador,"cuando se suman los dos numeros",  num2, "+", num4, "=",num3)

if (num2 + num4 == num1) :
    contador = contador + 1
    print( "si hay ",contador,"cuando se suman los dos numeros", num2, "+", num4, "=",num1)

if (num3 + num4 == num2) :
    contador = contador + 1
    print( "si hay ",contador,"cuando se suman los dos numeros",  num3, "+", num4, "=",num2)

if (num3 + num4 == num1) :
    contador = contador + 1
    print( "si hay ",contador,"cuando se suman los dos numeros",  num3, "+", num4, "=",num1)

if (contador == 0) :
    print( "No hay ningún caso.")