'''
Elabore el algoritmo para resolver una ecuación de primer grado de la forma ax + b = 0; donde a
y b son los datos, las posibles soluciones son: a <> 0 entonces x = -b/a, a = 0 b <> 0 entonces
"solución imposible", a = 0 b = 0 encantes "solución indeterminada".

'''

# Paso 1: Solicitar al usuario que ingrese los valores de "a" y "b"
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

# Paso 2: Verificar y calcular la solución
if a == 0:
    if b == 0:
        print("Solución indeterminada")
    else:
        print("Solución imposible")
else:
    x = -b / a
    print(f"La solución es x = {x}")

