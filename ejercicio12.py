'''
Presentar en orden (0 ascendente/ 1 descendente) 3 números reales ingresados por teclado.
'''
num1 =float(input("Ingrese el primer número real : "))
num2 =float(input("Ingrese el segundo número real : "))
num3 =float(input("Ingrese el tercer número real : "))

#pedir al usuario en que orden quiere ver los numeros 

orden = int(input("Ingrese 0 para orden ascendente o 1 para orden descendente: "))

'''
Si orden es igual a 0 (ascendente):
Compara los números num1 y num2. Si num1 es mayor que num2, se intercambian.
Luego, compara los números num2 y num3. Si num2 es mayor que num3, se intercambian.
Finalmente, se vuelve a comparar num1 y num2, y si num1 es mayor que num2, se intercambian nuevamente.

'''

if orden == 0: #ascendente
   if num1 > num2:
      num1,num2 = num2,num1
   if num2 > num3:
       num2, num3 = num3, num2
   if num1  > num2:
      num1, num2 = num2, num1
elif orden == 1:  # Descendente
    if num1 < num2:
        num1, num2 = num2, num1
    if num2 < num3:
        num2, num3 = num3, num2
    if num1 < num2:
        num1, num2 = num2, num1
else: 
     print("Opción no válida. Por favor, ingrese 0 para ascendente o 1 para descendente.")


# Imprimir los números en el orden correspondiente
print("Números en orden:")
print(num1)
print(num2)
print(num3)
