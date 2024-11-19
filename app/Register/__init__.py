from flask import Blueprint

Register = Blueprint("Register", __name__, url_prefix="/Register")

from . import views_register