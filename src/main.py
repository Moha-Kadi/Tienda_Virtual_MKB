### LIBRERÍAS ###
#################
import os
# Importación de clases desde otros módulos
from Clase_Cliente import Cliente
from Clase_Producto import Producto
from Clase_ProductoDigital import ProductoDigital
from Clase_Pedido import Pedido
from Clase_Reseña import Reseña

### FUNCIONES ###
#################

def limpiar_terminal():
    """Limpia la terminal (solo compatible con UNIX)."""
    os.system("clear")

def pausar_terminal():
    """Pausa la ejecución del programa hasta que el usuario pulse Enter."""
    input("« Pulse Enter para continuar... »")

### PROGRAMA PRINCIPAL ###
##########################

# Lista que almacena los productos creados
lista_productos = []

# Diccionario de clientes con su ID como clave
diccionario_clientes = {}

while True:
    limpiar_terminal()

    # Menú principal
    print("""
+++++++++++++++
      MENÚ
+++++++++++++++
          
0 - SALIR
1 - GESTIONAR PRODUCTOS
2 - GESTIONAR CLIENTES
3 - GESTIONAR PEDIDOS
4 - GESTIONAR RESEÑAS
""")

    opcion = input("Elige una de las opciones: ")
    limpiar_terminal()

    match opcion:
        case "0":
            print("\nQue tengas un buen día\n")
            break

        ### GESTIONAR PRODUCTOS ###
        case "1":
            while True:
                limpiar_terminal()
                print("""
    +++++++++++++++++++++++++++++++
            GESTIONAR PRODUCTOS
    +++++++++++++++++++++++++++++++
                
    0 - SALIR
    1 - AÑADIR PRODUCTO/S
    2 - LISTAR PRODUCTO/S
    3 - ACTUALIZAR STOCK
    """)

                opcion = input("Elige una de las opciones: ")
                limpiar_terminal()

                match opcion:
                    case "0":
                        break

                    case "1":
                        # Añadir producto a la lista
                        try:
                            id_producto = input("Introduzca el ID del producto: ")
                            nombre_producto = input("Introduzca el nombre del producto: ")
                            precio_producto = float(input("Introduzca el precio del producto: "))
                            stock_producto = int(input("Introduzca el stock del producto: "))
                            
                            producto = Producto(id_producto, nombre_producto, precio_producto, stock_producto)
                            lista_productos.append(producto)

                            print("\nProducto agregado correctamente.\n")
                        except Exception as ex:
                            print(f"Se ha producido un Error de tipo: {type(ex)}")

                    case "2":
                        # Mostrar todos los productos
                        print("\n*** LISTAR PRODUCTO/S ***\n")
                        for product in lista_productos:
                            print(product)

                    case "3":
                        # Actualizar stock de un producto
                        try:
                            print("\n*** ACTUALIZAR STOCK ***\n")
                            for product in lista_productos:
                                print(f" - ID: {product.get_id()}")
                            
                            id_product = input("\nIntroduzca ID para actualizar stock: ")
                            for product in lista_productos:
                                if id_product == product.get_id():
                                    nuevo_stock = int(input("Introduzca nuevo Stock: "))
                                    product.set_stock(nuevo_stock)
                                    break
                            else:
                                print("\nERROR. ID no encontrado")

                        except Exception as ex:
                            print(f"Se ha producido un Error de tipo: {type(ex)}")
                    case _:
                        print("ERROR. Introduzca una opción válida.\n")

                pausar_terminal()
            print()

        ### GESTIONAR CLIENTES ###
        case "2":
            while True:
                limpiar_terminal()
                print("""
    +++++++++++++++++++++++++++++++++
            GESTIONAR CLIENTES
    +++++++++++++++++++++++++++++++++
                
    0 - SALIR
    1 - AÑADIR CLIENTE/S
    2 - LISTAR CLIENTE/S
    """)
                opcion = input("Elige una de las opciones: ")
                limpiar_terminal()

                match opcion:
                    case "0":
                        break

                    case "1":
                        # Crear nuevo cliente
                        id_cliente = input("Introduzca el ID del cliente: ")
                        nombre_cliente = input("Introduzca el nombre del cliente: ")
                        email_cliente = input("Introduzca el email del cliente: ")
                        direccion_cliente = input("Introduzca la dirección del cliente: ")

                        cliente = Cliente(id_cliente, nombre_cliente, email_cliente, direccion_cliente)
                        diccionario_clientes[id_cliente] = cliente 
                        print("\nCliente creado correctamente.\n")

                    case "2":
                        # Mostrar todos los clientes
                        print("\n*** LISTAR CLIENTE/S ***\n")
                        for client in diccionario_clientes.values():
                            print(f"{client}\n")
                    case _:
                        print("ERROR. Introduzca una opción válida.\n")

                pausar_terminal()
            print()

        ### GESTIONAR PEDIDOS ###
        case "3":
            while True:
                limpiar_terminal()
                print("""
    +++++++++++++++++++++++++++++++
            GESTIONAR PEDIDOS
    +++++++++++++++++++++++++++++++
                
    0 - SALIR
    1 - CREAR PEDIDO/S
    2 - LISTAR PEDIDO/S
    3 - CALCULAR TOTAL
    """)

                opcion = input("Elige una de las opciones: ")
                limpiar_terminal()

                match opcion:
                    case "0":
                        break

                    case "1":
                        # Crear pedido y añadir todos los productos disponibles
                        id_pedido = input("Introduzca ID de pedido: ")
                        fecha_pedido = input("Introduzca fecha del pedido: ")

                        pedido = Pedido(id_pedido, cliente, fecha_pedido)
                        print("\nPedido creado correctamente\n")
                        
                        for products in lista_productos:
                            pedido.set_productos(products)

                    case "2":
                        # Mostrar información del pedido
                        print("\n*** LISTAR PEDIDO/S ***\n")
                        print(f" - ID: {id_pedido}\n - Fecha: {fecha_pedido}")
                        print(" - Productos:")
                        for prod in pedido.get_productos():
                            print(f"\t ¬ {prod.get_nombre()}")

                    case "3":
                        # Calcular total del pedido
                        print("\n*** CALCULAR TOTAL ***\n")
                        pedido.calcular_total()
                    case _:
                        print("ERROR. Introduzca una opción válida.\n")

                pausar_terminal()
            print()

        ### GESTIONAR RESEÑAS ###
        case "4":
            while True:
                limpiar_terminal()
                print("""
    +++++++++++++++++++++++++++++++
            GESTIONAR RESEÑAS
    +++++++++++++++++++++++++++++++
                
    0 - SALIR
    1 - AÑADIR RESEÑA/S
    2 - LISTAR RESEÑA/S
    """)
                opcion = input("Elige una de las opciones: ")
                limpiar_terminal()

                match opcion:
                    case "0":
                        break

                    case "1":
                        # Añadir reseña a un producto
                        try:
                            id_reseña = input("Introduzca ID de reseña: ")
                            comentario_reseña = input("Introduzca el comentario de la reseña: ")
                            puntuacion_reseña = int(input("Introduzca la puntuación de la reseña: "))

                            reseña = Reseña(id_reseña, producto, cliente, comentario_reseña, puntuacion_reseña)
                            print("Reseña añadida correctamente.\n")
                        except Exception as ex:
                            print(f"Se ha producido un Error de tipo: {type(ex)}")

                    case "2":
                        # Mostrar la reseña
                        try:
                            print("\n*** LISTAR RESEÑA/S ***\n")
                            print(reseña)
                        except Exception as ex:
                            print(f"Se ha producido un ERROR de tipo {type(ex)}")
                    case _:
                        print("ERROR. Introduzca una opción válida.\n")

                pausar_terminal()
            print()

        case _:
            print("ERROR. Introduzca una opción válida.\n")

    pausar_terminal()
