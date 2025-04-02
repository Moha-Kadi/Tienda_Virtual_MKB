### DEFINICIÓN DE CLASES ###
class Cliente:
    def __init__(self, id:str, nombre:str, email:str, direccion:str):
        
        self.__id = id
        self.__nombre = nombre
        self.__email = email
        self.__direccion = direccion

### GETTERs Y SETTERs ###
#   Atributo ID
    def get_id(self):
        return self.__id
    def set_id(self, nuevo_id):
        self.__id = nuevo_id
#   Atributo Nombre
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
#   Atributo Email
    def get_email(self):
        return self.__email
    def set_email(self, nuevo_email):
        self.__email = nuevo_email
#   Atributo Dirección
    def get_direccion(self):
        return self.__direccion
    def set_direccion(self, nueva_direccion):
        self.__direccion = nueva_direccion

    ### MÉTODOS DE LA CLASE CLIENTE ###

    def __str__(self):
        return f" - ID: {self.get_id()}\n - Nombre: {self.get_nombre()}\n - Email: {self.get_email()}\n - Dirección: {self.get_direccion()}"

if __name__ == "__main__":
    ### INSTANCIAS DE CLASE ###
    cliente = Cliente("C001", "Pepe Luis", "pepeluis2019@gmail.com", "C/ Cerro Mataero' Chabola 4")

    ### USO ###
    print(cliente)
