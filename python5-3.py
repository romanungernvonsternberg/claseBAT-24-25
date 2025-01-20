a = int(input("Introduce un año: "))
b = a%4
c = a%100
d = a%400
if  b == 0 and c!=0 or d == 0:
    print("Es bisiesto")
else :
    print("No es bisiesto")

#a%4 = 0 and a%100 != 0 and a%400 = 0 :