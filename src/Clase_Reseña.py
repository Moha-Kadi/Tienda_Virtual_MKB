### LIBRERÍAS ###
from Clase_Producto import Producto
from Clase_Cliente import Cliente

### DEFINICIÓN DE VARIABLES ###
class Reseña(Producto, Cliente):
    def __init__(self, id_reseña:str, producto:Producto, cliente:Cliente, comentario:str, puntuacion:int):
        Producto.__init__(self, producto.get_id(), producto.get_nombre(), producto.get_precio(), producto.get_stock())
        Cliente.__init__(self, cliente.get_id(), cliente.get_nombre(), cliente.get_email(), cliente.get_direccion())


        self.__id_reseña = id_reseña
        self.__comentario = comentario
        if puntuacion <= 0:
            self.__puntuacion = 1
        elif puntuacion > 5:
            self.__puntuacion = 5
        else:
            self.__puntuacion = puntuacion

### GETTERs Y SETTERs ###
#   ATRIBUTO RESEÑA
    def get_id_reseña(self):
        return self.__id_reseña
    def set_id_reseña(self, nueva_reseña):
        self.__id_reseña = nueva_reseña
#   ATRIBUTO COMENTARIO
    def get_comentario(self):
        return self.__comentario
    def set_comentario(self, nuevo_comentario):
        self.__comentario = nuevo_comentario
#   ATRIBUTO PUNTUACIÓN 
    def get_puntuacion(self):
        return self.__puntuacion
    def set_puntuacion(self, nueva_puntuacion):
        self.__puntuacion = nueva_puntuacion


    def __str__(self):
        return (f" - ID: {self.get_id_reseña()}\n - Producto: {producto.get_nombre()}\n - Cliente: {cliente.get_nombre()}\n - Comentario: {self.get_comentario()}\n - Puntuación: {self.get_puntuacion()}")

if __name__ == "__main__":
    ### INSTANCIAS DE CLASE ###
    producto = Producto("P001", "Colchón humilde", 190, 2)
    cliente = Cliente("C001", "Pepe Luis", "pepeluis2019@gmail.com", "C/ Cerro Mataero' Chabola 4")
    reseña = Reseña("R001",producto, cliente, "Colchón reventado, con mierda por todas partes", 0 )

    ### USO ###
    print(reseña)