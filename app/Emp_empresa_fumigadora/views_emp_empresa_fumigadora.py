from . import Emp_empresa_fumigadora
from flask import render_template, redirect, url_for, flash, request, session
from flask import session
from app.config import configracion_base
from datetime import datetime

secret_key = configracion_base.SECRET_KEY

# PLANTILLA
@Emp_empresa_fumigadora.route('/Emp_empre_plantilla')
def Emp_empre_plantilla():
    from app import mysql

    # OBTENER EL FK DE EMPRESA_FUMIGADORA
    idEmpresaFumigadoraFk = session.get('datos_cliente', {}).get('idEmpresaFumigadoraFk', None)

    if not idEmpresaFumigadoraFk:
        # EN CASO DE NO HABER FK EMPRESA FUMIGADORA
        return "Error: Empresa Fumigadora no asignada a este empleado", 400

    # CONECTAR A LA BASE DE DATOS Y RECIBIR NOMBRE_EMPRESA Y LOGO
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT nombreEmpresaFumigadora, fotoLogoEmpresaFumigadora 
        FROM empresafumigadora 
        WHERE idEmpresaFumigadora = %s;
    """, (idEmpresaFumigadoraFk,))
    resultado = cur.fetchone()
    cur.close()

    if not resultado:
        # EN CASO DE NO HABER RESULTADOS
        return "Error: No se encontraron datos para esta empresa fumigadora", 404

    # ASIGNAR VALORES DESDE LOS RESULTADOS
    nombre_empresa = resultado[0]
    logo_empresa_fumigadora = resultado[1]

    # CONTEXTO
    context = {
        'idEmpleado': session.get('datos_cliente', {}).get('idEmpleado', 'Id_empleado_inexistente'),
        'nombresEmpleado': session.get('datos_cliente', {}).get('nombresEmpleado', 'nombre_inexistente'),
        'apellidosEmpleado': session.get('datos_cliente', {}).get('apellidosEmpleado', 'apellido_inexistente'),
        'numeroTelefonicoEmpleado': session.get('datos_cliente', {}).get('numeroTelefonicoEmpleado', 'telefono_inexistente'),
        'correoEmpresarialEmpleado': session.get('datos_cliente', {}).get('correoEmpresarialEmpleado', 'correo_empresarial_inexistente'),
        'correoPersonalEmpleado': session.get('datos_cliente', {}).get('correoPersonalEmpleado', 'correo_personal_inexistente'),
        'contrasenaEmpleado': session.get('datos_cliente', {}).get('contrasenaEmpleado', 'contraseña_inexistente'),
        'idEmpresaFumigadoraFk': idEmpresaFumigadoraFk,
        'estadoEmpleado': session.get('datos_cliente', {}).get('estadoEmpleado', 'Estado_empleado_inexistente'),
        'nombreEmpresaFumigadora': nombre_empresa,  # Agregar el nombre de la empresa
        'logoEmpresaFumigadora': logo_empresa_fumigadora  # Agregar el logo de la empresa
    }
    return render_template('emp_empresa_fumigadora/Emp_empre_plantilla.html', **context)
    


# PÁGINA DE BIENVENIDA
@Emp_empresa_fumigadora.route('/Emp_empre_ui')
def Emp_empre_ui():
    from app import mysql

    # OBTENER EL FK DE EMPRESA_FUMIGADORA
    idEmpresaFumigadoraFk = session.get('datos_cliente', {}).get('idEmpresaFumigadoraFk', None)

    if not idEmpresaFumigadoraFk:
        # EN CASO DE NO HABER FK EMPRESA FUMIGADORA
        return "Error: Empresa Fumigadora no asignada a este empleado", 400

    # CONECTAR A LA BASE DE DATOS Y RECIBIR NOMBRE_EMPRESA Y LOGO
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT nombreEmpresaFumigadora, fotoLogoEmpresaFumigadora 
        FROM empresafumigadora 
        WHERE idEmpresaFumigadora = %s;
    """, (idEmpresaFumigadoraFk,))
    resultado = cur.fetchone()
    cur.close()

    if not resultado:
        # EN CASO DE NO HABER RESULTADOS
        return "Error: No se encontraron datos para esta empresa fumigadora", 404

    # ASIGNAR VALORES DESDE LOS RESULTADOS
    nombre_empresa = resultado[0]
    logo_empresa_fumigadora = resultado[1]

    # CONTEXTO
    context = {
        'idEmpleado': session.get('datos_cliente', {}).get('idEmpleado', 'Id_empleado_inexistente'),
        'nombresEmpleado': session.get('datos_cliente', {}).get('nombresEmpleado', 'nombre_inexistente'),
        'apellidosEmpleado': session.get('datos_cliente', {}).get('apellidosEmpleado', 'apellido_inexistente'),
        'numeroTelefonicoEmpleado': session.get('datos_cliente', {}).get('numeroTelefonicoEmpleado', 'telefono_inexistente'),
        'correoEmpresarialEmpleado': session.get('datos_cliente', {}).get('correoEmpresarialEmpleado', 'correo_empresarial_inexistente'),
        'correoPersonalEmpleado': session.get('datos_cliente', {}).get('correoPersonalEmpleado', 'correo_personal_inexistente'),
        'contrasenaEmpleado': session.get('datos_cliente', {}).get('contrasenaEmpleado', 'contraseña_inexistente'),
        'idEmpresaFumigadoraFk': idEmpresaFumigadoraFk,
        'estadoEmpleado': session.get('datos_cliente', {}).get('estadoEmpleado', 'Estado_empleado_inexistente'),
        'nombreEmpresaFumigadora': nombre_empresa,  # Agregar el nombre de la empresa
        'logoEmpresaFumigadora': logo_empresa_fumigadora  # Agregar el logo de la empresa
    }

    return render_template('emp_empresa_fumigadora/Emp_empre_ui.html', **context)


