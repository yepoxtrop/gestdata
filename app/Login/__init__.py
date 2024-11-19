from flask import Blueprint
Login = Blueprint("Login", __name__, url_prefix="/Login")

from . import views_login