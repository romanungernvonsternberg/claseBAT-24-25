"""Alejandro Moreno Alcaraz 5/2/2025
Ejercicio 1
Escribe un programa que imprima todos los números pares entre dos
números que se le pidan al usuario."""


n1 = int(input("Introduce un número: "))
n2 =int(input("introduce otro número: "))
for n1 in range(n1, (n2+1)):
    if (n1%2)==0 :
        print(n1)
