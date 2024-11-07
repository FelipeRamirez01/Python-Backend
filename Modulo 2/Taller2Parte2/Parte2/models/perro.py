from db import db

class Perro(db.Model):
    __tablename__ = 'perros'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    raza = db.Column(db.String(30), nullable=True)
    edad = db.Column(db.Integer, nullable=True)
    peso = db.Column(db.Float, nullable=True)
    id_cuidador = db.Column(db.Integer, db.ForeignKey('cuidadores.id'), nullable=False)

    cuidador = db.relationship('Cuidador', backref='perros')

    def __repr__(self):
        return f'<Perro {self.nombre}>'