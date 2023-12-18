from flaskr import app  # app インスタンスをimport
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')