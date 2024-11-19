from flask import Blueprint
Empresa_fumigadora =  Blueprint("Empresa_fumigadora", __name__, url_prefix="/Empresa_fumigadora")
from . import views_empresa_fumigadora
