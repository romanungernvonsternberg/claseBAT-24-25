#Pide al usuario 10 números y luego muestra los que son pares

datos = []


for i in range(0, 10):
    datos.append(int(input("Dame un número: ")))

print("Son pares:")

for i in range(0, 10):
    if ((datos[i])%2) == 0 :
        print(datos[i])