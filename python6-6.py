#Árbol de navidad en Python. Imprime un árbol de navidad formado con *
#haciendo uso del while y de la multiplicación de un entero por una cadena,
#cuyo resultado en Python es replicar la cadena

nivel = int(input("Introduce el nivel del arbol: "))
nivel2 = 1

while nivel2 <= nivel:
    espacio = nivel - nivel2
    asterisco = (2*nivel2) - 1
    print(" "*espacio + "*"*asterisco)
    nivel2 = nivel2 + 1