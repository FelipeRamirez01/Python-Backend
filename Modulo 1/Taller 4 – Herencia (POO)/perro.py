class Perro:
    def __init__(self, nombre:str, raza:str, edad:int, concentrado:list):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.concentrado = concentrado 

    def __str__(self):
        return f"Nombre perro es: {self.nombre}, Raza: {self.raza}, Edad: {self.edad} años, Concentrado Favorito: {self.concentrado.dar_informacion()}"
    
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