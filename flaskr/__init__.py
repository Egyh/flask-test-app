
from flask import Flask
app = Flask(__name__)
import flaskr.main # main.pyの内容をimport

from flaskr import db
db.create_books_table()