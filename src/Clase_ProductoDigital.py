### LIBRERÍAS ###
from Clase_Producto import Producto

### DEFINICIÓN DE CLASES ###
class ProductoDigital(Producto):
    def __init__(self, id:str, nombre:str, precio:float, stock:int, formato:str, tamaño:float):
        super().__init__(id, nombre, precio, stock)

        self.__formato = formato
        self.__tamaño = tamaño

### GETTERs Y SETTERs ###
#   ATRIBUTO FORMATO
    def get_formato(self):
        return self.__formato
    def set_formato(self, nuevo_formato):
        self.__formato = nuevo_formato
# ATRIBUTO TAMAÑO
    def get_tamaño(self):
        return self.__tamaño
    def set_tamaño(self, nuevo_tamaño):
        self.__tamaño = nuevo_tamaño

    ### MÉTODOS DE LA CLASE PRODUCTODIGITAL ###
    def __str__(self):
        return f"{super().__str__()}\n - Formato: {self.get_formato()}\n - Tamaño: {self.get_tamaño()} MB\n" 

if __name__ == "__main__":
    ### INSTANCIAS DE CLASE ###
    producto_digital = ProductoDigital("P002", "Los chunguitos", 12.99, 4, "MP4", 2400 )

    ### USO ###
    print(producto_digital)