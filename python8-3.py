#Pide al usuario un número del 1 al 12 y escribe el número del mes
#correspondiente (1 = enero, 2= febrero,..) usando un array

datos = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

n = int(input("Introduce un número del 1 al 12: "))

if 1 <= n <= 12:
    print(datos[n - 1])
else:
    print("Fuera de rango")