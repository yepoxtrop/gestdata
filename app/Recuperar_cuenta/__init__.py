from flask import Blueprint

Activar_cuenta = Blueprint("Activar_cuenta", __name__, url_prefix="/Activar_cuenta")

from . import views_recuperar_estado
