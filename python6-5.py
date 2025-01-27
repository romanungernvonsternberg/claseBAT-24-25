#Realiza un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú
#1 - Mostrar la suma de los dos números
#2 - Mostrar la resta de los dos números (el primero menos el segundo)
#3 - Mostrar la multiplicación de los dos números
#4 - Salir del programa
#En caso de introducir una opción inválida, el programa volverá a solicitar otra
#opción hasta que el usuario elija salir.

n1 = int(input("Introduce un número: "))
n2 = int(input("Introduce otro número: "))

print("Selecciona uno de los siguientes modos")
print("1 - Mostrar la suma de los dos números")
print("2 - Mostrar la resta de los dos números")
print("3 - Mostrar la multiplicación de los dos números")
print("4 - Salir del programa")

modo = int(input("Escribe uno de los modos: "))

while modo != 4:
    if modo == 1 :
        print("La suma de", n1, "y", n2, "es", n1+n2)
    
    elif modo == 2 :
        print("La resta de", n1, "y", n2, "es", n1-n2)
    
    elif modo == 3 :
        print("La multiplicación de", n1, "y", n2, "es", n1+n2)
        
    else :
        print("Modo no reconocido")

    modo = int(input("Escribe uno de los modos: "))

print("Adios")


    #if modo == 1:
    #    print("La suma de", n1, "y", n2, "es", n1+n2)
    #modo = int(input("Nuevo modo: "))
    #elif modo == 2:
    #    print("La resta de", n1, "y", n2, "es", n1-n2)
    #modo = int(input("Nuevo modo: "))
    #elif modo == 3:
    #    print("La multiplicación de", n1, "y", n2, "es", n1+n2)