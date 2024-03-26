import numpy as np

##Módulo de Productos:


"""
Permitirá a los usuarios registrar, actualizar o eliminar productos del inventario.

Los productos poseen: nombre, código, precio, y cantidad en stock.

Permitirá buscar productos por nombre o código.

Mostrará información como el listado de productos en inventario."""




print("Bienvenido a Maracusa S.A")

#Definir variables a usar 

usuario = ""
clave = ""


#Iniciar un bucle de menu
while True:
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
                def agregarProducto():
                        lista_productos = []
                        nom_producto = input("\nIntroduzca el nombre del producto: ").lower()
                        codigo = str(input("\nIntroduzca el código del producto: ")).lower()
                        precio = str (input("\nIntroduzca el precio del productos: ")).lower()
                        cantidad = str (input("\nIntroduzca la cantidad a añadir: ")).lower()

                        lista_productos.extend([nom_producto,codigo,precio,cantidad])

                        with open ("productos.txt", "a")as file:
                            file.write(",".join(lista_productos))
                            file.write("\r")
                            file.close()                    

                def actualizar_linea():
                    existe = False
                    print("\nDigite el nombre o el codigo del producto a actualizar:")
                    actualizar = input("---> ").lower()
                    with open('productos.txt', 'r') as file:
                        lineas = file.readlines()
                        productos = np.array([linea.strip().split(',') for linea in lineas])
                
                    for linea in productos:
                        if linea[0] == actualizar or linea[1] == actualizar:
                            lineas = np.where(productos == actualizar)[0]
                            while True:
                                print(f"""\nDigite:
                                    \r1) Actualizar Precio
                                    \r2) Actualizar Cantidad""")
                                dato = int(input("---> "))
                                if dato == 1 or dato == 2:
                                    print("Digite el dato nuevo:")
                                    dato_nuevo = input("---> ").lower()
                                if dato == 1:
                                    productos[lineas, -2] = dato_nuevo
                                    break
                                elif dato == 2:
                                    productos[lineas, -1] = dato_nuevo
                                    break
                                else:
                                    print("\nError, Digite un valor correcto")

                        print(f"""\nProducto encontrado con exito.
                                \rAhora los Datos del producto son:
                                \r{",".join(map(str, linea))}""")
                        existe = True
                
                    with open('productos.txt', 'w') as f:
                        for fila in productos:
                            f.write(','.join(fila) + '\n')

                    if existe == False:
                        print("\nProducto no encontrado")
                

                def eliminar_linea():
                    existe = False
                    print("\nDigite el nombre o el codigo del producto a eliminar:")
                    eliminar = input("---> ").lower()

                    with open("productos.txt", 'r') as file:
                        lineas = file.readlines()

                    filtro_linea = []
                    for linea in lineas:
                        datos = linea.strip().split(',')
                        if datos[0] == eliminar or datos[1] == eliminar:
                            existe = True
                            print("\nProducto eliminado con exito")
                            continue   
                        filtro_linea.append(linea)

                    if existe == False:
                        print("\nProducto no encontrado")

                    with open("productos.txt", 'w') as file:
                        file.writelines(filtro_linea)


                def inventario():
                    with open ("productos.txt", "r")as file:
                        lineas = file.readlines()

                    productos = []
                    for linea in lineas:
                        productos.append(linea.strip().split(","))

                    print("\nProductos en inventario por Nombre y Cantidad")
                    for fila in productos:
                        print(f"{fila[0]}|{fila[3]}")


                def buscar_producto():
                    existe = False
                    print("Digite el producto a buscar:")
                    buscar = input("---> ").lower()

                    with open ("productos.txt", "r")as file:
                        lineas = file.readlines()

                    productos = []
                    for linea in lineas:
                        productos.append(linea.strip().split(","))
                    
                    for fila in productos:
                        if fila[0] == buscar or fila[1] == buscar:
                            print(f"""Producto encontrado.
                                \r{",".join(map(str,fila))}""")
                            existe = True
                    
                    if existe == False:
                        print("Producto no encontrado")


                while True:
                    print("""\nDigite un numero del menu:
                        \r1) Agregar
                        \r2) Actualizar
                        \r3) Eliminar
                        \r4) Inventario
                        \r5) Salir""")
                    menu = int(input("---> "))
                    if menu == 5:
                        break

                    elif menu == 1:
                        agregarProducto()

                    elif menu == 2:
                        actualizar_linea()

                    elif menu == 3:
                        eliminar_linea()  
                        
                    elif menu == 4:
                        inventario()

                    else:
                        print("\nError, Digite un valor correcto al menu")
                break
            else: 
                print("Ingrese un usuario correcto")
    #Al presionar 3 termina el programa
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Por favor intente de nuevo con las opciones sugeridas.")