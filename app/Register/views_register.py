from . import Register
from flask import render_template, request, redirect, url_for, session, flash;
from werkzeug.security import generate_password_hash
#importaciones para guardar imagenes
import os
from app.config import configracion_base
from app.Register.funciones_multimedia import logo_cliente, logo_empresa_fumigadora, foto_encargado


@Register.route('/Register')
def register():
    return render_template('/Register.html')


@Register.route('/Register', methods=['POST'])
def registrar_usuario():
    #conexion a base de datos
    from app import mysql
    
    if request.method == 'POST':
        #inputs del formulario
        
        logo = request.files['logo']; 
        nit = request.form['nit']; 
        nombre_comercial = request.form['comercial']; 
        razon = request.form['razon']; 
        direccion = request.form['direccion']; 
        departamento = request.form['departamento']; 
        telefono = request.form['telefono']; 
        correo = request.form['correo']; 
        fotoEncargados = request.files['fotoEncargados']; 
        descripcion = request.form['descripcion']; 
        contraseña = request.form['contraseña']; 
        contraseña_cifrada = generate_password_hash(contraseña, 'pbkdf2:sha256:5', 5); 
        encargado_nombre = request.form['encargado_nombre']; 
        encargado_correo = request.form['encargado_correo']; 
        encargado_telefono = request.form['encargado_telefono']; 
        
        #checkbox
        cliente = request.form.get('cliente'); 
        empresa_fumigadora = request.form.get('empresa_fumigadora'); 
        
        #cursor de la db
        cur = mysql.connection.cursor()
        
        #insercion de cliente
        if cliente == 'on':
            
            #logo
            file_path = logo_cliente(nombre_comercial, logo)
            
            
            cur.execute("select *from cliente where razonSocialCliente = %s", (razon,))
            similitud1 = cur.fetchall(); 
            if similitud1:
                flash("Razón social ya existe en nuestro sistema")
                return redirect(url_for('Register.register'))
            
            cur.execute("select *from cliente where telefonoCliente = %s", (telefono,))    
            similitud2 = cur.fetchall(); 
            if similitud2:
                flash("Teléfono ya existe en nuestro sistema")
                return redirect(url_for('Register.register'))
            
            cur.execute("select *from cliente where gmailCliente = %s", (correo,))    
            similitud3 = cur.fetchall(); 
            if similitud3:
                flash("Correo ya existe en nuestro sistema")
                return redirect(url_for('Register.register'))
            
            #insercion del usuario
            cur.execute('insert into cliente(nombreComercialCliente, razonSocialCliente, telefonoCliente, gmailCliente, direcionCliente, descripcionCliente, logoCliente, contrasenaCliente) value (%s, %s, %s, %s, %s, %s, %s, %s)',
                    (nombre_comercial, razon, telefono, correo, direccion, descripcion, file_path, contraseña_cifrada))
            mysql.connection.commit()
            
            cur.execute("select *from cliente where gmailCliente = %s", (correo,)); 
            consulta_new_user = cur.fetchone(); 
            
            session['datos_cliente'] = {
                        'idCliente' : consulta_new_user[0],
                        'nombreComercialCliente' : consulta_new_user[1],
                        'razonSocialCliente': consulta_new_user[2],
                        'telefonoCliente' : consulta_new_user[3], 
                        'gmailCliente': consulta_new_user[4],
                        'direcionCliente' : consulta_new_user[5],  
                        'descripcionCliente' : consulta_new_user[6],   
                        'logoCliente' : consulta_new_user[7], 
                        'contrasenaCliente' : consulta_new_user[8],                
                        'estadoCliente' : consulta_new_user[9]
                    }
            
            
            return redirect(url_for('Cliente.ui_cliente'))    
        
        if empresa_fumigadora == 'on':
            #logo
            file_path = logo_empresa_fumigadora(nombre_comercial,logo); 
            
            #foto_encargado
            file_path_encargado = foto_encargado(encargado_nombre, fotoEncargados); 
            
            
            #nit
            cur.execute("select *from empresafumigadora where nitEmpresaFumigadora = %s" , (nit,))
            similitud1 = cur.fetchall(); 
            if similitud1:
                flash("Nit ya existente en el sistema"); 
                return redirect(url_for('Register.register')); 
            
            #telefono
            cur.execute("select *from empresafumigadora where telefonoEmpresaFumigadora = %s", (telefono,)); 
            similitud2 = cur.fetchall(); 
            if similitud2:
                flash("Teléfono ya existente en el sistema"); 
                return redirect(url_for('Register.register')); 
            
            #gmail
            cur.execute("select *from empresafumigadora where gmailEmpresaFumigadora = %s", (correo,)); 
            similitud3 = cur.fetchall(); 
            if similitud3:
                flash("Correo ya existente en el sistema"); 
                return redirect(url_for('Register.register')); 
            
            #encargado correo
            cur.execute("select *from empresafumigadora where gmailEncargadoEmpresaFumigadora = %s", (encargado_correo,)); 
            similitud4 = cur.fetchall(); 
            if similitud4:
                flash("Correo ya existente en el sistema"); 
                return redirect(url_for('Register.register')); 
            
            #encargado telefono
            cur.execute("select *from empresafumigadora where telefonoEncargadoEmpresaFumigadora = %s", (encargado_telefono,)); 
            similitud5 = cur.fetchall(); 
            if similitud5:
                flash("Teléfono ya existente en el sistema"); 
                return redirect(url_for('Register.register')); 
            
            
            #sesion
            
            cur.execute('insert into empresafumigadora(fotoLogoEmpresaFumigadora, nitEmpresaFumigadora, nombreEmpresaFumigadora, direccionEmpresaFumigadora, departamentoEmpresaFumigadora, contrasenaEmpresaFumigadora, descripcionEmpresaFumigadora, telefonoEmpresaFumigadora, gmailEmpresaFumigadora, nombreEncargadoEmpresaFumigadora, gmailEncargadoEmpresaFumigadora, telefonoEncargadoEmpresaFumigadora, fotoEncargadoEmpresaFumigadora) value(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                        (file_path, nit,nombre_comercial,direccion, departamento, contraseña_cifrada, descripcion, telefono, correo, encargado_nombre, encargado_correo, encargado_telefono, file_path_encargado))
            mysql.connection.commit()
            
            cur.execute("select *from empresafumigadora where gmailEmpresaFumigadora = %s", (correo,)); 
            consulta_new_user = cur.fetchone(); 
            
            session['datos_cliente'] = {
                        'id_cliente' : consulta_new_user[0],
                        'file_path' : consulta_new_user[1],
                        'nit': consulta_new_user[2],
                        'nombre_comercial' : consulta_new_user[3], 
                        'direccion': consulta_new_user[4],
                        'departamento' : consulta_new_user[5],  
                        'contraseña_cifrada' : consulta_new_user[6],   
                        'descripcion' : consulta_new_user[7], 
                        'telefono' : consulta_new_user[8],                
                        'correo' : consulta_new_user[9], 
                        'encargado_nombre' : consulta_new_user[10], 
                        'encargado_correo' : consulta_new_user[11],
                        'encargado_telefono' : consulta_new_user[12], 
                        'file_path_encargado' : consulta_new_user[13],
                        'estado' : consulta_new_user[14]
                    }
            
            cur.execute("insert into rentaSoftware(idEmpresaFumigadoraFk) value(%s)", (session['datos_cliente']['id_cliente'],))
            mysql.connection.commit()

        
            return redirect(url_for('Empresa_fumigadora.ui_empresa_fumigadora_index'))
        

    return 'Método no permitido', 405

