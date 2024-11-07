from perro import Perro
from guarderia import Guarderia
from concentrado import Concentrado

# Crear concentrados
concentrado1 = Concentrado("Dog Chow", 13000, 424, "INV1234")
concentrado2 = Concentrado("Chunky", 18000, 500, "INV5678")

# Crear perros y asigna concentrado
perro1 = Perro("Oreo", "Pitbull", 3, concentrado1)
perro2 = Perro("Bella", "Pincher", 6, concentrado2)

# Crear guardería y agregar a los perros
guarderia = Guarderia()
guarderia.agregar_perro(perro1)
guarderia.agregar_perro(perro2)

# Asignar concentrados a la guardería
guarderia.agregar_concentrado(concentrado1)
guarderia.agregar_concentrado(concentrado2)

# Mostrar información de los perros
guarderia.mostrar_perros()

# Mostrar rentabilidad concentrado
print(concentrado1.calcular_rentabilidad())
