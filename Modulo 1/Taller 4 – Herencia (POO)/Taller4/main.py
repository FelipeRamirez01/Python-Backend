from boa_constrictor import Boa_Constrictor
from huron import Huron


boa1 = Boa_Constrictor("Maxi", 13000, 44, "Colombia", 200.2)
boa1.agregar_raton()

print(boa1.ratones_comidos)
print(boa1.hacer_sonido())
boa1.agregar_raton(2)

huron1 = Huron("Oreo", 200, 4, "Mexico", 50.1)

print(huron1.hacer_sonido())
print(huron1.nombre)
print(boa1.calcular_flete())

## Con Get de la funcion independiente con frase
print(boa1.ratones_comidos())
## Con Get de la variable ratones_comido
print(boa1.ratones_comido)




