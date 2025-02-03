#Pide al usuario un número del 1 al 12 y escribe el número del mes
#correspondiente (1 = enero, 2= febrero,..) usando un array

datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

n = int(input("Introduce un número del 1 al 12: "))



for i in range(0, 12):
    if datos[i] == n:
        print(datos[i])
