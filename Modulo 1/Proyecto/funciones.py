
class Funciones:
    
    ##Punto 1
    def es_sano(self):
        return self.calorias < 100 or self.es_vegetariano
    
    ##Punto 2
    def calcular_calorias(self):
        return round(sum([ingrediente.calorias for ingrediente in self.ingredientes]) * 0.95, 2)

    ##Punto 3
    def calcular_costo(self):
        return sum([ingrediente.precio for ingrediente in self.ingredientes])
    
    ##Punto 4
    def calcular_rentabilidad(self):
        return self.precio_publico - self.calcular_costo()
    
    ##Punto 5
    def producto_mas_rentable(self):
        return max(self.productos, key=lambda producto: producto.calcular_rentabilidad()).nombre