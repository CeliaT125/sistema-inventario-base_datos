class Producto:
    #Añadimos los atributos privados con el constructor
    def __init__(self, nombre=None, precio=None, categoria=None,  cantidad=None):
        self.__nombre = nombre
        self.__precio = precio
        self.__categoria = categoria
        self.__cantidad = cantidad

    #Mostramos los detalles del producto
    def __str__(self):
        return f"Producto: {self.__nombre}, precio: {self.__precio} €, categoria: {self.__categoria}, cantidad: {self.__cantidad}"

    #Añadimos los getters y setters
    def get_nombre(self):
        return self.__nombre
    
    def get_categoria(self):
        return self.__categoria

    def get_precio(self):
        return self.__precio

    def get_cantidad(self):
        return self.__cantidad     

    #def set_precio(self, nuevo_precio):
    #    self.__precio = nuevo_precio  

    #def set_cantidad(self, nueva_cantidad):
    #    self.__cantidad = nueva_cantidad


