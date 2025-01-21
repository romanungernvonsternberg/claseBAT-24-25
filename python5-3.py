# Escribe un programa que pida un año y que escriba si es bisiesto o no.
#Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100
#no lo son, aunque los múltiplos de 400 sí.



a = int(input("Introduce un año: "))
b = a%4
c = a%100
d = a%400
if  b == 0 and c!=0 or d == 0:
    print("Es bisiesto")
else :
    print("No es bisiesto")

#a%4 = 0 and a%100 != 0 and a%400 = 0 :