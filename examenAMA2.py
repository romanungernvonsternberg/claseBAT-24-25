"""Alejandro Moreno Alcaraz 5/2/2025 
Ejercicio 2
Escribe un programa que pida al usuario un número y muestre su raíz
cuadrada. Si el número introducido es negativo, se lo volverá a pedir
tantas veces como sea necesario hasta que introduzca uno positivo."""
 


n = int(input("Introduce un número: "))

while n < 0:
    n = int(input("Introduce un número positivo: "))
n1 = n**(1/2)
print("La raiz cuadrada de", n, "es", n1)