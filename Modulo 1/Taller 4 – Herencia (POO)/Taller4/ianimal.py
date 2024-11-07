from abc import ABC, abstractmethod

class IAnimal(ABC):
  
    @abstractmethod
    def hacer_sonido(self):
        pass
    
    """  @abstractmethod
    def agregar_raton(self, comidad):
        pass

    @abstractmethod
    def ratones_comidos(self):
        pass
    """
   