from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

# Configuración de la aplicación
app = Flask(__name__, template_folder="views")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/prueba' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de la base de datos
db = SQLAlchemy(app)

# Definición de las tablas
class Cuidador(db.Model):
    __tablename__ = 'cuidadores'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(15), nullable=True)
    direccion = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<Cuidador {self.nombre}>'

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

# # Creación de las tablas y carga de datos de prueba en un contexto de aplicación
with app.app_context():
    # Crear las tablas en la base de datos
    db.create_all()

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

##db.init_app(app)

@app.route('/')
def index():
    # Consulta para contar cuántos perros se llaman "Lassie"
    cantidad_lassie = Perro.query.filter_by(nombre="Lassie").count()

    # Consulta para obtener todos los perros de Mario (suponiendo id = 1 para Mario)
    perros_mario = Perro.query.filter_by(id_cuidador=1).all()

    return render_template('index.html', cantidad_lassie=cantidad_lassie, perros_mario=perros_mario)

if __name__ == '__main__':
    app.run(debug=True)