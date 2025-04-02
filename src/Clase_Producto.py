### DEFINICIÓN DE CLASES ###
class Producto:
    def __init__(self, id:str, nombre:str, precio:float, stock:int):
        
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

### GETTERs Y SETTERs ###
#   Atributo Id    
    def get_id(self):
        return self.__id
    def set_id(self, nuevo_id):
        self.__id = nuevo_id
#   Atributo Nombre
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
#   Atributo Precio
    def get_precio(self):
        return self.__precio
    def set_precio(self, nuevo_precio):
        self.__precio = nuevo_precio
#   Atributo Stock
    def get_stock(self):
        return self.__stock
    def set_stock(self, nuevo_stock):
        self.__stock = nuevo_stock

    ### MÉTODOS DE LA FUNCIÓN ###
    def __str__(self):
        return f" - ID: {self.get_id()}\n - Nombre {self.get_nombre()}\n - Precio: {self.get_precio()}€\n - Stock: {self.get_stock()}\n"
    
    def actualizar_stock(self, cantidad:int):
        self.set_stock(cantidad)
    
if __name__ == "__main__":
    ### INSTANCIAS DE CLASE ###
    producto = Producto("P001", "Chabola", 312.80, 20)

    ### USO ###
    print(producto)