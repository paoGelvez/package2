'''
Elaborar un algoritmo para establecer si 5 números ingresados por teclado corresponden a una
secuencia incremental.
'''

# Solicitar al usuario que ingrese 5 números
print("Ingrese 5 números:")
numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))
numero3 = int(input("Número 3: "))
numero4 = int(input("Número 4: "))
numero5 = int(input("Número 5: "))

# Verificar si los números forman una secuencia incremental
if numero1 < numero2 < numero3 < numero4 < numero5:
    print("Los números forman una secuencia incremental.")
else:
    print("Los números no forman una secuencia incremental.")

