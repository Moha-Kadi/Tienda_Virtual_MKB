### LIBRERÍAS ###
from Clase_Cliente import Cliente
from Clase_Producto import Producto

### DEFINICIÓN DE CLASES ###
class Pedido:
    def __init__(self, id:str, cliente, fecha):

        self.__id = id
        self.__cliente = cliente
        self.__productos = []
        self.__fecha = fecha

### GETTERs Y SETTERs ###
#   ATRIBUTO ID
    def get_id(self):
        return self.__id
    def set_id(self, nuevo_id):
        self.__id = nuevo_id
#   ATRIBUTO CLIENTE
    def get_cliente(self):
        return self.__cliente
    def set_cliente(self, nuevo_cliente):
        self.__cliente = nuevo_cliente
#   ATRIBUTO PRODUCTOS
    def get_productos(self):
        return self.__productos
    def set_productos(self, nuevo_producto):
        self.__productos.append(nuevo_producto)
#   ATRIBUTO FECHA
    def get_fecha(self):
        return self.__fecha
    def set_fecha(self, nueva_fecha):
        self.__fecha = nueva_fecha

    ### MÉTODOS DE LA CLASE PEDIDO ###

    def productos_cliente(self):
        c = ""
        for product in self.get_productos():
            c += f"{product.get_nombre()}, "
        return c.rstrip(", ")

    def __str__(self):
        return f" - ID: {self.get_id()}\n - Cliente: {self.get_cliente().get_nombre()}\n - Productos: {self.get_productos()}\n - Fecha: {self.get_fecha()}"
    
    def agregar_producto(self, producto):
        self.get_productos().append(producto)

    def calcular_total(self):
        total = 0
        for product in self.get_productos():
            total += product.get_precio() * product.get_stock()

        print(f"El Total de la compra es de: {total}€")


if __name__ == "__main__": 
    ### INSTANCIAS DE CLASE ###
    producto1 = Producto("P001", "Chabola", 30.20, 20)
    producto2 = Producto("P002", "Luces led", 0.70, 200)
    producto3 = Producto("P003", "Cámara",1990.73, 1)
    cliente = Cliente("C001", "Pepe Luis", "pepeluis2019@gmail.com", "C/ Cerro Mataero' Chabola 4")
    pedido = Pedido("P001", cliente, "14/03/2025")

    ### USO ###
    pedido.agregar_producto(producto1)
    pedido.agregar_producto(producto2)
    pedido.agregar_producto(producto3)

    print(pedido)
    pedido.calcular_total()

