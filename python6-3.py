#Escriba un programa que pregunte una y otra vez si desea continuar con el
#programa, siempre que se conteste exactamente sí (en minúsculas y con tilde).

respuesta = input("¿Deseas seguir en el programa? : ")
while (respuesta == "sí") :
    respuesta = input("¿Deseas seguir en el programa? : ")
print("Adios")