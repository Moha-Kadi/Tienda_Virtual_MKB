### LIBRERÍAS ###
#################
import os
# CLASE CLIENTE
from Clase_Cliente import Cliente
# CLASE PRODUCTO
from Clase_Producto import Producto
# CLASE PRODUCTODIGITAL
from Clase_ProductoDigital import ProductoDigital
# CLASE PEDIDO
from Clase_Pedido import Pedido
# CLASE RESEÑA
from Clase_Reseña import Reseña

### FUNCIONES ###
#################

def limpiar_terminal():
    os.system("clear")

def pausar_terminal():
    input("« Pulse Enter para continuar... »")

### PROGRAMA PRINCIPAL ###
##########################

# LISTA PARA ALMACENAR PRODUCTOS
lista_productos = []

# DICCIONARIO CLIENTES DONDE LA CLAVE SEA «ID_CLIENTE»
diccionario_clientes = {}

while True:
    limpiar_terminal()

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
            print("\n*** GESTIONAR PRODUCTOS ***\n")
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
                        print("\n*** AÑADIR PRODUCTO ***\n")

                        try:
                            id_producto = input("Introduzca el ID del producto: ")
                            nombre_producto = input("Introduzca el nombre del producto: ")
                            precio_producto = float(input("Introduzca el precio del producto: "))
                            stock_producto = int(input("Introduzca el stock del producto: "))
                            

                            producto = Producto(id_producto, nombre_producto, precio_producto, stock_producto)

                            lista_productos.append(producto)

                            print("\nProducto agregado correctamente.")
                            print()

                        except Exception as ex:
                            print(f"Se ha producido un Error de tipo: {type(ex)}")

                    case "2":
                        print("\n*** LISTAR PRODUCTO/S ***\n")
                        for product in lista_productos:
                            print(product)
                        print()

                    case "3":
                        print("\n*** ACTUALIZAR STOCK ***\n")
                        
                        try:
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

                            print()
                        except Exception as ex:
                            print(f"Se ha producido un Error de tipo: {type(ex)}")

                    case _:
                        print("ERROR. Introduzca una opción válida.\n")
            
                pausar_terminal()
            print()

        
        ### GESTIONAR PRODUCTOS ###
        case "2":
            print("\n*** GESTIONAR CLIENTES ***\n")
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
                        print("\n*** AÑADIR CLIENTE/S ***\n")

                        id_cliente = input("Introduzca el ID del cliente: ")
                        nombre_cliente = input("Introduzca el nombre del cliente: ")
                        email_cliente = input("Introduzca el email del cliente: ")
                        direccion_cliente = input("Introduzca la dirección del cliente: ")

                        cliente = Cliente(id_cliente,nombre_cliente, email_cliente, direccion_cliente)

                        diccionario_clientes[id_cliente] = cliente 
                        print("\nCliente creado correctamente.")
                        print()

                    case "2":
                        print("\n*** LISTAR CLIENTE/S ***\n")
                        print("CLIENTES:\n")
                        for client in diccionario_clientes.values():
                            print(f"{client}\n")

                        print()
                    case _:
                        print("ERROR. Introduzca una opción válida.\n")
            
                pausar_terminal()
            print()

        
        ### GESTIONAR PEDIDOS ###
        case "3":
            print("\n*** GESTIONAR PEDIDOS ***\n")
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
                        print("\n*** CREAR PEDIDO/S ***\n")

                        id_pedido = input("Introduzca ID de pedido: ")
                        fecha_pedido = input("Introduzca fecha del pedido: ")

                        pedido = Pedido(id_pedido, cliente, fecha_pedido)
                        print("\nPedido creado correctamente")
                        
                        for products in lista_productos:
                            pedido.set_productos(products)
                        print()

                    case "2":
                        print("\n*** LISTAR PEDIDO/S ***\n")
                        print("PEDIDO:\n")
                        
                        print(f" - ID: {id_pedido}\n - Fecha: {fecha_pedido}")
                        print(" - Productos:")
                        for prod in pedido.get_productos():
                            print(f"\t ¬ {prod.get_nombre()}")
                        print()

                    case "3":

                        print("\n*** CALCULAR TOTAL ***\n")
                        pedido.calcular_total()
                        print()
                    case _:
                        print("ERROR. Introduzca una opción válida.\n")
            
                pausar_terminal()
            print()


        ### GESTIONAR RESEÑAS ###
        case "4":
            print("\n*** GESTIONAR RESEÑAS ***\n")
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
                        print("\n*** AÑADIR RESEÑA/S ***\n")

                        try:
                            id_reseña = input("Introduzca ID de reseña: ")
                            comentario_reseña = input("Introduzca el comentario de la reseña: ")
                            puntuacion_reseña = int(input("Introduzca la puntuación de la reseña: "))

                            reseña = Reseña(id_reseña,producto, cliente, comentario_reseña, puntuacion_reseña )
                            print("Reseña añadida correctamente.")    
                            print()

                        except Exception as ex:
                            print(f"Se ha producido un Error de tipo: {type(ex)}")

                    case "2":
                        print("\n*** LISTAR RESEÑA/S ***\n")
                        try:
                            print(reseña)
                            print()
                        except Exception as ex:
                            print(f"Se ha producido un ERROR de tipo {type(ex)}")

                    case _:
                        print("ERROR. Introduzca una opción válida.\n")
            
                pausar_terminal()
            print()
            
        case _:
            print("ERROR. Introduzca una opción válida.\n")

    pausar_terminal()