# PÁGINA DE INFORMACIÓN DEL EMPLEADO 
@Emp_empresa_fumigadora.route('/Emp_empre_info')
def emp_empre_info():
    from app import mysql

    # OBTENER EL FK DE EMPRESA_FUMIGADORA
    idEmpresaFumigadoraFk = session.get('datos_cliente', {}).get('idEmpresaFumigadoraFk', None)

    if not idEmpresaFumigadoraFk:
        # EN CASO DE NO HABER FK EMPRESA FUMIGADORA
        return "Error: Empresa Fumigadora no asignada a este empleado", 400

    # OBTENER ID DEL EMPLEADO DESDE LA SESIÓN
    idEmpleado = session.get('datos_cliente', {}).get('idEmpleado', 'id_inexistente')

    # CONECTAR A LA BASE DE DATOS Y RECIBIR NOMBRE_EMPRESA Y LOGO
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT nombreEmpresaFumigadora, fotoLogoEmpresaFumigadora 
        FROM empresafumigadora 
        WHERE idEmpresaFumigadora = %s;
    """, (idEmpresaFumigadoraFk,))
    resultado_empresa = cur.fetchone()

    if not resultado_empresa:
        # EN CASO DE NO HABER RESULTADOS
        return "Error: No se encontraron datos para esta empresa fumigadora", 404


    # ASIGNAR VALORES DESDE LOS RESULTADOS
    nombre_empresa = resultado_empresa[0]
    logo_empresa_fumigadora = resultado_empresa[1]

    # CONTEXTO
    context = {
        'idEmpleado': idEmpleado,
        'nombresEmpleado': session.get('datos_cliente', {}).get('nombresEmpleado', 'nombre_inexistente'),
        'apellidosEmpleado': session.get('datos_cliente', {}).get('apellidosEmpleado', 'apellido_inexistente'),
        'numeroTelefonicoEmpleado': session.get('datos_cliente', {}).get('numeroTelefonicoEmpleado', 'telefono_inexistente'),
        'correoEmpresarialEmpleado': session.get('datos_cliente', {}).get('correoEmpresarialEmpleado', 'correo_empresarial_inexistente'),
        'correoPersonalEmpleado': session.get('datos_cliente', {}).get('correoPersonalEmpleado', 'correo_personal_inexistente'),
        'idEmpresaFumigadoraFk': idEmpresaFumigadoraFk,
        'estadoEmpleado': session.get('datos_cliente', {}).get('estadoEmpleado', 'Estado_empleado_inexistente'),
        'nombreEmpresaFumigadora': nombre_empresa,  
        'logoEmpresaFumigadora': logo_empresa_fumigadora 
    }

    return render_template('emp_empresa_fumigadora/Emp_empre_info.html', **context)



# PÁGINA PARA EDITAR INFORMACIÓN DEL EMPLEADO
@Emp_empresa_fumigadora.route('/Emp_empre_edit', methods=['GET', 'POST'])
def emp_empre_edit():
    from app import mysql

    # OBTENER EL FK DE EMPRESA_FUMIGADORA
    idEmpresaFumigadoraFk = session.get('datos_cliente', {}).get('idEmpresaFumigadoraFk', None)

    if not idEmpresaFumigadoraFk:
        flash("Error: Empresa Fumigadora no asignada a este empleado", 'error')
        return redirect(url_for('Emp_empresa_fumigadora.emp_empre_edit'))

    idEmpleado = session.get('datos_cliente', {}).get('idEmpleado', None)
    
    if not idEmpleado:
        flash("Error: Empleado no encontrado en la sesión", 'error')
        return redirect(url_for('Emp_empresa_fumigadora.emp_empre_edit'))

    if request.method == 'POST':
        # OBTENER LOS DATOS
        nombre_empleado = request.form.get('empleado_nombre')
        apellido_empleado = request.form.get('empleado_apellido')
        telefono = request.form.get('telefono')
        correo_personal = request.form.get('correo_personal')
        correo_empresarial = request.form.get('correo_empresarial')

        # VERIFICAR QUE NO EXITAN LOS CORREOS
        cur = mysql.connection.cursor()

        # VERIFICAR EL CORREO EMPRESARIAL QUE SEA UNICO
        cur.execute("""
            SELECT idEmpleado FROM empleado WHERE correoEmpresarialEmpleado = %s AND idEmpleado != %s
        """, (correo_empresarial, idEmpleado))
        correo_empresarial_existe = cur.fetchone()
        
        if correo_empresarial_existe:
            flash("El correo empresarial ya está en uso por otro empleado.", 'error')
            return redirect(url_for('Emp_empresa_fumigadora.emp_empre_edit'))

        # VERIFICAR EL CORREO PERSONAL QUE SEA UNICO
        cur.execute("""
            SELECT idEmpleado FROM empleado WHERE correoPersonalEmpleado = %s AND idEmpleado != %s
        """, (correo_personal, idEmpleado))
        correo_personal_existe = cur.fetchone()
        
        if correo_personal_existe:
            flash("El correo personal ya está en uso por otro empleado.", 'error')
            return redirect(url_for('Emp_empresa_fumigadora.emp_empre_edit'))

        # ACTUALIZAR LOS DATOS
        cur.execute("""
            UPDATE empleado
            SET nombresEmpleado = %s, apellidosEmpleado = %s, 
                numeroTelefonicoEmpleado = %s, correoPersonalEmpleado = %s, 
                correoEmpresarialEmpleado = %s
            WHERE idEmpleado = %s;
        """, (
            nombre_empleado, 
            apellido_empleado, 
            telefono, 
            correo_personal, 
            correo_empresarial,  
            idEmpleado
        ))

        mysql.connection.commit()

        # ACTUALIZAR LA SESSION CON LOS DATOS NUEVOS
        session['datos_cliente']['nombresEmpleado'] = nombre_empleado
        session['datos_cliente']['apellidosEmpleado'] = apellido_empleado
        session['datos_cliente']['numeroTelefonicoEmpleado'] = telefono
        session['datos_cliente']['correoPersonalEmpleado'] = correo_personal
        session['datos_cliente']['correoEmpresarialEmpleado'] = correo_empresarial

        flash("Información actualizada exitosamente", 'success')
        return redirect(url_for('Emp_empresa_fumigadora.emp_empre_actualizacion'))

    # MOSTRAR PAGINA CON DATOS ACTUALES
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT nombreEmpresaFumigadora, fotoLogoEmpresaFumigadora 
        FROM empresafumigadora 
        WHERE idEmpresaFumigadora = %s;
    """, (idEmpresaFumigadoraFk,))
    
    resultado = cur.fetchone()
    cur.close()

    if not resultado:
        flash("Error: No se encontraron datos para esta empresa fumigadora", 'error')
        return redirect(url_for('Emp_empresa_fumigadora.emp_empre_edit'))

    nombre_empresa = resultado[0]
    logo_empresa_fumigadora = resultado[1]

    # CONTEXTO
    context = {
        'idEmpleado': idEmpleado,
        'logoEmpresaFumigadora': logo_empresa_fumigadora,
        'nombresEmpleado': session.get('datos_cliente', {}).get('nombresEmpleado', 'Nombre no encontrado'),
        'apellidosEmpleado': session.get('datos_cliente', {}).get('apellidosEmpleado', 'Apellido no encontrado'),
        'numeroTelefonicoEmpleado': session.get('datos_cliente', {}).get('numeroTelefonicoEmpleado', 'Teléfono no encontrado'),
        'correoEmpresarialEmpleado': session.get('datos_cliente', {}).get('correoEmpresarialEmpleado', 'Correo empresarial no encontrado'), 
        'correoPersonalEmpleado': session.get('datos_cliente', {}).get('correoPersonalEmpleado', 'Correo personal no encontrado'),
        'nombreEmpresaFumigadora': nombre_empresa
    }

    return render_template('emp_empresa_fumigadora/Emp_empre_edit.html', **context)

