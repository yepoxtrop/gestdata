from flask import Blueprint
Index = Blueprint("Index", __name__, url_prefix="/")
from . import views_index