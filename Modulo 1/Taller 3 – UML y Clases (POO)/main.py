from perro import Perro

perro1 = Perro("Zeus", "Rottweiler", 3, 45.8 )
perro2 = Perro("Nala", "Golden R.", 0, 8 )
perro3 = Perro("Atila", "Alabai", 5, 58.9 )

print(perro1.get_peso())

perro1.modificar_peso(46.5)

print(perro1.get_peso())
print(perro3.__dict__)

print(perro1.ladrar())
print(perro2.ladrar())

perro1.modificar_peso(44.8)
print(perro1.__dict__)

print(perro1.nombre)