#Pide al usuario un número entero (por ejemplo, 58) y nos dé todos los
#múltiplos de 7 que hay entre el número 1 y ese número (incluido

numero = int(input("Introduce un numero: "))
print("1")
for numero in range(1, numero,1) :
    if (numero%7)==0 :
        print(numero)