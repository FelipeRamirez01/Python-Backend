class Guarderia:
    def __init__(self):
        self.perros = []
        self.concentrados = []

    def agregar_perro(self, perro):
        self.perros.append(perro)

    def agregar_concentrado(self, concentrado):
        self.concentrados.append(concentrado)

    def mostrar_perros(self):
        for perro in self.perros:
            print(perro)