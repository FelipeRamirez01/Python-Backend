from flask import render_template
from app import app
from models.perro import Perro
from models.cuidador import Cuidador

@app.route('/')
def index():
    # Obtén todos los perros
    perros = Perro.query.all()
    return render_template('index.html', perros=perros)

@app.route('/perros/<int:perro_id>')
def ver_perro(perro_id):
    # Muestra los detalles de un perro específico
    perro = Perro.query.get_or_404(perro_id)
    return render_template('perro_detalle.html', perro=perro)
