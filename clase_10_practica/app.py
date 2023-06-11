from flask import Flask, render_template

# python3 -m flask run #

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("home.html") #<p> etiqueta de parrafo

@app.get("/conclusiones")
def home1():
    return render_template("conclusiones.html")


