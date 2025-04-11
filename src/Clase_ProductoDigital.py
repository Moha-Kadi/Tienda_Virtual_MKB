### LIBRERÍAS ###
from Clase_Producto import Producto  # Importa la clase base Producto

### DEFINICIÓN DE CLASES ###
class ProductoDigital(Producto):
    """
    Clase que representa un producto digital, heredando de Producto,
    e incluyendo atributos adicionales como formato y tamaño.
    """

    def __init__(self, id: str, nombre: str, precio: float, stock: int, formato: str, tamaño: float):
        """
        Constructor de la clase ProductoDigital.

        :param id: Identificador del producto.
        :param nombre: Nombre del producto digital.
        :param precio: Precio del producto digital.
        :param stock: Cantidad disponible.
        :param formato: Formato del archivo digital (por ejemplo, MP4, PDF, etc.).
        :param tamaño: Tamaño del archivo en MB.
        """
        super().__init__(id, nombre, precio, stock)  # Llama al constructor de la clase padre
        self.__formato = formato
        self.__tamaño = tamaño

    ### GETTERs Y SETTERs ###

    # ATRIBUTO FORMATO
    def get_formato(self):
        """Devuelve el formato del archivo digital."""
        return self.__formato

    def set_formato(self, nuevo_formato):
        """Establece un nuevo formato para el producto digital."""
        self.__formato = nuevo_formato

    # ATRIBUTO TAMAÑO
    def get_tamaño(self):
        """Devuelve el tamaño del archivo en MB."""
        return self.__tamaño

    def set_tamaño(self, nuevo_tamaño):
        """Establece un nuevo tamaño en MB para el archivo."""
        self.__tamaño = nuevo_tamaño

    ### MÉTODOS DE LA CLASE PRODUCTODIGITAL ###

    def __str__(self):
        """
        Devuelve una representación en cadena del producto digital,
        incluyendo la información heredada del producto base.
        """
        return (
            f"{super().__str__()}\n"
            f" - Formato: {self.get_formato()}\n"
            f" - Tamaño: {self.get_tamaño()} MB\n"
        )


if __name__ == "__main__":
    ### INSTANCIAS DE CLASE ###

    # Se crea un producto digital de ejemplo
    producto_digital = ProductoDigital("P002", "Los chunguitos", 12.99, 4, "MP4", 2400)

    ### USO ###

    # Se imprime la información del producto digital
    print(producto_digital)
