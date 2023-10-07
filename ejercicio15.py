'''
Prepare un algoritmo que permita detectar si un número tiene o no parte fraccionaria.
'''
#  Solicitar al usuario que ingrese un número
numero = float(input("Ingrese un número: "))

#  Calcular la parte decimal del número
# Para hacerlo, puedes restar la parte entera del número al número original.
parte_entera = int(numero)

# Restar la parte entera del número original nos deja con la parte fraccionaria. Si la parte fraccionaria es igual a cero, entonces el número no tiene parte fraccionaria, lo que significa que es un número entero. Por lo tanto, verificamos si la parte fraccionaria es igual a cero para determinar si un número tiene o no parte fraccionaria.

parte_decimal = numero - parte_entera

#  Verificar si la parte decimal es igual a 0
if parte_decimal == 0:
    print("El número ",numero,"no tiene parte fraccionaria, es un número entero.")
else:
    print("El número ",numero, "tiene parte fraccionaria.")