@Emp_empresa_fumigadora.route('/Emp_empre_actualizacion')
def emp_empre_actualizacion():
    from app import mysql
    from flask import session, render_template

    # OBTENER EL FK DE EMPRESA_FUMIGADORA
    id_empresa_fumigadora_fk = session.get('datos_cliente', {}).get('idEmpresaFumigadoraFk')

    if not id_empresa_fumigadora_fk:
        # EN CASO DE NO HABER FK EMPRESA FUMIGADORA
        return "Error: Empresa Fumigadora no asignada a este empleado", 400

    # CONECTAR A LA BASE DE DATOS Y RECIBIR NOMBRE_EMPRESA Y LOGO
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT nombreEmpresaFumigadora, fotoLogoEmpresaFumigadora 
        FROM empresafumigadora 
        WHERE idEmpresaFumigadora = %s;
    """, (id_empresa_fumigadora_fk,))
    
    resultado = cur.fetchone()
    cur.close()

    if not resultado:
        # EN CASO DE NO HABER RESULTADOS
        return "Error: No se encontraron datos para esta empresa fumigadora", 404

    # ASIGNAR VALORES DESDE LOS RESULTADOS
    nombre_empresa = resultado[0]
    logo_empresa_fumigadora = resultado[1]

    # CONTEXTO
    context = {
        'idEmpleado': session.get('datos_cliente', {}).get('idEmpleado', 'Id_empleado_inexistente'),
        'nombresEmpleado': session.get('datos_cliente', {}).get('nombresEmpleado', 'nombre_inexistente'),
        'apellidosEmpleado': session.get('datos_cliente', {}).get('apellidosEmpleado', 'apellido_inexistente'),
        'numeroTelefonicoEmpleado': session.get('datos_cliente', {}).get('numeroTelefonicoEmpleado', 'telefono_inexistente'),
        'correoEmpresarialEmpleado': session.get('datos_cliente', {}).get('correoEmpresarialEmpleado', 'correo_empresarial_inexistente'),
        'correoPersonalEmpleado': session.get('datos_cliente', {}).get('correoPersonalEmpleado', 'correo_personal_inexistente'),
        'contrasenaEmpleado': session.get('datos_cliente', {}).get('contrasenaEmpleado', 'contraseña_inexistente'),
        'idEmpresaFumigadoraFk': id_empresa_fumigadora_fk,
        'estadoEmpleado': session.get('datos_cliente', {}).get('estadoEmpleado', 'Estado_empleado_inexistente'),
        'nombreEmpresaFumigadora': nombre_empresa,  # Agregar el nombre de la empresa
        'logoEmpresaFumigadora': logo_empresa_fumigadora  # Agregar el logo de la empresa
    }

    return render_template('emp_empresa_fumigadora/Emp_empre_actualizacion.html', **context)




# PÁGINA PARA ELIMINAR CUENTA
@Emp_empresa_fumigadora.route('/Emp_empre_borrar', methods=['GET', 'POST'])
def emp_empre_borrar():
    from app import mysql

    # OBTENER EL FK DE EMPRESA_FUMIGADORA
    idEmpresaFumigadoraFk = session.get('datos_cliente', {}).get('idEmpresaFumigadoraFk', None)
    idEmpleado = session.get('datos_cliente', {}).get('idEmpleado', None)

    if not idEmpresaFumigadoraFk:
        # EN CASO DE NO HABER FK EMPRESA Fumigadora
        return "Error: Empresa Fumigadora no asignada a este empleado", 400

    if not idEmpleado:
        flash("Error: Empleado no encontrado", 'error')
        return redirect(url_for('Emp_empresa_fumigadora.emp_empre_ui'))

    if request.method == 'POST':
        # Actualizar el estado de la cuenta a inactiva
        cur = mysql.connection.cursor()
        cur.execute("UPDATE empleado SET estadoEmpleado = 0 WHERE idEmpleado = %s;", (idEmpleado,))
        mysql.connection.commit()

        # Limpiar la sesión y redirigir al login
        session.clear()
        flash("Cuenta inactivada exitosamente", 'success')
        return redirect(url_for('Login.login'))

    # Obtener el nombre de la empresa y el logo
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT nombreEmpresaFumigadora, fotoLogoEmpresaFumigadora 
        FROM empresafumigadora 
        WHERE idEmpresaFumigadora = %s;
    """, (idEmpresaFumigadoraFk,))
    resultado = cur.fetchone()
    cur.close()

    if not resultado:
        return "Error: No se encontraron datos para esta empresa fumigadora", 404

    # Asignar los valores desde los resultados
    nombre_empresa = resultado[0]  # Nombre de la empresa
    logo_empresa_fumigadora = resultado[1]  # Ruta del logo de la empresa

    # Contexto para el template
    context = {
        'idEmpleado': idEmpleado,
        'logoEmpresaFumigadora': logo_empresa_fumigadora,
        'nombresEmpleado': session.get('datos_cliente', {}).get('nombresEmpleado', 'nombre_inexistente'),
        'apellidosEmpleado': session.get('datos_cliente', {}).get('apellidosEmpleado', 'apellido_inexistente'),
        'numeroTelefonicoEmpleado': session.get('datos_cliente', {}).get('numeroTelefonicoEmpleado', 'telefono_inexistente'),
        'correoEmpresarialEmpleado': session.get('datos_cliente', {}).get('correoEmpresarialEmpleado', 'correo_empresarial_inexistente'), 
        'correoPersonalEmpleado': session.get('datos_cliente', {}).get('correoPersonalEmpleado', 'correo_personal_inexistente'),
        'contrasenaEmpleado': session.get('datos_cliente', {}).get('contrasenaEmpleado', 'contraseña_inexistente'),
        'idEmpresaFumigadoraFk': idEmpresaFumigadoraFk,
        'estadoEmpleado': session.get('datos_cliente', {}).get('estadoEmpleado', 'Estado_empleado_inexistente'),
        'nombreEmpresaFumigadora': nombre_empresa
    }

    return render_template('emp_empresa_fumigadora/Emp_empre_borrar.html', **context)




 
