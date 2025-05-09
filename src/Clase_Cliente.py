### DEFINICIÓN DE CLASES ###
class Cliente:
    """
    Clase que representa a un cliente con sus datos personales.
    """

    def __init__(self, id: str, nombre: str, email: str, direccion: str):
        """
        Constructor de la clase Cliente.

        :param id: Identificador único del cliente.
        :param nombre: Nombre completo del cliente.
        :param email: Correo electrónico del cliente.
        :param direccion: Dirección física del cliente.
        """
        self.__id = id
        self.__nombre = nombre
        self.__email = email
        self.__direccion = direccion

    ### GETTERs Y SETTERs ###

    # Atributo ID
    def get_id(self):
        """
        Devuelve el ID del cliente.
        """
        return self.__id

    def set_id(self, nuevo_id):
        """
        Establece un nuevo ID para el cliente.

        :param nuevo_id: Nuevo identificador.
        """
        self.__id = nuevo_id

    # Atributo Nombre
    def get_nombre(self):
        """
        Devuelve el nombre del cliente.
        """
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        """
        Establece un nuevo nombre para el cliente.

        :param nuevo_nombre: Nuevo nombre.
        """
        self.__nombre = nuevo_nombre

    # Atributo Email
    def get_email(self):
        """
        Devuelve el email del cliente.
        """
        return self.__email

    def set_email(self, nuevo_email):
        """
        Establece un nuevo email para el cliente.

        :param nuevo_email: Nuevo correo electrónico.
        """
        self.__email = nuevo_email

    # Atributo Dirección
    def get_direccion(self):
        """
        Devuelve la dirección del cliente.
        """
        return self.__direccion

    def set_direccion(self, nueva_direccion):
        """
        Establece una nueva dirección para el cliente.

        :param nueva_direccion: Nueva dirección.
        """
        self.__direccion = nueva_direccion

    ### MÉTODOS DE LA CLASE CLIENTE ###

    def __str__(self):
        """
        Devuelve una representación en forma de cadena de los datos del cliente.

        :return: Cadena formateada con los datos del cliente.
        """
        return f" - ID: {self.get_id()}\n - Nombre: {self.get_nombre()}\n - Email: {self.get_email()}\n - Dirección: {self.get_direccion()}"


if __name__ == "__main__":
    ### INSTANCIAS DE CLASE ###

    # Se crea un objeto Cliente con sus atributos.
    cliente = Cliente(
        "C001", "Pepe Luis", "pepeluis2019@gmail.com", "C/ Cerro Mataero' Chabola 4"
    )

    ### USO ###

    # Se imprime la representación en string del cliente.
    print(cliente)
