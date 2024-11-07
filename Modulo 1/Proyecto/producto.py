from iproducto import IProducto

# Clases Prodcuto que implementa IProducto
class Producto(IProducto):
    def __init__(self, nombre: str, precio_publico: int, ingredientes: list):
        self.nombre = nombre
        self.precio_publico = precio_publico
        self.ingredientes = ingredientes

@property
def nombre(self) -> str:
    """ Devuelve el valor del atributo privado 'nombre' """
    return self.__nombre

@nombre.setter
def nombre(self, value:str) -> None:
    """ 
    Establece un nuevo valor para el atributo privado 'nombre'

    Valida que el valor enviado corresponda al tipo de dato del atributo
    """ 
    if isinstance(value, str):
        self.__nombre = value
    else:
        raise ValueError('Expected str')
    
@property
def precio_publico(self) -> int:
    """ Devuelve el valor del atributo privado 'precio_publico' """
    return self.__precio_publico

@precio_publico.setter
def precio_publico(self, value:int) -> None:
    """ 
    Establece un nuevo valor para el atributo privado 'precio_publico'

    Valida que el valor enviado corresponda al tipo de dato del atributo
    """ 
    if isinstance(value, int):
        self.__precio_publico = value
    else:
        raise ValueError('Expected int')
    
@property
def ingredientes(self) -> list:
    """ Devuelve el valor del atributo privado 'ingredientes' """
    return self.__ingredientes

@ingredientes.setter
def ingredientes(self, value:list) -> None:
    """ 
    Establece un nuevo valor para el atributo privado 'ingredientes'

    Valida que el valor enviado corresponda al tipo de dato del atributo
    """ 
    if isinstance(value, list):
        self.__ingredientes = value
    else:
        raise ValueError('Expected list')