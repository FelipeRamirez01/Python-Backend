from abc import ABC, abstractmethod

# Interfaz Producto
class IProducto(ABC):
    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def calcular_calorias(self):
        pass

    @abstractmethod
    def calcular_rentabilidad(self):
        pass