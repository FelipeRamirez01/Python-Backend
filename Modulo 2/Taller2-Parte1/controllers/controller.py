from models.guarderia import Guarderia
from models.perro import Perro
from typing import Tuple



perro1 = Perro("Rufo", "Labrador", 22, 7)
perro2 = Perro("Bingo", "Pug", 6, 4)
perro3 = Perro("Lassie", "Collie", 27, 5)


# Crear guardería y agregar a los perros
guarderia = Guarderia()
guarderia.agregar_perro(perro1)
guarderia.agregar_perro(perro2)
guarderia.agregar_perro(perro3)

 
def retorna_perros() -> Tuple[Perro]:
    return guarderia.retornar_perros()