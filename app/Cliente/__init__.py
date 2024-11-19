from flask import Blueprint; 

Cliente = Blueprint("Cliente", __name__, url_prefix="/Cliente")

from . import views_cliente; 