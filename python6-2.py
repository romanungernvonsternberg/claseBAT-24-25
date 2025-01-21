#Pide una clave y una contraseña al usuario. No se le dejará proseguir hasta que el código sea admin y la clave 0987.
#Debes utilizar conectores lógicos (and, or, not,...)

clave = input("Introduce la clave: ")
contraseña = input("Introduce la contraseña: ")
while (clave != "0987") or (contraseña != "admin") :
   print("Incorrecto ")
   clave = input("Vuelve a intentarlo, introduce la clave: ")
   contraseña = input("Introduce la contraseña: ")
print("Información correcta")