
from . import Login;
from flask import render_template, request, redirect, url_for, flash, session;
from werkzeug.security import check_password_hash; 


@Login.route('/Login')
def login():
    return render_template('/Login.html')

#inicar sesion
@Login.route('/Iniciar_sesion', methods=['POST'])
def iniciar_sesion():
    from app import mysql
    if request.method == 'POST':
        rol = request.form['rol']
        email = request.form['correo']; 
        password = request.form['contraseña']; 
        
        print(rol)
        #conexion
        cur = mysql.connection.cursor()
        
        
        if rol == 'Empresa_fumigadora':
            cur.execute('select *from empresafumigadora where gmailEmpresaFumigadora = %s', (email,));
            consulta2 = cur.fetchone()
            
            if consulta2:
                contraseña_db = consulta2[6] 
                if check_password_hash(contraseña_db, password): 
                    session['datos_cliente'] = {
                        'id_cliente' : consulta2[0],
                        'file_path' : consulta2[1],
                        'nit': consulta2[2],
                        'nombre_comercial' : consulta2[3], 
                        'direccion': consulta2[4],
                        'departamento' : consulta2[5],  
                        'contraseña_cifrada' : consulta2[6],   
                        'descripcion' : consulta2[7], 
                        'telefono' : consulta2[8],                
                        'correo' : consulta2[9], 
                        'encargado_nombre' : consulta2[10], 
                        'encargado_correo' : consulta2[11],
                        'encargado_telefono' : consulta2[12], 
                        'file_path_encargado' : consulta2[13],
                        'estado' : consulta2[14]
                    }
                    
                    if session['datos_cliente']['estado'] == False:
                        flash('Cuenta inactiva')
                        return redirect(url_for('Login.login'))
                    
                    return redirect(url_for('Empresa_fumigadora.ui_empresa_fumigadora_index'))
                else:
                    flash('Contraseña incorrecta.')
                    return redirect(url_for('Login.login'))
            else:
                flash('Correo inexistente.')
                return redirect(url_for('Login.login'))
            
        elif rol == 'Empleado':
            cur.execute('select *from empleado where correoEmpresarialEmpleado = %s', (email,));
            consulta3 = cur.fetchone()
            
            if consulta3:
                contraseña_db = consulta3[6] 
                if check_password_hash(contraseña_db, password): 
                    session['datos_cliente']={
                        'idEmpleado' : consulta3[0],
                        'nombresEmpleado' : consulta3[1],
                        'apellidosEmpleado' : consulta3[2],
                        'numeroTelefonicoEmpleado' : consulta3[3],
                        'correoEmpresarialEmpleado' : consulta3[4],
                        'correoPersonalEmpleado' : consulta3[5],
                        'contrasenaEmpleado' : consulta3[6],
                        'estadoEmpleado' : consulta3[7],
                        'idEmpresaFumigadoraFk' : consulta3[8]
                    }
                    
                    if session['datos_cliente']['estadoEmpleado'] == False:
                        flash('Cuenta inactiva')
                        return redirect(url_for('Login.login'))
                    
                    return redirect(url_for('Emp_empresa_fumigadora.Emp_empre_ui'))
                else:
                    flash('Contraseña incorrecta.')
                    return redirect(url_for('Login.login'))
            else:
                flash('Correo inexistente.')
                return redirect(url_for('Login.login'))
        
        elif rol =='Cliente':
            cur.execute('select *from cliente where gmailCliente = %s', (email,)); 
            consulta1 = cur.fetchone()
            
            if consulta1:
                contraseña_db = consulta1[8] 
                if check_password_hash(contraseña_db, password) == True: 
                    session['datos_cliente']={
                        'idCliente' : consulta1[0],
                        'nombreComercialCliente' : consulta1[1],
                        'razonSocialCliente' : consulta1[2],
                        'telefonoCliente' : consulta1[3],
                        'gmailCliente' : consulta1[4],
                        'direcionCliente' : consulta1[5],
                        'descripcionCliente' : consulta1[6],
                        'logoCliente' : consulta1[7],
                        'contrasenaCliente' : consulta1[8],
                        'estadoCliente' : consulta1[9]
                    }
                    
                    if session['datos_cliente']['estadoCliente'] == False:
                        flash('Cuenta inactiva')
                        return redirect(url_for('Login.login'))
                    
                    return redirect(url_for('Cliente.ui_cliente'))
                else:
                    flash('Contraseña incorrecta.')
                    return redirect(url_for('Login.login'))
            else:
                flash('Correo inexistente.')
                return redirect(url_for('Login.login'))
            
        
        elif rol =='Sede_cliente':
            cur.execute('select *from sedescliente where gmailSedeCliente = %s', (email,));
            consulta4 = cur.fetchone()
            
            if consulta4: 
                contraseña_db = consulta4[5] 
                if check_password_hash(contraseña_db, password): 
                    session['datos_cliente']={
                        'idSedeCliente ' : consulta4[0],
                        'nitSedeCliente ' : consulta4[1],
                        'nombreSedeCliente ' : consulta4[2],
                        'direccionSedeCliente ' : consulta4[3],
                        'gmailSedeCliente ' : consulta4[4],
                        'contrasenaSedeCliente ' : consulta4[5],
                        'telefonoSedeCliente ' : consulta4[6],
                        'departamentoSedeCliente ' : consulta4[7],
                        'logoSedeCliente ': consulta4[8],
                        'nombreEncargadoSedeCliente ' : consulta4[9],
                        'telefonoEncargadoSedeCliente ' : consulta4[10],
                        'gmailEncargadoSedeCliente ' : consulta4[11],
                        'fotoEncargadoSedeCliente ' : consulta4[12],
                        'idClienteFk ' : consulta4[13],
                        'estadoSede' : consulta4[14]
                    }
                    
                    if session['datos_cliente']['estadoSede'] == False:
                        flash('Cuenta inactiva')
                        return redirect(url_for('Login.login'))
                    
                    return redirect(url_for('Sede_cliente.sede_cliente_ui'))
                else:
                    flash('Contraseña incorrecta.')
                    return redirect(url_for('Login.login'))
            else:
                flash('Correo inexistente.')
                return redirect(url_for('Login.login'))
        
    flash('problema al inciar sesion')
    return redirect(url_for('Login.login')); 


#Funcion de cierre de sesion
@Login.route('/Logout',)
def cerrar_sesion():
    session.clear()
    return redirect(url_for('Index.home'))

