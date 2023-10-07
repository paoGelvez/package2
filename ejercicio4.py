'''
Algoritmo que a partir de dos números y través de un menú, permita al usuario seleccionar la
acción a realizar entre sumarlos, restarlos, multiplicarlos o dividirlos.
'''

# primero solicitamos al usuario que ingrese 2 numeros 
# INT para que solo acepte numeros enteros 
num1 = int(input("Ingrese el primer número:"))
num2 = int(input("Ingrese el segundo número:"))

#menú de opciones al usuario
print("selecciona la operación que deseas realizar :")
print("1) Suma")
print("2) Resta")
print("3) Multiplicación")
print("4) División")

#Solicitar al usuario que seleccione una opción, esto se guarda en la variable (opcion)

#se guarda como int por que solo debe recibir valores enteros
opcion= int(input("Ingrese el número de la opción deseada : "))

#realiza la operación que selecciono el usuario y muestra el resultado 

if opcion ==1:
    resultado=num1 + num2
    print("El resultado de la suma es:", resultado)
elif opcion ==2:
    resultado= num1 - num2
    print("El resultado de la resta es:", resultado)
elif opcion ==3:
    resultado= num1 * num2
    print("El resultado de la Multiplicación es:", resultado)
elif  opcion ==4:
    if num2 == 0:
       print("no se puede dividir por cero :(")
    else:
      resultado =num1/num2
      print("El resultado de la división es:", resultado)
else:
     print("Opción no válida. Por favor, seleccione una opción válida del menú.")





