from producto import Producto

# Clases Copa y Malteada que implementan IProducto
class Copa(Producto):
    def __init__(self, nombre: str, precio_publico: int, ingredientes: list, tipo_vaso:str):
        super().__init__(nombre, precio_publico, ingredientes)
        self.tipo_vaso = tipo_vaso

    def calcular_costo(self):
        return sum([ingrediente.precio for ingrediente in self.ingredientes])

    def calcular_calorias(self):
        return round(sum([ingrediente.calorias for ingrediente in self.ingredientes]) * 0.95, 2)

    def calcular_rentabilidad(self):
        return self.precio_publico - self.calcular_costo()
    
    @property
    def tipo_vaso(self) -> str:
        """ Devuelve el valor del atributo privado 'tipo_vaso' """
        return self.__tipo_vaso
    
    @tipo_vaso.setter
    def tipo_vaso(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'tipo_vaso'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self.__tipo_vaso = value
        else:
            raise ValueError('Expected str')
    
  