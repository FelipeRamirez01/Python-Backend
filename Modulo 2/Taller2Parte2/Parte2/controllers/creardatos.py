from prueba import db
from models.cuidador import Cuidador
from models.perro import Perro

with db.app_context():
    # Crear las tablas en la base de datos
   ## db.create_all()

    # Datos de prueba para Cuidadores
    cuidador1 = Cuidador(nombre="Mario", telefono="123456789", direccion="Calle 123")
    cuidador2 = Cuidador(nombre="Lucia", telefono="987654321", direccion="Avenida 456")
    ## db.session.add_all([cuidador1, cuidador2])

    # Datos de prueba para Perros
    perro1 = Perro(nombre="Firulais", raza="Labrador", edad=3, peso=2.5, cuidador=cuidador1)
    perro2 = Perro(nombre="Lassie", raza="Pug", edad=1, peso=8.2, cuidador=cuidador2)
    perro4 = Perro(nombre='Max', raza='Labrador',edad= 3, peso=2.5, cuidador=cuidador1)
    perro5 = Perro(nombre='Bella', raza='Golden Retriever', edad=2, peso=4.0, cuidador=cuidador1)
    perro6 = Perro(nombre='Rocky', raza='Bulldog',edad= 4, peso=18.3, cuidador=cuidador2)
    perro7 = Perro(nombre='Lassie', raza='Poodle',edad= 1, peso=2.2, cuidador=cuidador1),
    ##db.session.add_all([perro1, perro2, perro3, perro4, perro5, perro6, perro7])

    # Confirmar los cambios en la base de datos
    db.session.commit()