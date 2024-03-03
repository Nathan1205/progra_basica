
print("Bienvenido a Maracusa S.A")

#Definir variables a usar 
opcion = ""
usuario = ""
clave = ""


#Iniciar un bucle de menu
while opcion != "5":
    print("1. Informacion sobre Maracusa S.A")
    print("2. Inicio de secion")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Somos una empresa llamada Maracusa S.A")#Hay que agregar info ser creativos segun el documento 

    #Acceso al menu de admin 
    elif opcion == "2":
        while usuario != "admin" or clave !=123:
            usuario = input("Usuario: ")
            clave = input("Clave: ")
            if usuario == "admin" and clave == "123":
                print("Binevenido ")
            else: 
                print("Ingrese un usuario correcto")
               


    elif opcion == "3":
        print("¡Hasta luego!")