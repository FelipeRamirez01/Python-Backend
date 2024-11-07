from flask import Flask, render_template
from controllers.controller import retorna_perros

app = Flask(__name__, template_folder="views")

@app.route("/")
def index():
     _perro = retorna_perros()
     return render_template("index.html", perros=_perro)


