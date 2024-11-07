
from circulo import calcularCirculo

def calcularCuadrado(lado):
   
    areaCuadrado = lado ** 2

    radio = lado / 2  
    areaCirculo = calcularCirculo(radio)
    
    areaSombreada = areaCuadrado - areaCirculo
    
    return round(areaSombreada, 2)
