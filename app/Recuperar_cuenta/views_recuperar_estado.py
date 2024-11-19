from . import Activar_cuenta
from flask import render_template, url_for, redirect, request, flash
from werkzeug.security import check_password_hash

@Activar_cuenta.route('/acceso_for_recuperar')
def activar_cuenta_view(): 
    return render_template('/Recuperar_usuario.html')

@Activar_cuenta.route('/funcion_editar_cuenta', methods=['POST'])
def editar_cuenta():
    rol = request.form['rol']
    correo = request.form['correo_usuario']
    contraseña = request.form['contraseña_nueva']

    from app import mysql;

    cur = mysql.connection.cursor(); 

    

    if rol == 'Empresa_fumigadora':
        cur.execute("select contrasenaEmpresaFumigadora from empresaFumigadora where gmailEmpresaFumigadora = %s", (correo,))
        consulta1 = cur.fetchone(); 
        if consulta1:
            contraseña_nueva= check_password_hash(consulta1[0], contraseña)
            print(contraseña_nueva)
            if contraseña_nueva == True:
                cur.execute("update empresaFumigadora set estadoEmpresa = True where gmailEmpresaFumigadora = %s" , (correo,))
                cur.connection.commit(); 
                return redirect(url_for("Login.login"))
            else:
                flash("contraseña incorrecta")
                return render_template('/Recuperar_usuario.html')
        else:
            flash("Correo incorrecto")
            return render_template('/Recuperar_usuario.html')
        
    elif rol == 'Empleado':
        cur.execute("select contrasenaEmpleado from empleado where correoEmpresarialEmpleado = %s", (correo,))
        consulta1 = cur.fetchone(); 
        if consulta1:
            contraseña_nueva= check_password_hash(consulta1[0], contraseña)
            if contraseña_nueva == True:
                cur.execute("update empleado set estadoEmpleado = True where correoEmpresarialEmpleado = %s" , (correo,))
                cur.connection.commit(); 
                return redirect(url_for("Login.login"))
            else:
                flash("contraseña incorrecta")
                return render_template('/Recuperar_usuario.html')
        else:
            flash("Correo incorrecto")
            return render_template('/Recuperar_usuario.html')
        
    elif rol == 'Cliente':
        cur.execute("select contrasenaCliente from cliente where gmailCliente = %s", (correo,))
        consulta1 = cur.fetchone(); 
        if consulta1:
            contraseña_nueva= check_password_hash(consulta1[0], contraseña)
            if contraseña_nueva == True:
                cur.execute("update cliente set estadoCliente = True where gmailCliente = %s" , (correo,))
                cur.connection.commit(); 
                return redirect(url_for("Login.login"))
            else:
                flash("contraseña incorrecta")
                return render_template('/Recuperar_usuario.html')
        else:
            flash("Correo incorrecto")
            return render_template('/Recuperar_usuario.html')
        
    elif rol == 'Sede_cliente':
        cur.execute("select contrasenaSedeCliente from sedesCliente where gmailSedeCliente = %s", (correo,))
        consulta1 = cur.fetchone(); 
        if consulta1:
            contraseña_nueva= check_password_hash(consulta1[0], contraseña)
            if contraseña_nueva == True:
                cur.execute("update cliente set estadoSede = True where gmailSedeCliente = %s" , (correo,))
                cur.connection.commit(); 
                return redirect(url_for("Login.login"))
            else:
                flash("contraseña incorrecta")
                return render_template('/Recuperar_usuario.html')
        else:
            flash("Correo incorrecto")
            return render_template('/Recuperar_usuario.html')
        

    return render_template('/Recuperar_usuario.html')





 