# PÁGINA DE DETALLES DE SERVICIO 
@Emp_empresa_fumigadora.route('/Emp_empre_detall')
def emp_empre_detall():
    from app import mysql

    # OBTENER EL FK DE EMPRESA_FUMIGADORA
    idEmpresaFumigadoraFk = session.get('datos_cliente', {}).get('idEmpresaFumigadoraFk', None)

    if not idEmpresaFumigadoraFk:
        # EN CASO DE NO HABER FK EMPRESA FUMIGADORA
        return "Error: Empresa Fumigadora no asignada a este empleado", 400

    # CONECTAR A LA BASE DE DATOS Y RECIBIR NOMBRE_EMPRESA Y LOGO
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT nombreEmpresaFumigadora, fotoLogoEmpresaFumigadora 
        FROM empresafumigadora 
        WHERE idEmpresaFumigadora = %s;
    """, (idEmpresaFumigadoraFk,))
    resultado = cur.fetchone()
    cur.close()

    if not resultado:
        # EN CASO DE NO HABER RESULTADOS
        return "Error: No se encontraron datos para esta empresa fumigadora", 404

    # ASIGNAR VALORES DESDE LOS RESULTADOS
    nombre_empresa = resultado[0]
    logo_empresa_fumigadora = resultado[1]

    # Consulta para obtener los servicios
    cur = mysql.connection.cursor()
    cur.execute(""" 
    SELECT 
        c.idCliente AS id_cliente,
        c.nombreComercialCliente AS cliente,
        s.nombreSedeCliente AS sede,
        cl.nombreClases AS clase,
        car.nombreCaracteristicas AS caracteristica,
        det.valorDetalle AS detalle
    FROM 
        detallesservicio det
    JOIN 
        caracteristicas car ON det.idCaracteristicaFk = car.idCaracteristicas
    JOIN 
        clases cl ON car.idClasesFk = cl.idClases
    JOIN 
        servicio ser ON det.idServicioFk = ser.idServicio
    JOIN 
        sedescliente s ON ser.idSedeClienteFk = s.idSedeCliente
    JOIN 
        cliente c ON s.idClienteFk = c.idCliente
    WHERE 
        s.idClienteFk IN (
            SELECT s.idClienteFk 
            FROM sedescliente s 
            WHERE s.idClienteFk IN (
                SELECT c.idCliente 
                FROM cliente c 
                JOIN sedescliente s ON c.idCliente = s.idClienteFk 
                WHERE s.idClienteFk IN (
                    SELECT e.idEmpleado 
                    FROM empleado e 
                    WHERE e.idEmpresaFumigadoraFk = %s
                )
            )
        );
    """, (idEmpresaFumigadoraFk,))

    # datos para las tablas
    d_servicios = cur.fetchall()
    cur.close()

    # Verificar si hay detalles de servicio
    if not d_servicios:
        return redirect(url_for('Emp_empresa_fumigadora.emp_empre_no_det_servicio'))

    d_servicios_contexto = [
        {
            'id_servicio': detalle[0],
            'nombre_cliente': detalle[1],
            'sede_cliente': detalle[2],
            'clase': detalle[3],
            'caracteristica': detalle[4],
            'detalle': detalle[5],
        }
        for detalle in d_servicios
    ]

    # CONTEXTO
    context = {
        'idEmpleado': session.get('datos_cliente', {}).get('idEmpleado', 'id_inexistente'),
        'logoEmpresaFumigadora': logo_empresa_fumigadora,  # Usar el logo de la empresa como el file_path
        'nombresEmpleado': session.get('datos_cliente', {}).get('nombresEmpleado', 'nombre_inexistente'),
        'apellidosEmpleado': session.get('datos_cliente', {}).get('apellidosEmpleado', 'apellido_inexistente'),
        'numeroTelefonicoEmpleado': session.get('datos_cliente', {}).get('numeroTelefonicoEmpleado', 'telefono_inexistente'),
        'correoEmpresarialEmpleado': session.get('datos_cliente', {}).get('correoEmpresarialEmpleado', 'correo_empresarial_inexistente'), 
        'correoPersonalEmpleado': session.get('datos_cliente', {}).get('correoPersonalEmpleado', 'correo_personal_inexistente'),
        'contrasenaEmpleado': session.get('datos_cliente', {}).get('contrasenaEmpleado', 'contraseña_inexistente'),
        'idEmpresaFumigadoraFk': idEmpresaFumigadoraFk,
        'estadoEmpleado': session.get('datos_cliente', {}).get('estadoEmpleado', 'Estado_empleado_inexistente'),
        'nombreEmpresaFumigadora': nombre_empresa,
        'd_servicios': d_servicios_contexto
    }

    return render_template('emp_empresa_fumigadora/Emp_empre_detall.html', **context)













# PÁGINA DE SERVICIOS
@Emp_empresa_fumigadora.route('/Emp_empre_servi')
def emp_empre_servi():
    from app import mysql

    # OBTENER EL FK DE EMPRESA_FUMIGADORA
    idEmpresaFumigadoraFk = session.get('datos_cliente', {}).get('idEmpresaFumigadoraFk', None)

    if not idEmpresaFumigadoraFk:
        return "Error: Empresa Fumigadora no asignada a este empleado", 400

    # CONECTAR A LA BASE DE DATOS Y RECIBIR NOMBRE_EMPRESA Y LOGO
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT nombreEmpresaFumigadora, fotoLogoEmpresaFumigadora 
        FROM empresafumigadora 
        WHERE idEmpresaFumigadora = %s;
    """, (idEmpresaFumigadoraFk,))
    resultado = cur.fetchone()
    cur.close()

    if not resultado:
        return "Error: No se encontraron datos para esta empresa fumigadora", 404

    # ASIGNAR VALORES DESDE LOS RESULTADOS
    nombre_empresa = resultado[0]
    logo_empresa_fumigadora = resultado[1]

    # Consulta para obtener los servicios
    cur = mysql.connection.cursor()
    cur.execute(""" 
    SELECT c.idCliente, s.nombreSedeCliente, 
           c.descripcionCliente, ser.fechaSolicitudServicio, 
           ser.fechaInicioServicio, ser.fechaFinalServicio, 
           ser.estadoServicio 
    FROM servicio ser 
    JOIN sedescliente s ON ser.idSedeClienteFk = s.idSedeCliente 
    JOIN cliente c ON s.idClienteFk = c.idCliente 
    WHERE s.idClienteFk IN ( 
        SELECT s.idClienteFk 
        FROM sedescliente s 
        WHERE s.idClienteFk IN (
            SELECT c.idCliente 
            FROM cliente c 
            JOIN sedescliente s ON c.idCliente = s.idClienteFk 
            WHERE s.idClienteFk IN (
                SELECT e.idEmpleado 
                FROM empleado e 
                WHERE e.idEmpresaFumigadoraFk = %s
            )
        )
    ); 
""", (idEmpresaFumigadoraFk,))



    # datos para las tablas
    servicios = cur.fetchall()
    cur.close()

     # Verificar si hay detalles de servicio
    if not servicios:
        return redirect(url_for('Emp_empresa_fumigadora.emp_empre_no_servicio'))

    servicios_contexto = [
    {
        'id_cliente': servicio[0],
        'sede': servicio[1],
        'descripcion': servicio[2],
        'solicitud': servicio[3],
        'inicio': servicio[4],
        'fin': servicio[5],
        'estado': servicio[6],
    }
    for servicio in servicios
    ]




    context = {
    'idEmpleado': session.get('datos_cliente', {}).get('idEmpleado', 'id_inexistente'),
    'logoEmpresaFumigadora': logo_empresa_fumigadora,
    'nombresEmpleado': session.get('datos_cliente', {}).get('nombresEmpleado', 'nombre_inexistente'),
    'apellidosEmpleado': session.get('datos_cliente', {}).get('apellidosEmpleado', 'apellido_inexistente'),
    'numeroTelefonicoEmpleado': session.get('datos_cliente', {}).get('numeroTelefonicoEmpleado', 'telefono_inexistente'),
    'correoEmpresarialEmpleado': session.get('datos_cliente', {}).get('correoEmpresarialEmpleado', 'correo_empresarial_inexistente'),
    'correoPersonalEmpleado': session.get('datos_cliente', {}).get('correoPersonalEmpleado', 'correo_personal_inexistente'),
    'contrasenaEmpleado': session.get('datos_cliente', {}).get('contrasenaEmpleado', 'contraseña_inexistente'),
    'idEmpresaFumigadoraFk': idEmpresaFumigadoraFk,
    'estadoEmpleado': session.get('datos_cliente', {}).get('estadoEmpleado', 'Estado_empleado_inexistente'),
    'nombreEmpresaFumigadora': nombre_empresa,
    'servicios': servicios_contexto
}

    return render_template('emp_empresa_fumigadora/Emp_empre_servi.html', **context)




















