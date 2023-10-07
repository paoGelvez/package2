'''
Elabore un programa que calcule el salario a cancelar a un trabajador que se le paga por hora.
Considere que las que superen las 40 horas, estas se cancelan al doble, y las horas trabajadas que
superan el valor de 48, estas se cancelan al triple. Ejemplo: valor hora 10000 horas trabajadas
50; el valor a cancelar es 400000+160000+60000=620000.
'''


horas=int(input("ingresa la cantidad de horas trabajadas : "))
valorHora = float(input("ingrese el valor por hora : "))

#primero hacemos el if que pregunte si las horas son menores o iguales a 40 si es asi que guarde dentro de la variable salarioBase multiplicamos horas * valor hora y que lo muestre 
if horas <= 40 :
    salarioBase = horas * valorHora
    print("El salario sin horas extras es: ",salarioBase)
elif horas > 40 and horas <= 48:  #si horas es mayor a 40 y horas es menor a 48 entonces que entre al ciclo se restan el numero de horas que ingreso el usuario con 40 ya que el numero de horas extras que se pagan doble solo son las que estan entre el rango de 41 a 48 horas es decir si el usuario trabajo 43 horas eso se resta con 40 ya que las unicas horas extras que se pagan son las del excedente en ese caso serian 3 todo se guarda dentro de las variables en el caso de la operación del valor de las horas extras se multiplican por el valor de la hora trabajada y el resultado final se multiplica por dos ya que se paga doble 
    horasExtras = horas - 40
    salarioBase = horas * valorHora
   
    horasExtrasValor = horasExtras * valorHora*2
    total = salarioBase  + horasExtrasValor # aca sumamos el salario base que se habia guardado anteriormente con el valor de las horas extras trabajadas lo que me da el total 
    print("El salario con horas extras es: ",total)
else :
    horasExtras = 8 # Las primeras 8 horas extras se pagan al doble
    horasAdicionales = horas - 48 # Horas adicionales al triple
    salarioBase = 40 * valorHora
    salarioHorasExtras = horasExtras * valorHora * 2
    salarioHorasAdicionales = horasAdicionales * valorHora * 3
    total = salarioBase + salarioHorasExtras + salarioHorasAdicionales 
    print("El salario con horas extras y adicionales es : ", total)
