from flask import Flask, render_template

# python3 -m flask run #

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("home.html") 
