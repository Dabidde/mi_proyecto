import zipfile
import os

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Bienvenido! a la página principal de tu proyecto."

if __name__ == "__main__":
    app.run(debug=True)
