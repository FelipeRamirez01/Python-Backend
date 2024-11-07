
from app import db
from models.tablas import Cuidador, Perro

with db.app_context():
    # Crear las tablas en la base de datos
    db.create_all()

    # Datos de prueba para Cuidadores
    cuidador1 = Cuidador(nombre="andres", telefono="123456789", direccion="Calle 123")
    cuidador2 = Cuidador(nombre="jorge", telefono="987654321", direccion="Avenida 456")
    db.session.add_all([cuidador1, cuidador2])

    # Datos de prueba para Perros
    perro1 = Perro(nombre="Firulais", raza="Labrador", edad=3, peso=22.5, cuidador=cuidador1)
    perro2 = Perro(nombre="Max", raza="Pug", edad=1, peso=8.2, cuidador=cuidador2)
    db.session.add_all([perro1, perro2])

    # Confirmar los cambios en la base de datos
    db.session.commit()

print("Base de datos y tablas creadas exitosamente.")
