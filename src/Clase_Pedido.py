### LIBRERÍAS ###
from Clase_Cliente import Cliente  # Importa la clase Cliente desde un módulo externo.
from Clase_Producto import Producto  # Importa la clase Producto desde un módulo externo.

### DEFINICIÓN DE CLASES ###
class Pedido:
    """
    Clase que representa un pedido realizado por un cliente,
    incluyendo los productos, la fecha y otros detalles.
    """

    def __init__(self, id: str, cliente, fecha):
        """
        Constructor de la clase Pedido.

        :param id: Identificador único del pedido.
        :param cliente: Objeto de tipo Cliente que realiza el pedido.
        :param fecha: Fecha en la que se realiza el pedido.
        """
        self.__id = id
        self.__cliente = cliente
        self.__productos = []  # Lista para almacenar productos.
        self.__fecha = fecha

    ### GETTERs Y SETTERs ###

    # ATRIBUTO ID
    def get_id(self):
        """Devuelve el ID del pedido."""
        return self.__id

    def set_id(self, nuevo_id):
        """Establece un nuevo ID para el pedido."""
        self.__id = nuevo_id

    # ATRIBUTO CLIENTE
    def get_cliente(self):
        """Devuelve el cliente asociado al pedido."""
        return self.__cliente

    def set_cliente(self, nuevo_cliente):
        """Establece un nuevo cliente para el pedido."""
        self.__cliente = nuevo_cliente

    # ATRIBUTO PRODUCTOS
    def get_productos(self):
        """Devuelve la lista de productos en el pedido."""
        return self.__productos

    def set_productos(self, nuevo_producto):
        """
        Agrega un nuevo producto a la lista de productos del pedido.

        :param nuevo_producto: Objeto de tipo Producto a agregar.
        """
        self.__productos.append(nuevo_producto)

    # ATRIBUTO FECHA
    def get_fecha(self):
        """Devuelve la fecha del pedido."""
        return self.__fecha

    def set_fecha(self, nueva_fecha):
        """Establece una nueva fecha para el pedido."""
        self.__fecha = nueva_fecha

    ### MÉTODOS DE LA CLASE PEDIDO ###

    def productos_cliente(self):
        """
        Devuelve una cadena con los nombres de todos los productos del pedido,
        separados por comas.
        """
        c = ""
        for product in self.get_productos():
            c += f"{product.get_nombre()}, "
        return c.rstrip(", ")

    def __str__(self):
        """
        Devuelve una representación legible del pedido, incluyendo cliente,
        productos y fecha.
        """
        return (
            f" - ID: {self.get_id()}\n"
            f" - Cliente: {self.get_cliente().get_nombre()}\n"
            f" - Productos: {self.get_productos()}\n"
            f" - Fecha: {self.get_fecha()}"
        )

    def agregar_producto(self, producto):
        """
        Agrega un producto al pedido.

        :param producto: Objeto de tipo Producto.
        """
        self.get_productos().append(producto)

    def calcular_total(self):
        """
        Calcula y muestra el total del pedido, basado en el precio y stock
        de cada producto.
        """
        total = 0
        for product in self.get_productos():
            total += product.get_precio() * product.get_stock()

        print(f"El Total de la compra es de: {total}€")


if __name__ == "__main__": 
    ### INSTANCIAS DE CLASE ###

    # Crear productos de ejemplo
    producto1 = Producto("P001", "Chabola", 30.20, 20)
    producto2 = Producto("P002", "Luces led", 0.70, 200)
    producto3 = Producto("P003", "Cámara", 1990.73, 1)

    # Crear cliente de ejemplo
    cliente = Cliente("C001", "Pepe Luis", "pepeluis2019@gmail.com", "C/ Cerro Mataero' Chabola 4")

    # Crear pedido con el cliente
    pedido = Pedido("P001", cliente, "14/03/2025")

    ### USO ###

    # Agregar productos al pedido
    pedido.agregar_producto(producto1)
    pedido.agregar_producto(producto2)
    pedido.agregar_producto(producto3)

    # Imprimir detalles del pedido
    print(pedido)

    # Calcular el total del pedido
    pedido.calcular_total()
