from . import Recuperar_password
from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash; 

@Recuperar_password.route('/Recuperar_password')
def recuperar_password():
    return render_template('/Recuperar_password.html')

#cambiar contraseña
@Recuperar_password.route('/Cambiar_contraseña', methods=['POST'])
def Cambiar_contraseña():
    from app import mysql
    if request.method == 'POST':
        #inpus
        correo_usuario = request.form['correo_usuario']; 
        contraseña_nueva = request.form['contraseña_nueva']; 
        verificar_contraseña = request.form['verificar_contraseña']; 
        rol = request.form['rol']
        
        #conexion
        cur = mysql.connection.cursor()
        
        if rol == 'Empresa_fumigadora':
            cur.execute('select *from empresafumigadora where gmailEmpresaFumigadora = %s', (correo_usuario,));
            consulta2 = cur.fetchone()
            
            if consulta2:
                if contraseña_nueva == verificar_contraseña:
                    contraseña_cifrada = generate_password_hash(contraseña_nueva, 'pbkdf2:sha256:5', 5)
                    cur.execute('UPDATE empresafumigadora SET contrasenaEmpresaFumigadora = %s WHERE gmailEmpresaFumigadora = %s', (contraseña_cifrada, correo_usuario))
                    cur.connection.commit()
                    return redirect(url_for('Login.login'))
                else:
                    flash("Las dos contraseñas son diferentes")
                    return redirect(url_for('Recuperar_password.recuperar_password'))
            else:
                flash("Este correo no se encuentra en el sistema"); 
                return redirect(url_for('Recuperar_password.recuperar_password'))
            
        elif rol == 'Empleado':
            cur.execute('select *from empleado where correoEmpresarialEmpleado = %s', (correo_usuario,));
            consulta3 = cur.fetchone()
            
            if consulta3:
                if contraseña_nueva == verificar_contraseña:
                    contraseña_cifrada = generate_password_hash(contraseña_nueva, 'pbkdf2:sha256:5', 5)
                    cur.execute('UPDATE empleado SET contrasenaEmpleado = %s WHERE correoEmpresarialEmpleado = %s', (contraseña_cifrada, correo_usuario))
                    cur.connection.commit()
                    return redirect(url_for('Login.login'))
                else:
                    flash("Las dos contraseñas son diferentes")
                    return redirect(url_for('Recuperar_password.recuperar_password'))
            else:
                flash("Este correo no se encuentra en el sistema"); 
                return redirect(url_for('Recuperar_password.recuperar_password'))
        
        elif rol =='Cliente':
            cur.execute('select *from cliente where gmailCliente = %s', (correo_usuario,)); 
            consulta1 = cur.fetchone()
            
            if consulta1:
                if contraseña_nueva == verificar_contraseña:
                    contraseña_cifrada = generate_password_hash(contraseña_nueva, 'pbkdf2:sha256:5', 5)
                    cur.execute('UPDATE cliente SET contrasenaCliente = %s WHERE gmailCliente = %s',(contraseña_cifrada, correo_usuario))
                    cur.connection.commit()
                    return redirect(url_for('Login.login'))
                else:
                    flash("Las dos contraseñas son diferentes")
                    return redirect(url_for('Recuperar_password.recuperar_password'))
            else:
                flash("Este correo no se encuentra en el sistema"); 
                return redirect(url_for('Recuperar_password.recuperar_password'))
        
        elif rol =='Sede_cliente':
            cur.execute('select *from sedescliente where gmailSedeCliente = %s', (correo_usuario,));
            consulta4 = cur.fetchone()
            
            if consulta4:
                if contraseña_nueva == verificar_contraseña:
                    contraseña_cifrada = generate_password_hash(contraseña_nueva, 'pbkdf2:sha256:5', 5)
                    cur.execute('UPDATE sedescliente SET contrasenaSedeCliente = %s WHERE gmailSedeCliente = %s', (contraseña_cifrada, correo_usuario))
                    cur.connection.commit()
                    return redirect(url_for('Login.login'))
                else:
                    flash("Las dos contraseñas son diferentes")
                    return redirect(url_for('Recuperar_password.recuperar_password'))
            else:
                flash("Este correo no se encuentra en el sistema"); 
                return redirect(url_for('Recuperar_password.recuperar_password'))
        
    return redirect(url_for('Recuperar_password.recuperar_password'))


