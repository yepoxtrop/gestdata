from flask import Blueprint
Emp_empresa_fumigadora = Blueprint('Emp_empresa_fumigadora', __name__, url_prefix='/Emp_empresa_fumigadora')
from . import views_emp_empresa_fumigadora