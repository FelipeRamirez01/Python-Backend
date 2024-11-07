from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from controllers.perros_controller import perros_controller

# Inicialización de la aplicación
app = Flask(__name__)
app.config.from_object(Config)

# Inicialización de la base de datos
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)
