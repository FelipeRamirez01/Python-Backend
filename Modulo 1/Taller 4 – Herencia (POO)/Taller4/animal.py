from ianimal import IAnimal


class Animal(IAnimal):
    def __init__(self, nombre:str,  peso:int, edad:int):
        self.nombre = nombre
        self.peso = peso
        self.edad = edad

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
    def raza(self) -> str:
        return self.__raza
    @raza.setter
    def raza(self, value:str) -> None:
        if isinstance(value, str):
            self.__raza = value
        else:
            raise ValueError('Expected str')
        
    @property
    def edad(self) -> int:
        return self.__edad
    @edad.setter
    def edad(self, value:int) -> None:
        if isinstance(value, int):
            self.__edad = value
        else:
            raise ValueError('Expected int')