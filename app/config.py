import os

#configuracion base
class configracion_base():
    #basica
    SECRET_KEY = "slipknot_slipknot1999"
    DEBUG = True
    TESTING =  True
    #base de datos
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '20102006'
    MYSQL_DB = 'gestdata'
    #folder de imagenes
    UPLOAD_FOLDERS = {
        'cliente_logo': os.path.join('app', 'static', 'src', 'gest_data_users', 'cliente'),
        'empresa_fumigadora_logo': os.path.join('app', 'static', 'src', 'gest_data_users', 'empresa_fumigadora', 'logo'),
        'empresa_fumigadora_administrador': os.path.join('app', 'static', 'src', 'gest_data_users', 'empresa_fumigadora', 'administrador'),
        'sede_cliente_logo': os.path.join('app', 'static', 'src', 'gest_data_users', 'sede_cliente', 'logo'),
        'sede_cliente_administrador': os.path.join('app', 'static', 'src', 'gest_data_users', 'sede_cliente', 'administrador'),
    }
    
    #D:\Desktop\PROYECTOS_FLASK\gest_data\app\static\src\gest_data_users\cliente
    
class entorno_desarrollo(configracion_base):
    FLASK_ENV  = 'development'

class entorno_produccion(configracion_base):
    FLASK_ENV  = 'production'
    DEBUG = False
    TESTING = False

