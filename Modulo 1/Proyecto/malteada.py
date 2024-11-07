from producto import Producto

class Malteada(Producto):
    def __init__(self, nombre: str, precio_publico: int, ingredientes: list, volumen:int):
        super().__init__(nombre, precio_publico, ingredientes)
        self.volumen = volumen

    def calcular_costo(self):
        return sum([ingrediente.precio for ingrediente in self.ingredientes]) + 500  # Costo adicional por vaso plástico

    def calcular_calorias(self):
        return sum([ingrediente.calorias for ingrediente in self.ingredientes]) + 200  # Extra calorías por crema chantilly

    def calcular_rentabilidad(self):
        return self.precio_publico - self.calcular_costo()
  

    @property
    def volumen(self) -> int:
        """ Devuelve el valor del atributo privado 'volumen' """
        return self.__volumen
    
    @volumen.setter
    def volumen(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'volumen'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self.__volumen = value
        else:
            raise ValueError('Expected int')