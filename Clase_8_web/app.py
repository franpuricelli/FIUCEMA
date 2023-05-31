from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)
prendas = [
    {"id": 1, "tipo": "pantalon", "talle": 38},
    {"id": 2, "tipo": "pantalon", "talle": 48}
    ]

@app.get("/")
def home():
    return render_template("home.html") #<p> etiqueta de parrafo

@app.get("/prendas")
def get_all_prendas():
    return f"<p>Mostrando todas las prendas</p>"

#armar la ruta /prendas que muetsre todos los items de prendas

@app.get("/prendas/<id>")
def get_prenda(id):
    return f"<p>Mostrando la prenda {escape(id)}</p>"


