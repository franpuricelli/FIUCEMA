from flask import Flask, render_template

# python3 -m flask run #

app = Flask(__name__)

productos = {
    1:{"name":"Sherlock Holmes", "Stock":2, "precio_unitario":300, "imagen":"static/sherlock.jpeg"},
    2:{"name":"La Sirenita", "Stock":1, "precio_unitario":200, "imagen":"static/la_sirenita.jpeg"},
    3:{"name":"Zero to One", "Stock":4, "precio_unitario":400, "imagen":"static/zero_to_one.png"}
}

@app.get("/")
def home():
    return render_template("home.html") 

@app.get("/libros")
def get_all_libros():
    return render_template("libros.html", productos=productos.items())

@app.get("/productos/<int:id>")
def get_producto(id):
    if id in productos:
        producto = productos[id]
        return render_template("producto.html", id=id, producto=producto)
    else:
        return ("no hay producto", 404)
    


