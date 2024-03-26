import datetime

class Cliente:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion

class Producto:
    def __init__(self, nombre, cantidad, precio_unitario):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.subtotal = cantidad * precio_unitario

class Venta:
    def __init__(self, numero_venta, fecha_venta, cliente):
        self.numero_venta = numero_venta
        self.fecha_venta = fecha_venta
        self.cliente = cliente
        self.productos_vendidos = []

    def agregar_producto(self, producto):
        self.productos_vendidos.append(producto)

    def calcular_total_venta(self, descuento=0):
        total = sum(producto.subtotal for producto in self.productos_vendidos)
        total -= total * (descuento / 100)  # Aplicar descuento si hay alguno
        return total
    

# Se ingresan la información de los clientes
nombre_cliente = input("Ingrese el nombre del cliente: ")
identificacion_cliente = input("Digite la identificación del cliente: ")
cliente1 = Cliente(nombre_cliente, identificacion_cliente)


# Acá obtenemos la información de las ventas
numero_venta = int(input("Por favor digite el número de venta: "))
fecha_venta = datetime.date.today()
venta1 = Venta(numero_venta, fecha_venta, cliente1)


# Se ingresan la información de los productos vendidos
while True:
    nombre_producto = input("Por favor, Ingrese el nombre del producto (o 'fin' para finalizar): ")
    if nombre_producto.lower() == 'fin':
        break

    cantidad_producto = int(input("Digite la cantidad vendida: "))
    precio_unitario_producto = float(input("Ingrese el precio unitario del producto: "))

    producto = Producto(nombre_producto, cantidad_producto, precio_unitario_producto)
    venta1.agregar_producto(producto)

# La información del descuento
descuento = float(input("Digite el porcentaje de descuento (0 si no hay descuento): "))

# Reflejamos la información de la venta y productos vendidos
print(f"\nNúmero de Venta: {venta1.numero_venta}")
print(f"Fecha de Venta: {venta1.fecha_venta}")
print(f"Cliente: {venta1.cliente.nombre}")
print("\nProductos Vendidos:")
for producto in venta1.productos_vendidos:
    print(f"  - Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio Unitario: {producto.precio_unitario}, Subtotal: {producto.subtotal}")

total_venta = venta1.calcular_total_venta(descuento)
print(f"\nTotal de Venta (con {descuento}% de descuento): {total_venta}")
