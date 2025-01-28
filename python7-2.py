#Pide al usuario un número entero (por ejemplo, 5) y muestra la tabla de
#multiplicar de ese número( Ejemplo: “5 x 1 = 5” hasta “5 x 10 = 50”)

numero = int(input("Introdue un numero: "))
numero1 = 1
for numero1 in range(1, 11) :
    print(numero, "x", numero1,"=", numero*numero1)