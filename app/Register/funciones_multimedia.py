from app.config import configracion_base
from werkzeug.utils import secure_filename
import os


#CLIENTE_LOGO
def logo_cliente(nombre_comercial,logo_usuario):
    #ubicacion del folder
    carpeta_path = configracion_base.UPLOAD_FOLDERS['cliente_logo']
    
    #crear carpeta en caso de que no exista
    if not os.path.exists(carpeta_path):
        os.makedirs(carpeta_path)
        
    #capturar nombre del archivo
    file_name = secure_filename(logo_usuario.filename)
    
    #capturar extension del archivo
    extension  = os.path.splitext(file_name)[1]
    
    #concatenar valores
    file_name_final = nombre_comercial + extension
    
    #crear path
    file_path = os.path.join(carpeta_path, file_name_final)
    
    logo_usuario.save(file_path)
    
    file_path = file_path.replace('app', '')
    file_path = file_path.replace('\\', '/')
    
    return file_path

#EMPRESA_FUMIGADORA_LOGO
def logo_empresa_fumigadora(nombre_comercial,logo_usuario):
    #ubicacion del folder
    carpeta_path = configracion_base.UPLOAD_FOLDERS['empresa_fumigadora_logo']
    
    #crear carpeta en caso de que no exista
    if not os.path.exists(carpeta_path):
        os.makedirs(carpeta_path)
        
    #capturar nombre del archivo
    file_name = secure_filename(logo_usuario.filename)
    
    #capturar extension del archivo
    extension  = os.path.splitext(file_name)[1]
    
    #concatenar valores
    file_name_final = nombre_comercial + extension
    
    #crear path
    file_path = os.path.join(carpeta_path, file_name_final)

    logo_usuario.save(file_path)
    
    file_path = file_path.replace('app', '')
    file_path = file_path.replace('\\', '/')
    
    return file_path

#FOTO_ENCARGADO
def foto_encargado(nombre_encargado, foto):
    #ubicacion del folder
    carpeta_path = configracion_base.UPLOAD_FOLDERS['empresa_fumigadora_administrador']
    
    #crear carpeta en caso de que no exista
    if not os.path.exists(carpeta_path):
        os.makedirs(carpeta_path)
        
    #captura nombre del archivo
    file_name = secure_filename(foto.filename)
    
    #extension del archivo
    extension = os.path.splitext(file_name)[1]
    
    #concatenar valores
    file_name_final = nombre_encargado + extension
    
    #crear path
    file_path = os.path.join(carpeta_path,file_name_final)
    
    #guardar archivo
    foto.save(file_path)
    
    file_path = file_path.replace('app', '')
    file_path = file_path.replace('\\', '/')
    
    return file_path