# PARTE REPORTE

@Emp_empresa_fumigadora.route("/reporte")
def reporte():
    from app import mysql

    # OBTENER EL FK DE EMPRESA_FUMIGADORA
    idEmpresaFumigadoraFk = session.get('datos_cliente', {}).get('idEmpresaFumigadoraFk', None)

    if not idEmpresaFumigadoraFk:
        # EN CASO DE NO HABER FK EMPRESA FUMIGADORA
        return "Error: Empresa Fumigadora no asignada a este empleado", 400

    # CONECTAR A LA BASE DE DATOS Y RECIBIR NOMBRE_EMPRESA Y LOGO
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT nombreEmpresaFumigadora, fotoLogoEmpresaFumigadora 
        FROM empresafumigadora 
        WHERE idEmpresaFumigadora = %s;
    """, (idEmpresaFumigadoraFk,))
    resultado = cur.fetchone()
    cur.close()

    if not resultado:
        # EN CASO DE NO HABER RESULTADOS
        return "Error: No se encontraron datos para esta empresa fumigadora", 404

    # ASIGNAR VALORES DESDE LOS RESULTADOS
    nombre_empresa = resultado[0]
    logo_empresa_fumigadora = resultado[1]

 
    context = {
        'idEmpleado': session.get('datos_cliente', {}).get('idEmpleado', 'Id_empleado_inexistente'),
        'nombresEmpleado': session.get('datos_cliente', {}).get('nombresEmpleado', 'nombre_inexistente'),
        'apellidosEmpleado': session.get('datos_cliente', {}).get('apellidosEmpleado', 'apellido_inexistente'),
        'numeroTelefonicoEmpleado': session.get('datos_cliente', {}).get('numeroTelefonicoEmpleado', 'telefono_inexistente'),
        'correoEmpresarialEmpleado': session.get('datos_cliente', {}).get('correoEmpresarialEmpleado', 'correo_empresarial_inexistente'),
        'correoPersonalEmpleado': session.get('datos_cliente', {}).get('correoPersonalEmpleado', 'correo_personal_inexistente'),
        'contrasenaEmpleado': session.get('datos_cliente', {}).get('contrasenaEmpleado', 'contraseña_inexistente'),
        'idEmpresaFumigadoraFk': idEmpresaFumigadoraFk,
        'estadoEmpleado': session.get('datos_cliente', {}).get('estadoEmpleado', 'Estado_empleado_inexistente'),
        'nombreEmpresaFumigadora': nombre_empresa,  # Agregar el nombre de la empresa
        'logoEmpresaFumigadora': logo_empresa_fumigadora  # Agregar el logo de la empresa
    }
    return render_template("emp_empresa_fumigadora/Reporte.html", **context)

   







# PARTE certificados

@Emp_empresa_fumigadora.route('/certificado')
def certificado():
    from app import mysql

    # OBTENER EL FK DE EMPRESA_FUMIGADORA
    idEmpresaFumigadoraFk = session.get('datos_cliente', {}).get('idEmpresaFumigadoraFk', None)

    if not idEmpresaFumigadoraFk:
        # EN CASO DE NO HABER FK EMPRESA FUMIGADORA
        return "Error: Empresa Fumigadora no asignada a este empleado", 400

    # CONECTAR A LA BASE DE DATOS Y RECIBIR NOMBRE_EMPRESA Y LOGO
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT nombreEmpresaFumigadora, fotoLogoEmpresaFumigadora 
        FROM empresafumigadora 
        WHERE idEmpresaFumigadora = %s;
    """, (idEmpresaFumigadoraFk,))
    resultado = cur.fetchone()
    cur.close()

    if not resultado:
        # EN CASO DE NO HABER RESULTADOS
        return "Error: No se encontraron datos para esta empresa fumigadora", 404

    # ASIGNAR VALORES DESDE LOS RESULTADOS
    nombre_empresa = resultado[0]
    logo_empresa_fumigadora = resultado[1]

    # CONTEXTO
    context = {
        'idEmpleado': session.get('datos_cliente', {}).get('idEmpleado', 'Id_empleado_inexistente'),
        'nombresEmpleado': session.get('datos_cliente', {}).get('nombresEmpleado', 'nombre_inexistente'),
        'apellidosEmpleado': session.get('datos_cliente', {}).get('apellidosEmpleado', 'apellido_inexistente'),
        'numeroTelefonicoEmpleado': session.get('datos_cliente', {}).get('numeroTelefonicoEmpleado', 'telefono_inexistente'),
        'correoEmpresarialEmpleado': session.get('datos_cliente', {}).get('correoEmpresarialEmpleado', 'correo_empresarial_inexistente'),
        'correoPersonalEmpleado': session.get('datos_cliente', {}).get('correoPersonalEmpleado', 'correo_personal_inexistente'),
        'contrasenaEmpleado': session.get('datos_cliente', {}).get('contrasenaEmpleado', 'contraseña_inexistente'),
        'idEmpresaFumigadoraFk': idEmpresaFumigadoraFk,
        'estadoEmpleado': session.get('datos_cliente', {}).get('estadoEmpleado', 'Estado_empleado_inexistente'),
        'nombreEmpresaFumigadora': nombre_empresa,  # Agregar el nombre de la empresa
        'logoEmpresaFumigadora': logo_empresa_fumigadora  # Agregar el logo de la empresa
    }
    #Certificados_descargar.html
    return render_template('emp_empresa_fumigadora/Certificados.html', **context); 















