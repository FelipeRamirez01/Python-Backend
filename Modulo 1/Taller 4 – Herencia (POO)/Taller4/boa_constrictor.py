from animal_exotico import Animal_Exotico

class Boa_Constrictor(Animal_Exotico):
    def __init__(self,nombre, peso, edad, pais_origen, impuestos, ratones_comido=0):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self.ratones_comido = ratones_comido
    
    def agregar_raton(self, numero=1) -> None:
        self.__ratones_comido += numero

    def ratones_comidos(self):
        return f"{self.nombre} Se a comido {self.ratones_comido} ratones"
    
   
    def hacer_sonido(self):
        return "¡Tsss!"
    
    @property
    def ratones_comido(self) -> int:
        return self.__ratones_comido
    @ratones_comido.setter
    def ratones_comido(self, value:int) -> None:
        if isinstance(value, int):
            self.__ratones_comido = value
        else:
            raise ValueError('Expected int')