'''
Calcular la nota definitiva de un estudiante de la UDI (primer corte 30%, segundo corte 30% y
tercer corte 40%). Primer corte (quiz 5%, trabajos 5%, parcial 20%), igual para el segundo corte;
en el caso del tercer corte cambiar el parcial de 20 a 30%, indicar también si aprobó o no teniendo
en cuenta que se aprueba con 3.0 sobre 5.0.
'''

#primero pide al usuario las notas y las ingresa en sus respectivas variables 
#Notas del primer corte 
corte1Quiz =float(input("Ingrese la nota del quiz primer corte : "))
corte1Trabajo =float(input("Ingrese la nota del trabajo primer corte : "))
corte1Parcial =float(input("Ingrese la nota del parcial primer corte : "))



#Notas del segundo corte 
corte2Quiz =float(input("Ingrese la nota del quiz segundo corte : "))
corte2Trabajo =float(input("Ingrese la nota del trabajo segundo corte : "))
corte2Parcial =float(input("Ingrese la nota del parcial segundo corte  : "))

#Notas del tercer corte  
corte3Quiz =float(input("Ingrese la nota del quiz tercer corte  : "))
corte3Trabajo =float(input("Ingrese la nota del trabajo tercer corte : "))
corte3Parcial =float(input("Ingrese la nota del parcial tercer corte : "))


#calculo del 30 % de primer corte 

corte1 = (corte1Quiz * 0.05) + (corte1Trabajo* 0.05) + (corte1Parcial*0.20)



#calculo del 30 % de segundo corte 

corte2=(corte2Quiz * 0.05) + (corte2Trabajo* 0.05) + (corte2Parcial*0.20)

#calculo del 40 % de tercer corte 

corte3=(corte3Quiz * 0.05) + (corte3Trabajo* 0.05) + (corte3Parcial*0.30)


#calcular nota definitiva, esta se calcula sumando los porcentajes obtenidos anteriormente 

notaDefinitiva = (corte1 + corte2 + corte3)

#mostrar la nota definitiva 

print("La nota definitiva es : ",notaDefinitiva)

#comprobar si el estudiante aprobó o no 

if notaDefinitiva >= 3.0:
    print("El estudiante aprobo.")
else:
    print("El estudiante no aprobo ")