# PÁGINA NO DETALLES SERVICIO

@Emp_empresa_fumigadora.route('Emp_empre_no_det_servicio')
def emp_empre_no_det_servicio():
    from app import mysql

    # OBTENER EL FK DE EMPRESA_FUMIGADORA
    idEmpresaFumigadoraFk = session.get('datos_cliente', {}).get('idEmpresaFumigadoraFk', None)

    if not idEmpresaFumigadoraFk:
        # EN CASO DE NO HABER FK EMPRESA FUMIGADORA
        return "Error: Empresa Fumigadora no asignada a este empleado", 400

    # CONECTAR A LA BASE DE DATOS Y RECIBIR NOMBRE_EMPRESA Y LOGO
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT nombreEmpresaFumigadora, fotoLogoEmpresaFumigadora 
        FROM empresafumigadora 
        WHERE idEmpresaFumigadora = %s;
    """, (idEmpresaFumigadoraFk,))
    resultado = cur.fetchone()
    cur.close()

    if not resultado:
        # EN CASO DE NO HABER RESULTADOS
        return "Error: No se encontraron datos para esta empresa fumigadora", 404

    # ASIGNAR VALORES DESDE LOS RESULTADOS
    nombre_empresa = resultado[0]
    logo_empresa_fumigadora = resultado[1]

    # CONTEXTO
    context = {
        'idEmpleado': session.get('datos_cliente', {}).get('idEmpleado', 'Id_empleado_inexistente'),
        'nombresEmpleado': session.get('datos_cliente', {}).get('nombresEmpleado', 'nombre_inexistente'),
        'apellidosEmpleado': session.get('datos_cliente', {}).get('apellidosEmpleado', 'apellido_inexistente'),
        'numeroTelefonicoEmpleado': session.get('datos_cliente', {}).get('numeroTelefonicoEmpleado', 'telefono_inexistente'),
        'correoEmpresarialEmpleado': session.get('datos_cliente', {}).get('correoEmpresarialEmpleado', 'correo_empresarial_inexistente'),
        'correoPersonalEmpleado': session.get('datos_cliente', {}).get('correoPersonalEmpleado', 'correo_personal_inexistente'),
        'contrasenaEmpleado': session.get('datos_cliente', {}).get('contrasenaEmpleado', 'contraseña_inexistente'),
        'idEmpresaFumigadoraFk': idEmpresaFumigadoraFk,
        'estadoEmpleado': session.get('datos_cliente', {}).get('estadoEmpleado', 'Estado_empleado_inexistente'),
        'nombreEmpresaFumigadora': nombre_empresa,
        'logoEmpresaFumigadora': logo_empresa_fumigadora
    }
    return render_template('emp_empresa_fumigadora/Emp_empre_no_det_servicio.html', **context)



# PÁGINA NO SERVICIOS
@Emp_empresa_fumigadora.route('Emp_empre_no_servicio')
def emp_empre_no_servicio():
    from app import mysql

    # OBTENER EL FK DE EMPRESA_FUMIGADORA
    idEmpresaFumigadoraFk = session.get('datos_cliente', {}).get('idEmpresaFumigadoraFk', None)

    if not idEmpresaFumigadoraFk:
        # EN CASO DE NO HABER FK EMPRESA FUMIGADORA
        return "Error: Empresa Fumigadora no asignada a este empleado", 400

    # CONECTAR A LA BASE DE DATOS Y RECIBIR NOMBRE_EMPRESA Y LOGO
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT nombreEmpresaFumigadora, fotoLogoEmpresaFumigadora 
        FROM empresafumigadora 
        WHERE idEmpresaFumigadora = %s;
    """, (idEmpresaFumigadoraFk,))
    resultado = cur.fetchone()
    cur.close()

    if not resultado:
        # EN CASO DE NO HABER RESULTADOS
        return "Error: No se encontraron datos para esta empresa fumigadora", 404

    # ASIGNAR VALORES DESDE LOS RESULTADOS
    nombre_empresa = resultado[0]
    logo_empresa_fumigadora = resultado[1]

    # CONTEXTO
    context = {
        'idEmpleado': session.get('datos_cliente', {}).get('idEmpleado', 'Id_empleado_inexistente'),
        'nombresEmpleado': session.get('datos_cliente', {}).get('nombresEmpleado', 'nombre_inexistente'),
        'apellidosEmpleado': session.get('datos_cliente', {}).get('apellidosEmpleado', 'apellido_inexistente'),
        'numeroTelefonicoEmpleado': session.get('datos_cliente', {}).get('numeroTelefonicoEmpleado', 'telefono_inexistente'),
        'correoEmpresarialEmpleado': session.get('datos_cliente', {}).get('correoEmpresarialEmpleado', 'correo_empresarial_inexistente'),
        'correoPersonalEmpleado': session.get('datos_cliente', {}).get('correoPersonalEmpleado', 'correo_personal_inexistente'),
        'contrasenaEmpleado': session.get('datos_cliente', {}).get('contrasenaEmpleado', 'contraseña_inexistente'),
        'idEmpresaFumigadoraFk': idEmpresaFumigadoraFk,
        'estadoEmpleado': session.get('datos_cliente', {}).get('estadoEmpleado', 'Estado_empleado_inexistente'),
        'nombreEmpresaFumigadora': nombre_empresa,
        'logoEmpresaFumigadora': logo_empresa_fumigadora
    }
    return render_template('emp_empresa_fumigadora/Emp_empre_no_servicio.html', **context)