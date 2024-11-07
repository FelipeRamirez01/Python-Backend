from ingrediente import Ingrediente

class Complemento(Ingrediente):
    def __init__(self, nombre: str, precio: int, calorias: int, inventario: float, es_vegetariano: bool):
        super().__init__(nombre, precio, calorias, inventario, es_vegetariano)

    def abastecer(self):
        self.inventario += 10

    def renovar_inventario(self):
        self.inventario = 0