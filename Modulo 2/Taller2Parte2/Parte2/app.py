from flask import Flask
from flask import render_template
from db import db
from models.perro import Perro
from models.cuidador import Cuidador

# Configuración de la aplicación
app = Flask(__name__, template_folder="views")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/prueba' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    # Consulta para contar cuántos perros se llaman "Lassie"
    cantidad_lassie = Perro.query.filter_by(nombre="Lassie").count()

    # Consulta para obtener todos los perros de Mario por id
    perros_mario = Perro.query.filter_by(id_cuidador=2).all()

    return render_template('index.html', cantidad_lassie=cantidad_lassie, perros_mario=perros_mario)

if __name__ == '__main__':
    app.run(debug=True)