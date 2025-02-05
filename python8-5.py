#Crea un programa que pida al usuario 12 números enteros, los guarde en un
#array y luego le pregunte de forma repetitiva qué número quiere buscar. Le
#responderá si dicho número estaba o no entre los datos que se habían
#introducido inicialmente. Dejará de repetirse cuando se introduzca el número 0


datos = []


for i in range(0, 12):
    datos.append(int(input("Dame un número entero, no 0: ")))

n = int(input("¿Qué numero quieres buscar?..."))

while n != 0:
    if datos[i] == n :
        print("Ese número esta en los datos")
        n = int(input("¿Qué numero quieres buscar?..."))
    elif datos[i] == n > 12 and n< 0:
        print("No está en los datos")
        n = int(input("¿Qué numero quieres buscar?..."))
