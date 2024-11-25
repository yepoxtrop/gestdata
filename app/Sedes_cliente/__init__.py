from flask import Blueprint
Sede_cliente = Blueprint('Sede_cliente', __name__, url_prefix='/Sede_cliente')
from . import views_sede_cliente