### LIBRERÍAS ###
from Clase_Producto import Producto  # Importa la clase Producto
from Clase_Cliente import Cliente    # Importa la clase Cliente

### DEFINICIÓN DE CLASES ###
class Reseña(Producto, Cliente):
    """
    Clase que representa una reseña realizada por un cliente sobre un producto.
    Hereda de las clases Producto y Cliente para acceder a sus atributos.
    """

    def __init__(self, id_reseña: str, producto: Producto, cliente: Cliente, comentario: str, puntuacion: int):
        """
        Constructor de la clase Reseña.

        :param id_reseña: Identificador de la reseña.
        :param producto: Instancia del producto reseñado.
        :param cliente: Instancia del cliente que realiza la reseña.
        :param comentario: Comentario del cliente sobre el producto.
        :param puntuacion: Puntuación otorgada (entre 1 y 5).
        """
        # Inicializa atributos heredados de Producto y Cliente
        Producto.__init__(self, producto.get_id(), producto.get_nombre(), producto.get_precio(), producto.get_stock())
        Cliente.__init__(self, cliente.get_id(), cliente.get_nombre(), cliente.get_email(), cliente.get_direccion())

        self.__id_reseña = id_reseña
        self.__comentario = comentario

        # Controla que la puntuación esté dentro del rango válido (1 a 5)
        if puntuacion <= 0:
            self.__puntuacion = 1
        elif puntuacion > 5:
            self.__puntuacion = 5
        else:
            self.__puntuacion = puntuacion

    ### GETTERs Y SETTERs ###

    # Atributo ID de la reseña
    def get_id_reseña(self):
        """Devuelve el ID de la reseña."""
        return self.__id_reseña

    def set_id_reseña(self, nueva_reseña):
        """Establece un nuevo ID para la reseña."""
        self.__id_reseña = nueva_reseña

    # Atributo Comentario
    def get_comentario(self):
        """Devuelve el comentario de la reseña."""
        return self.__comentario

    def set_comentario(self, nuevo_comentario):
        """Establece un nuevo comentario para la reseña."""
        self.__comentario = nuevo_comentario

    # Atributo Puntuación
    def get_puntuacion(self):
        """Devuelve la puntuación otorgada en la reseña."""
        return self.__puntuacion

    def set_puntuacion(self, nueva_puntuacion):
        """
        Establece una nueva puntuación para la reseña.
        No se limita aquí, pero debería validarse externamente.
        """
        self.__puntuacion = nueva_puntuacion

    def __str__(self):
        """
        Devuelve una representación en cadena de la reseña,
        incluyendo información del producto y del cliente.
        """
        return (
            f" - ID: {self.get_id_reseña()}\n"
            f" - Producto: {self.get_nombre()}\n"
            f" - Cliente: {self.get_nombre()}\n"
            f" - Comentario: {self.get_comentario()}\n"
            f" - Puntuación: {self.get_puntuacion()}"
        )


if __name__ == "__main__":
    ### INSTANCIAS DE CLASE ###

    # Se crea un producto y un cliente
    producto = Producto("P001", "Colchón humilde", 190, 2)
    cliente = Cliente("C001", "Pepe Luis", "pepeluis2019@gmail.com", "C/ Cerro Mataero' Chabola 4")

    # Se crea una reseña sobre ese producto por parte del cliente
    reseña = Reseña("R001", producto, cliente, "Colchón reventado, con mierda por todas partes", 0)

    ### USO ###

    # Se imprime la reseña
    print(reseña)
