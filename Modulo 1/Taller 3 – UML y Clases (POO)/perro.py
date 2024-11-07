class Perro:
    #Constructor
    def __init__(self, nombre:str, raza:str, edad:int, peso:float) -> None:
        
        ##Atributos
        self.nombre = nombre
        self.__raza = raza
        self.__edad = edad
        self.__peso = peso

    #Metodos

    def modificar_peso(self, peso:float) -> None:
        if isinstance(peso, float):
            self.__peso = peso

    def get_peso(self) -> float:
        return self.__peso
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, value:str) -> None:
        if isinstance(value, str):
            self.__nombre = value
        else:
            raise ValueError('Expected str')
    
    #Utiliza una informacion estatica, es decir, que no utiliza ni atributos ni metodos de la instancia
    @staticmethod
    def ladrar() -> str:
        return "¡Guau, Guau!"