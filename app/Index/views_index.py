from flask import render_template
from . import Index

@Index.route('/')
def home():
    print("views_index.py se ha cargado correctamente.")
    return render_template('Index.html')
