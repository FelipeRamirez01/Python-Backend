class Perro:
    def __init__(self, nombre:str, raza:str, peso:int, edad:int):
        self.nombre = nombre
        self.raza = raza
        self.peso = peso
        self.edad = edad
        

    def __str__(self):
        return f"Nombre perro es: {self.nombre}, Raza: {self.raza}, Edad: {self.edad} años, Su pesos es {self.peso}"
    
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
        
    @property
    def peso(self) -> int:
        """ Devuelve el valor del atributo privado 'peso' """
        return self.__peso
    
    @peso.setter
    def peso(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'peso'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self.__peso = value
        else:
            raise ValueError('Expected int')