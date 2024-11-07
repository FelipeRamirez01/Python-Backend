from animal import Animal


class Animal_Exotico(Animal):
    def __init__(self,nombre:str, peso:int, edad:int, pais_origen:str, impuestos:str):
        super().__init__(nombre, peso, edad)
        self.pais_origen = pais_origen
        self.impuestos = impuestos

    def calcular_flete(self):
        valor = self.impuestos * self.peso
        return f"El flete del animal {self.nombre} es de ${valor}"
    

    @property
    def pais_origen(self) -> str:
        return self.__pais_origen
    @pais_origen.setter
    def pais_origen(self, value:str) -> None:
        if isinstance(value, str):
            self.__pais_origen = value
        else:
            raise ValueError('Expected str')
        
    @property
    def impuestos(self) -> float:
        return self.__impuestos
    @impuestos.setter
    def impuestos(self, value: float) -> None:
        if isinstance(value, float):
            self.__impuestos = value
        else:
            raise ValueError('Expected float')