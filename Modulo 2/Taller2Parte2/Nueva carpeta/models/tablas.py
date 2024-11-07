
from app import db

class Cuidador(db.Model):
    __tablename__ = 'cuidadores'

    id_cuidador = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(100))

    # Relación con Perros (uno a muchos)
    perros = db.relationship('Perro', backref='cuidador', lazy=True)

    def __repr__(self):
        return f'<Cuidador {self.nombre}>'


class Perro(db.Model):
    __tablename__ = 'perros'

    id_perro = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    raza = db.Column(db.String(50))
    edad = db.Column(db.Integer)
    peso = db.Column(db.Float)
    id_cuidador = db.Column(db.Integer, db.ForeignKey('cuidadores.id_cuidador'), nullable=False)
    # Omite id_guarderia según las instrucciones

    def __repr__(self):
        return f'<Perro {self.nombre}>'
