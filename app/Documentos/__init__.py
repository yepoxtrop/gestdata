from flask import Blueprint
Documentos = Blueprint('Documentos', __name__, url_prefix='/Documentos')
from . import views_documentos