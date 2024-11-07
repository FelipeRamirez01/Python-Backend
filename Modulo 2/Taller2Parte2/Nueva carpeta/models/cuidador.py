from app import db

class Cuidador(db.Model):
    __tablename__ = 'cuidadores'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(15), nullable=True)
    direccion = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<Cuidador {self.nombre}>'
