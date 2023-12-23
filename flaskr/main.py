from flaskr import app  # app インスタンスをimport
from flask import render_template

@app.route('/')
def index():
    books = [
        {'title': 'Math',
        'price': 1000,
        'arrival_day': '2023/12/23'},
        
        {'title': 'English',
        'price': 1500,
        'arrival_day': '2023/12/27'},
    ]
    
    return render_template(
        'index.html',
        books=books
        )
    