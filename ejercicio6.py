#De 5 números ingresados por el usuario, establecer cuántos son positivos, negativos y neutros (0).

#primero creamos contadores y los inicializamos en cero 
positivos = 0 
negativos = 0
neutros =0

# lo que hacemos en este caso es que cuando un numero entre al ciclo va a estar en uno y mientras entre se va ir sumando uno en el contador que inicialmente estaba en cero para al final poder entregar  la cantidad de numeros positivos negativos o neutros 

num1=int(input("ingresa el numero 1 : "))
num2=int(input("ingresa el numero 2 : "))
num3=int(input("ingresa el numero 3 : "))
num4=int(input("ingresa el numero 4 : "))
num5=int(input("ingresa el numero 5 : "))

if num1 > 0 :
    positivos += 1
elif num1 < 0 :
    negativos += 1
else:
    neutros += 1

if num2 > 0 :
    positivos += 1
elif num2 < 0 :
    negativos += 1
else:
    neutros += 1

if num3 > 0 :
    positivos += 1
elif num3 < 0 :
    negativos += 1
else:
    neutros += 1

if num4 > 0 :
    positivos += 1
elif num4 < 0 :
    negativos += 1
else:
    neutros += 1

if num5 > 0 :
    positivos += 1
elif num5 < 0 :
    negativos += 1
else:
    neutros += 1


print("la cantidad de numeros positivos ingresados son :",positivos)
print("la cantidad de numeros negativos ingresados son :",negativos)
print("la cantidad de numeros neutros ingresados son :",neutros)