### DEFINICIÓN DE CLASES ###
class Producto:
    """
    Clase que representa un producto con su información básica:
    ID, nombre, precio y stock disponible.
    """

    def __init__(self, id: str, nombre: str, precio: float, stock: int):
        """
        Constructor de la clase Producto.

        :param id: Identificador único del producto.
        :param nombre: Nombre del producto.
        :param precio: Precio unitario del producto.
        :param stock: Cantidad disponible en inventario.
        """
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    ### GETTERs Y SETTERs ###

    # Atributo ID
    def get_id(self):
        """Devuelve el ID del producto."""
        return self.__id

    def set_id(self, nuevo_id):
        """Establece un nuevo ID para el producto."""
        self.__id = nuevo_id

    # Atributo Nombre
    def get_nombre(self):
        """Devuelve el nombre del producto."""
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        """Establece un nuevo nombre para el producto."""
        self.__nombre = nuevo_nombre

    # Atributo Precio
    def get_precio(self):
        """Devuelve el precio del producto."""
        return self.__precio

    def set_precio(self, nuevo_precio):
        """Establece un nuevo precio para el producto."""
        self.__precio = nuevo_precio

    # Atributo Stock
    def get_stock(self):
        """Devuelve la cantidad disponible en stock del producto."""
        return self.__stock

    def set_stock(self, nuevo_stock):
        """Establece una nueva cantidad de stock para el producto."""
        self.__stock = nuevo_stock

    ### MÉTODOS DE LA CLASE ###

    def __str__(self):
        """
        Devuelve una representación en cadena del producto.

        :return: Cadena con los detalles del producto.
        """
        return (
            f" - ID: {self.get_id()}\n"
            f" - Nombre: {self.get_nombre()}\n"
            f" - Precio: {self.get_precio()}€\n"
            f" - Stock: {self.get_stock()}\n"
        )

    def actualizar_stock(self, cantidad: int):
        """
        Actualiza el stock disponible del producto.

        :param cantidad: Nueva cantidad de stock.
        """
        self.set_stock(cantidad)


if __name__ == "__main__":
    ### INSTANCIAS DE CLASE ###

    # Se crea un producto de ejemplo
    producto = Producto("P001", "Chabola", 312.80, 20)

    ### USO ###

    # Se imprime el producto
    print(producto)
