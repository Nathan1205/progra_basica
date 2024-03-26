
print("Bienvenido a Maracusa S.A")

#Definir variables a usar 
opcion = ""
usuario = ""
clave = ""


#Iniciar un bucle de menu
while opcion != "5":
    print("1. Informacion sobre Maracusa S.A")
    print("2. Inicio de sesion")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("""Maracacusa S.A es una empresa enfocada en la venta y reparación de computadoras y sus perifericos.\nFundación:11/04/2000?\nFundador:Tony Stark\nNuestro lema:"Potencia tu juego, equipa tu victoria.""")

    #Acceso al menu de admin 
    elif opcion == "2":
        while usuario != "admin" or clave !=123:
            usuario = input("Usuario: ")
            clave = input("Clave: ")
            if usuario == "admin" and clave == "123":
                print("Binevenido ")
            else: 
                print("Ingrese un usuario correcto")
               

    #Al presionar 3 termina el programa
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Por favor intente de nuevo con las opciones sugeridas.")
