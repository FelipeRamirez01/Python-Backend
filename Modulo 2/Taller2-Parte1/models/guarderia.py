from  models.perro import Perro
from typing import Tuple

class Guarderia:
    def __init__(self):
        self.perros = []
           
    def agregar_perro(self, perro):
        self.perros.append(perro)

    def retornar_perros(self) ->Tuple[Perro]:
       return tuple(self.perros)