from flask import Blueprint;

Recuperar_password = Blueprint("Recuperar_password", __name__, url_prefix="/Recuperar_password")

from . import views_recuperar_password