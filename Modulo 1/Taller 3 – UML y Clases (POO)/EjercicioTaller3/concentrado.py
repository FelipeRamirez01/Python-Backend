class Concentrado:
    def __init__(self, nombre:str, precio:int, calorias:int, registro_invima:str):
        self.nombre = nombre
        self.precio = precio
        self.calorias = calorias
        self.__registro_invima = registro_invima

    def dar_informacion(self):
        return f"{self.nombre} Valor: ${self.precio}"

    def calcular_rentabilidad(self):
        return f"Rentabilidad del concentrada {self.nombre} es ${round(self.precio / self.calorias, 2)} por gramo"
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, value:str) -> None:
        if isinstance(value, str):
            self.__nombre = value
        else:
            raise ValueError('Expected str')
    @property
    def precio(self) -> int:
        return self.__precio
    @precio.setter
    def precio(self, value:int) -> None:
        if isinstance(value, int):
            self.__precio = value
        else:
            raise ValueError('Expected int')
    @property
    def calorias(self) -> int:
        return self.__calorias
    @calorias.setter
    def calorias(self, value:int) -> None:
        if isinstance(value, int):
            self.__calorias = value
        else:
            raise ValueError('Expected int')