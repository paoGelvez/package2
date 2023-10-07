#Algoritmo para calcular la media aritmética, el rango de 10 números positivos. El rango
#corresponde a la diferencia entre el número mayor y el número menor de una lista de valores.


# se arranca en uno por que es pensado en el usuario
i =1
suma = 0
print ("Ingrese el valor ",i,": ",end="")
num = int(input())


#esto es un acumulador que permite ir sumando las operaciones
#los acumuladores no tiene un valor fijo por que el usuario es el que ingresa la información y se suma
suma = suma + num


#esto es un contador y va de uno en uno
i = i +1


#en la variable mayor se guarda lo que se ingreso como el menor y a todo se le asigna el num


mayor = menor = num


# el end es una palabra reservada para poder alterar su estructura normal
print ("Ingrese el valor ",i,": ",end="")
num = int(input())
suma = suma + num
i = i +1
if num > mayor:
    mayor=num
if num < menor:
    menor = num


print ("Ingrese el valor ",i,": ",end="")
num = int(input())
suma = suma + num
i = i +1
if num > mayor:
    mayor=num
if num < menor:
    menor = num


print ("Ingrese el valor ",i,": ",end="")
num = int(input())
suma = suma + num
i = i +1
if num > mayor:
    mayor=num
if num < menor:
    menor = num


print ("Ingrese el valor ",i,": ",end="")
num = int(input())
suma = suma + num
i = i +1
if num > mayor:
    mayor=num
if num < menor:
    menor = num


print ("Ingrese el valor ",i,": ",end="")
num = int(input())
suma = suma + num
i = i +1
if num > mayor:
    mayor=num
if num < menor:
    menor = num


print ("Ingrese el valor ",i,": ",end="")
num = int(input())
suma = suma + num
i = i +1
if num > mayor:
    mayor=num
if num < menor:
    menor = num


print ("Ingrese el valor ",i,": ",end="")
num = int(input())
suma = suma + num
i = i +1
if num > mayor:
    mayor=num
if num < menor:
    menor = num


print ("Ingrese el valor ",i,": ",end="")
num = int(input())
suma = suma + num
i = i +1
if num > mayor:
    mayor=num
if num < menor:
    menor = num


print ("Ingrese el valor ",i,": ",end="")
num = int(input())
suma = suma + num
i = i +1
if num > mayor:
    mayor=num
if num < menor:
    menor = num




print("El promedio es : ",(suma/10))
print("El rango es ",(mayor-menor))