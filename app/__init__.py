from flask import Flask
from .config import entorno_desarrollo
from .config import entorno_produccion
from app.Index import Index  
from app.Login import Login  
from app.Register import Register
from app.Recuperar_password import Recuperar_password
from app.Empresa_fumigadora import Empresa_fumigadora
from app.Documentos import Documentos
from app.Recuperar_cuenta import Activar_cuenta
from app.Cliente import Cliente; 
from app.Emp_empresa_fumigadora import Emp_empresa_fumigadora
from app.Sedes_cliente import Sede_cliente

from flask_mysqldb import MySQL


mysql = MySQL()

def crear_app():
    app = Flask(__name__)
    
    #configuracion base()
    app.config.from_object(entorno_produccion) 
    
    #conexion a bd
    mysql.init_app(app)
    
    #blueprints
    app.register_blueprint(Index)
    app.register_blueprint(Login)
    app.register_blueprint(Register)
    app.register_blueprint(Recuperar_password)
    app.register_blueprint(Empresa_fumigadora)
    app.register_blueprint(Documentos)
    app.register_blueprint(Activar_cuenta)
    app.register_blueprint(Cliente)
    app.register_blueprint(Emp_empresa_fumigadora)
    app.register_blueprint(Sede_cliente)
    
    #sesiones de login - logout
    return app
