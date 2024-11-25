from . import Sede_cliente
from flask import render_template, redirect, url_for, flash, request, session
from flask import session
from app.config import configracion_base
from datetime import datetime

secret_key = configracion_base.SECRET_KEY

# PÁGINA DE PLANTILLA
@Sede_cliente.route('/Sede_cliente_plantilla')
def sede_cliente_plantilla():
    context = {
        'idSedeCliente' : session.get('datos_cliente', {}).get('idSedeCliente', 'Id_inexistente'),
        'nitSedeCliente' : session.get('datos_cliente', {}).get('nitSedeCliente', 'Nit_inexistente'),
        'nombreSedeCliente' : session.get('datos_cliente', {}).get('nombreSedeCliente', 'Nombre_inexistente'),
        'direccionSedeCliente' : session.get('datos_cliente', {}).get('direccionSedeCliente', 'Direccion_inexistente'),
        'gmailSedeCliente' : session.get('datos_cliente', {}).get('gmailSedeCliente', 'Gmail_inexistente'),
        'contrasenaSedeCliente' : session.get('datos_cliente', {}).get('contrasenaSedeCliente', 'Contraseña_inexistente'),
        'telefonoSedeCliente' : session.get('datos_cliente', {}).get('telefonoSedeCliente', 'Telefono_inexistente'),
        'departamentoSedeCliente' : session.get('datos_cliente', {}).get('departamentoSedeCliente', 'Departamento_inexistente'),
        'nombreEncargadoSedeCliente' : session.get('datos_cliente', {}).get('nombreEncargadoSedeCliente', 'Nombre_e_inexistente'),
        'telefonoEncargadoSedeCliente' : session.get('datos_cliente', {}).get('telefonoEncargadoSedeCliente', 'Telefono_e_inexistente'),
        'gmailEncargadoSedeCliente' : session.get('datos_cliente', {}).get('gmailEncargadoSedeCliente', 'Gmail_e_inexistente'),
        'fotoEncargadoSedeCliente' : session.get('datos_cliente', {}).get('fotoEncargadoSedeCliente', 'Foto_e_inexistente'),
        'idClienteFk' : session.get('datos_cliente', {}).get('idClienteFk', 'FK_Id_inexistente')
    }
    return render_template('sede_cliente/Sede_cliente_plantilla.html', **context)

# PÁGINA DE BIENVENIDA
@Sede_cliente.route('/Sede_cliente_ui')
def sede_cliente_ui():
    from app import mysql

    # Obtener el ID de la sede cliente desde la sesión
    idSedeCliente = session.get('datos_cliente', {}).get('idSedeCliente ', None)

    if not idSedeCliente:
        return "Error: Sede Cliente no asignada a este usuario", 400

    # Consulta para obtener el nombre comercial, logo del cliente y foto del encargado de la sede
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT cliente.nombreComercialCliente, cliente.logoCliente, sedescliente.fotoEncargadoSedeCliente
        FROM cliente
        JOIN sedescliente ON cliente.idCliente = sedescliente.idClienteFk
        WHERE sedescliente.idSedeCliente = %s;
    """, (idSedeCliente,))
    resultado = cur.fetchone()
    cur.close()

    if not resultado:
        return f"Error: No se encontraron datos para esta sede cliente con idSedeCliente = {idSedeCliente}", 404

    # Asignar valores desde el resultado de la consulta
    nombre_comercial_cliente = resultado[0]
    logo_cliente = resultado[1]
    foto_encargado = resultado[2]  # Nueva variable para la foto del encargado

    # Contexto para la plantilla con las claves de sesión y foto del encargado
    context = {
        'idSedeCliente': idSedeCliente,
        'nombreComercialCliente': nombre_comercial_cliente,
        'logoCliente': logo_cliente,
        'fotoEncargadoSedeCliente': foto_encargado,
        'nitSedeCliente': session.get('datos_cliente', {}).get('nitSedeCliente ', 'Nit_inexistente'),
        'nombreSedeCliente': session.get('datos_cliente', {}).get('nombreSedeCliente ', 'Nombre_inexistente'),
        'direccionSedeCliente': session.get('datos_cliente', {}).get('direccionSedeCliente ', 'Direccion_inexistente'),
        'gmailSedeCliente': session.get('datos_cliente', {}).get('gmailSedeCliente ', 'Gmail_inexistente'),
        'contrasenaSedeCliente': session.get('datos_cliente', {}).get('contrasenaSedeCliente ', 'Contraseña_inexistente'),
        'telefonoSedeCliente': session.get('datos_cliente', {}).get('telefonoSedeCliente ', 'Telefono_inexistente'),
        'departamentoSedeCliente': session.get('datos_cliente', {}).get('departamentoSedeCliente ', 'Departamento_inexistente'),
        'nombreEncargadoSedeCliente': session.get('datos_cliente', {}).get('nombreEncargadoSedeCliente ', 'Nombre_e_inexistente'),
        'telefonoEncargadoSedeCliente': session.get('datos_cliente', {}).get('telefonoEncargadoSedeCliente ', 'Telefono_e_inexistente'),
        'gmailEncargadoSedeCliente': session.get('datos_cliente', {}).get('gmailEncargadoSedeCliente ', 'Gmail_e_inexistente')
    }

    return render_template('sede_cliente/Sede_cliente_ui.html', **context)




# PÁGINA INFORMACIÓN GERENTE
@Sede_cliente.route('/Sede_cliente_gerente')
def Sede_cliente_gerente():
    from app import mysql

    # Obtener el ID de la sede cliente desde la sesión
    idSedeCliente = session.get('datos_cliente', {}).get('idSedeCliente ', None)

    if not idSedeCliente:
        return "Error: Sede Cliente no asignada a este usuario", 400

    # Consulta para obtener el nombre comercial, logo del cliente y foto del encargado de la sede
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT cliente.nombreComercialCliente, cliente.logoCliente, sedescliente.fotoEncargadoSedeCliente
        FROM cliente
        JOIN sedescliente ON cliente.idCliente = sedescliente.idClienteFk
        WHERE sedescliente.idSedeCliente = %s;
    """, (idSedeCliente,))
    resultado = cur.fetchone()
    cur.close()

    if not resultado:
        return f"Error: No se encontraron datos para esta sede cliente con idSedeCliente = {idSedeCliente}", 404

    # Asignar valores desde el resultado de la consulta
    nombre_comercial_cliente = resultado[0]
    logo_cliente = resultado[1]
    foto_encargado = resultado[2]  # Nueva variable para la foto del encargado

    # Contexto para la plantilla con las claves de sesión y foto del encargado
    context = {
        'idSedeCliente': idSedeCliente,
        'nombreComercialCliente': nombre_comercial_cliente,
        'logoCliente': logo_cliente,
        'fotoEncargadoSedeCliente': foto_encargado,
        'nitSedeCliente': session.get('datos_cliente', {}).get('nitSedeCliente ', 'Nit_inexistente'),
        'nombreSedeCliente': session.get('datos_cliente', {}).get('nombreSedeCliente ', 'Nombre_inexistente'),
        'direccionSedeCliente': session.get('datos_cliente', {}).get('direccionSedeCliente ', 'Direccion_inexistente'),
        'gmailSedeCliente': session.get('datos_cliente', {}).get('gmailSedeCliente ', 'Gmail_inexistente'),
        'contrasenaSedeCliente': session.get('datos_cliente', {}).get('contrasenaSedeCliente ', 'Contraseña_inexistente'),
        'telefonoSedeCliente': session.get('datos_cliente', {}).get('telefonoSedeCliente ', 'Telefono_inexistente'),
        'departamentoSedeCliente': session.get('datos_cliente', {}).get('departamentoSedeCliente ', 'Departamento_inexistente'),
        'nombreEncargadoSedeCliente': session.get('datos_cliente', {}).get('nombreEncargadoSedeCliente ', 'Nombre_e_inexistente'),
        'telefonoEncargadoSedeCliente': session.get('datos_cliente', {}).get('telefonoEncargadoSedeCliente ', 'Telefono_e_inexistente'),
        'gmailEncargadoSedeCliente': session.get('datos_cliente', {}).get('gmailEncargadoSedeCliente ', 'Gmail_e_inexistente')
    }
    return render_template('sede_cliente/Sede_cliente_gerente.html', **context)


# PÁGINA EDITAR CUENTA
@Sede_cliente.route('/Sede_cliente_edit', methods=['GET', 'POST'])
def Sede_cliente_edit():
    from app import mysql

    # Verificar la estructura y el contenido de 'datos_cliente' en la sesión
    print("Contenido de session['datos_cliente'] al entrar en Sede_cliente_edit:", session.get('datos_cliente'))

    # Obtener el ID de la sede cliente desde la sesión
    idSedeCliente = session['datos_cliente'].get('idSedeCliente ')
    print(f"ID de Sede Cliente desde la sesión: {idSedeCliente}")

    if idSedeCliente is None:
        flash("Error: ID de Sede Cliente no encontrado en la sesión. Revisa la configuración de sesión.", "error")
        return redirect(url_for('Sede_cliente.sede_cliente_ui'))

    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            departamento = request.form.get('departamento')
            telefono = request.form.get('telefono')
            direccion = request.form.get('direccion')
            nombre_encargado = request.form.get('nombre_encargado')
            nit = request.form.get('nit')
            nombre_establecimiento = request.form.get('nombre_establecimiento')
            correo = request.form.get('correo')
            telefono_encargado = request.form.get('telefono_encargado')
            correo_encargado = request.form.get('correo_encargado')

            print("Datos recibidos del formulario:", {
                'departamento': departamento,
                'telefono': telefono,
                'direccion': direccion,
                'nombre_encargado': nombre_encargado,
                'nit': nit,
                'nombre_establecimiento': nombre_establecimiento,
                'correo': correo,
                'telefono_encargado': telefono_encargado,
                'correo_encargado': correo_encargado
            })

            # Actualizar los datos en la base de datos
            cur = mysql.connection.cursor()
            cur.execute("""
                UPDATE sedescliente 
                SET departamentoSedeCliente = %s, telefonoSedeCliente = %s, 
                    direccionSedeCliente = %s, nombreEncargadoSedeCliente = %s, 
                    nitSedeCliente = %s, nombreSedeCliente = %s, gmailSedeCliente = %s, 
                    telefonoEncargadoSedeCliente = %s, gmailEncargadoSedeCliente = %s
                WHERE idSedeCliente = %s
            """, (
                departamento, telefono, direccion, nombre_encargado, nit, 
                nombre_establecimiento, correo, telefono_encargado, correo_encargado, 
                idSedeCliente
            ))
            mysql.connection.commit()
            cur.close()

            print("Actualización de datos en la base de datos completada para ID:", idSedeCliente)

            # Actualizar la sesión con los datos nuevos
            session['datos_cliente'].update({
                'departamentoSedeCliente ': departamento,
                'telefonoSedeCliente ': telefono,
                'direccionSedeCliente ': direccion,
                'nombreEncargadoSedeCliente ': nombre_encargado,
                'nitSedeCliente ': nit,
                'nombreSedeCliente ': nombre_establecimiento,
                'gmailSedeCliente ': correo,
                'telefonoEncargadoSedeCliente ': telefono_encargado,
                'gmailEncargadoSedeCliente ': correo_encargado
            })

            flash("Datos actualizados correctamente", "success")
            # Redirigir a la vista de actualización después de la edición exitosa
            return redirect(url_for('Sede_cliente.Sede_cliente_actualizar'))
        
        except Exception as e:
            print("Error durante la actualización de datos:", e)
            flash("Error al actualizar los datos: " + str(e), "error")
            return redirect(url_for('Sede_cliente.Sede_cliente_edit'))



    # Obtener el ID de la sede cliente desde la sesión
    idSedeCliente = session.get('datos_cliente', {}).get('idSedeCliente ', None)

    if not idSedeCliente:
        return "Error: Sede Cliente no asignada a este usuario", 400

    # Consulta para obtener el nombre comercial, logo del cliente y foto del encargado de la sede
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT cliente.nombreComercialCliente, cliente.logoCliente, sedescliente.fotoEncargadoSedeCliente
        FROM cliente
        JOIN sedescliente ON cliente.idCliente = sedescliente.idClienteFk
        WHERE sedescliente.idSedeCliente = %s;
    """, (idSedeCliente,))
    resultado = cur.fetchone()
    cur.close()

    if not resultado:
        return f"Error: No se encontraron datos para esta sede cliente con idSedeCliente = {idSedeCliente}", 404

    # Asignar valores desde el resultado de la consulta
    nombre_comercial_cliente = resultado[0]
    logo_cliente = resultado[1]
    foto_encargado = resultado[2]  # Nueva variable para la foto del encargado


    # Si se accede por GET, mostrar los datos actuales en la plantilla
    context = {
        'idSedeCliente': idSedeCliente,
        'logoCliente': logo_cliente,
        'fotoEncargadoSedeCliente': foto_encargado,
        'nombreComercialCliente': nombre_comercial_cliente,
        'nitSedeCliente': session['datos_cliente'].get('nitSedeCliente ', 'Nit_inexistente'),
        'nombreSedeCliente': session['datos_cliente'].get('nombreSedeCliente ', 'Nombre_inexistente'),
        'direccionSedeCliente': session['datos_cliente'].get('direccionSedeCliente ', 'Direccion_inexistente'),
        'gmailSedeCliente': session['datos_cliente'].get('gmailSedeCliente ', 'Gmail_inexistente'),
        'telefonoSedeCliente': session['datos_cliente'].get('telefonoSedeCliente ', 'Telefono_inexistente'),
        'departamentoSedeCliente': session['datos_cliente'].get('departamentoSedeCliente ', 'Departamento_inexistente'),
        'nombreEncargadoSedeCliente': session['datos_cliente'].get('nombreEncargadoSedeCliente ', 'Nombre_e_inexistente'),
        'telefonoEncargadoSedeCliente': session['datos_cliente'].get('telefonoEncargadoSedeCliente ', 'Telefono_e_inexistente'),
        'gmailEncargadoSedeCliente': session['datos_cliente'].get('gmailEncargadoSedeCliente ', 'Gmail_e_inexistente')
    }

    print("Contexto enviado a la plantilla de edición:", context)
    return render_template('sede_cliente/Sede_cliente_edit.html', **context)










@Sede_cliente.route('/Sede_cliente_actualizacion')
def Sede_cliente_actualizar():
    from app import mysql

    # Obtener el ID de la sede cliente desde la sesión
    idSedeCliente = session.get('datos_cliente', {}).get('idSedeCliente ', None)

    if not idSedeCliente:
        return "Error: Sede Cliente no asignada a este usuario", 400

    # Consulta para obtener el nombre comercial, logo del cliente y foto del encargado de la sede
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT cliente.nombreComercialCliente, cliente.logoCliente, sedescliente.fotoEncargadoSedeCliente
        FROM cliente
        JOIN sedescliente ON cliente.idCliente = sedescliente.idClienteFk
        WHERE sedescliente.idSedeCliente = %s;
    """, (idSedeCliente,))
    resultado = cur.fetchone()
    cur.close()

    if not resultado:
        return f"Error: No se encontraron datos para esta sede cliente con idSedeCliente = {idSedeCliente}", 404

    # Asignar valores desde el resultado de la consulta
    nombre_comercial_cliente = resultado[0]
    logo_cliente = resultado[1]
    foto_encargado = resultado[2]  # Nueva variable para la foto del encargado

    # Contexto para la plantilla con las claves de sesión y foto del encargado
    context = {
        'idSedeCliente': idSedeCliente,
        'nombreComercialCliente': nombre_comercial_cliente,
        'logoCliente': logo_cliente,
        'fotoEncargadoSedeCliente': foto_encargado,
        'nitSedeCliente': session.get('datos_cliente', {}).get('nitSedeCliente ', 'Nit_inexistente'),
        'nombreSedeCliente': session.get('datos_cliente', {}).get('nombreSedeCliente ', 'Nombre_inexistente'),
        'direccionSedeCliente': session.get('datos_cliente', {}).get('direccionSedeCliente ', 'Direccion_inexistente'),
        'gmailSedeCliente': session.get('datos_cliente', {}).get('gmailSedeCliente ', 'Gmail_inexistente'),
        'contrasenaSedeCliente': session.get('datos_cliente', {}).get('contrasenaSedeCliente ', 'Contraseña_inexistente'),
        'telefonoSedeCliente': session.get('datos_cliente', {}).get('telefonoSedeCliente ', 'Telefono_inexistente'),
        'departamentoSedeCliente': session.get('datos_cliente', {}).get('departamentoSedeCliente ', 'Departamento_inexistente'),
        'nombreEncargadoSedeCliente': session.get('datos_cliente', {}).get('nombreEncargadoSedeCliente ', 'Nombre_e_inexistente'),
        'telefonoEncargadoSedeCliente': session.get('datos_cliente', {}).get('telefonoEncargadoSedeCliente ', 'Telefono_e_inexistente'),
        'gmailEncargadoSedeCliente': session.get('datos_cliente', {}).get('gmailEncargadoSedeCliente ', 'Gmail_e_inexistente')
    }
    
    return render_template('sede_cliente/Sede_cliente_actualizacion.html', **context)






# PÁGINA BORRAR CUENTA
@Sede_cliente.route('/Sede_cliente_borrar', methods=['GET', 'POST'])
def Sede_cliente_borrar():
    from app import mysql

    # Acceder a 'idSedeCliente' eliminando el espacio adicional
    idSedeCliente = session.get('datos_cliente', {}).get('idSedeCliente ', None)  # Nota el espacio
    print(f"ID de Sede Cliente después de eliminar espacios: {idSedeCliente}")

    if not idSedeCliente:
        flash("Error: Sede Cliente no asignada a este usuario", 'error')
        return redirect(url_for('Sede_cliente.sede_cliente_ui'))

    if request.method == 'POST':
        # Cambiar el estado de la sede cliente a inactiva (1)
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE sedescliente 
            SET estadoSede = 1
            WHERE idSedeCliente = %s
        """, (idSedeCliente,))
        mysql.connection.commit()
        cur.close()

        # Limpiar la sesión y redirigir al login
        session.clear()
        flash("Sede cliente activada exitosamente", "success")
        return redirect(url_for('Login.login'))

    # Prueba de conexión con la tabla 'cliente' y 'sedescliente'
    try:
        cur = mysql.connection.cursor()
        cur.execute("""
            SELECT cliente.logoCliente, sedescliente.fotoEncargadoSedeCliente
            FROM cliente
            JOIN sedescliente ON cliente.idCliente = sedescliente.idClienteFk
            WHERE sedescliente.idSedeCliente = %s;
        """, (idSedeCliente,))
        resultado = cur.fetchone()
        cur.close()

        if not resultado:
            flash("No se encontraron datos de cliente asociados a esta sede.", "error")
            return redirect(url_for('Sede_cliente.sede_cliente_ui'))

        # Configurar el contexto con los datos recuperados o valores por defecto
        logo_cliente = resultado[0] if resultado else 'Logo_inexistente'
        foto_encargado = resultado[1] if resultado else 'Foto_encargado_inexistente'

        context = {
            'idSedeCliente': idSedeCliente,
            'nombreSedeCliente': session.get('datos_cliente', {}).get('nombreSedeCliente ', 'Nombre_inexistente'),
            'logoCliente': logo_cliente,
            'fotoEncargadoSedeCliente': foto_encargado,
        }

        return render_template('sede_cliente/Sede_cliente_borrar.html', **context)

    except Exception as e:
        print(f"Error en la consulta de base de datos: {e}")
        flash("Error al conectar con la base de datos. Verifica la relación entre las tablas.", "error")
        return redirect(url_for('Sede_cliente.sede_cliente_ui'))































# PÁGINA DETALLES DE SERVICIO
@Sede_cliente.route('/Sede_cliente_detall')
def Sede_cliente_detall():
    from app import mysql
    from flask import session, render_template, redirect, url_for

    # Obtener el ID de la sede cliente desde la sesión
    idSedeCliente = session.get('datos_cliente', {}).get('idSedeCliente ', None)

    if not idSedeCliente:
        return "Error: Sede Cliente no asignada a este usuario", 400

    # Consulta para obtener el nombre comercial, logo del cliente y foto del encargado de la sede
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT cliente.nombreComercialCliente, cliente.logoCliente, sedescliente.fotoEncargadoSedeCliente
        FROM cliente
        JOIN sedescliente ON cliente.idCliente = sedescliente.idClienteFk
        WHERE sedescliente.idSedeCliente = %s;
    """, (idSedeCliente,))
    resultado = cur.fetchone()
    cur.close()

    if not resultado:
        return f"Error: No se encontraron datos para esta sede cliente con idSedeCliente = {idSedeCliente}", 404

    # Asignar valores desde el resultado de la consulta
    nombre_comercial_cliente = resultado[0]
    logo_cliente = resultado[1]
    foto_encargado = resultado[2]  # Nueva variable para la foto del encargado

    # Nueva consulta para obtener EMPRESA, CLASE, CARACTERISTICA y DETALLE
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT
            empresafumigadora.nombreEmpresaFumigadora AS empresa,
            clases.nombreClases AS clase,
            caracteristicas.nombreCaracteristicas AS caracteristica,
            detallesservicio.valorDetalle AS detalle
        FROM
            detallesservicio
        JOIN
            caracteristicas ON detallesservicio.idCaracteristicaFk = caracteristicas.idCaracteristicas
        JOIN
            clases ON caracteristicas.idClasesFk = clases.idClases
        JOIN
            servicio ON detallesservicio.idServicioFk = servicio.idServicio
        JOIN
            sedescliente ON servicio.idSedeClienteFk = sedescliente.idSedeCliente
        JOIN
            empresafumigadora ON sedescliente.idClienteFk = empresafumigadora.idEmpresaFumigadora
        WHERE
            sedescliente.idSedeCliente = %s;
    """, (idSedeCliente,))

    d_servicios = cur.fetchall()
    cur.close()

    # Comprobar si se obtuvieron servicios
    if not d_servicios:
        return redirect(url_for('Sede_cliente.Sede_cliente_no_det_servicio'))

    d_servicios_contexto = [
        {
            'empresa': detalle[0],
            'clase': detalle[1],
            'caracteristica': detalle[2],
            'detalles': detalle[3],
        }
        for detalle in d_servicios
    ]

    # Contexto para la plantilla con las claves de sesión y foto del encargado
    context = {
        'idSedeCliente': idSedeCliente,
        'nombreComercialCliente': nombre_comercial_cliente,
        'logoCliente': logo_cliente,
        'fotoEncargadoSedeCliente': foto_encargado,
        'nitSedeCliente': session.get('datos_cliente', {}).get('nitSedeCliente ', 'Nit_inexistente'),
        'nombreSedeCliente': session.get('datos_cliente', {}).get('nombreSedeCliente ', 'Nombre_inexistente'),
        'direccionSedeCliente': session.get('datos_cliente', {}).get('direccionSedeCliente ', 'Direccion_inexistente'),
        'gmailSedeCliente': session.get('datos_cliente', {}).get('gmailSedeCliente ', 'Gmail_inexistente'),
        'contrasenaSedeCliente': session.get('datos_cliente', {}).get('contrasenaSedeCliente ', 'Contraseña_inexistente'),
        'telefonoSedeCliente': session.get('datos_cliente', {}).get('telefonoSedeCliente ', 'Telefono_inexistente'),
        'departamentoSedeCliente': session.get('datos_cliente', {}).get('departamentoSedeCliente ', 'Departamento_inexistente'),
        'nombreEncargadoSedeCliente': session.get('datos_cliente', {}).get('nombreEncargadoSedeCliente ', 'Nombre_e_inexistente'),
        'telefonoEncargadoSedeCliente': session.get('datos_cliente', {}).get('telefonoEncargadoSedeCliente ', 'Telefono_e_inexistente'),
        'gmailEncargadoSedeCliente': session.get('datos_cliente', {}).get('gmailEncargadoSedeCliente ', 'Gmail_e_inexistente'),
        'd_servicios': d_servicios_contexto
    }

    return render_template('sede_cliente/Sede_cliente_detall.html', **context)
































# PÁGINA SERVICIOS
@Sede_cliente.route('/Sede_cliente_servi')
def Sede_cliente_servi():
    from app import mysql
    from flask import session, render_template, redirect, url_for
    # Obtener el ID de la sede cliente desde la sesión
    idSedeCliente = session.get('datos_cliente', {}).get('idSedeCliente ', None)

    if not idSedeCliente:
        return "Error: Sede Cliente no asignada a este usuario", 400

    # Consulta para obtener el nombre comercial, logo del cliente y foto del encargado de la sede
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT cliente.nombreComercialCliente, cliente.logoCliente, sedescliente.fotoEncargadoSedeCliente
        FROM cliente
        JOIN sedescliente ON cliente.idCliente = sedescliente.idClienteFk
        WHERE sedescliente.idSedeCliente = %s;
    """, (idSedeCliente,))
    resultado = cur.fetchone()
    cur.close()

    if not resultado:
        return f"Error: No se encontraron datos para esta sede cliente con idSedeCliente = {idSedeCliente}", 404

    # Asignar valores desde el resultado de la consulta
    nombre_comercial_cliente = resultado[0]
    logo_cliente = resultado[1]
    foto_encargado = resultado[2]  # Nueva variable para la foto del encargado


    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT 
            ef.nombreEmpresaFumigadora AS empresa,
            CONCAT(e.nombresEmpleado, ' ', e.apellidosEmpleado) AS empleados,
            s.fechaInicioServicio AS inicio,
            s.fechaFinalServicio AS fin,
            s.estadoServicio AS estado
        FROM 
            servicio s
        JOIN 
            empleado e ON s.idEmpleadoFk = e.idEmpleado
        JOIN 
            empresafumigadora ef ON e.idEmpresaFumigadoraFk = ef.idEmpresaFumigadora
        WHERE 
            s.idSedeClienteFk = %s and s.estadoServicio = "en espera";
    """, (idSedeCliente,))
    
    servicios = cur.fetchall()
    cur.close()

    # Comprobar si se obtuvieron servicios
    if not servicios:
        return redirect(url_for('Sede_cliente.Sede_cliente_no_servicio'))


    servicios_contexto = [
        {
            'empresa': servicio[0],
            'empleados': servicio[1],
            'inicio': servicio[2],
            'fin': servicio[3],
            'estado': servicio[4],
        }
        for servicio in servicios
    ]

    context = {
        'idSedeCliente': idSedeCliente,
        'nombreComercialCliente': nombre_comercial_cliente,
        'logoCliente': logo_cliente,
        'fotoEncargadoSedeCliente': foto_encargado,
        'idSedeCliente' : session.get('datos_cliente', {}).get('idSedeCliente', 'Id_inexistente'),
        'nitSedeCliente' : session.get('datos_cliente', {}).get('nitSedeCliente', 'Nit_inexistente'),
        'nombreSedeCliente' : session.get('datos_cliente', {}).get('nombreSedeCliente', 'Nombre_inexistente'),
        'direccionSedeCliente' : session.get('datos_cliente', {}).get('direccionSedeCliente', 'Direccion_inexistente'),
        'gmailSedeCliente' : session.get('datos_cliente', {}).get('gmailSedeCliente', 'Gmail_inexistente'),
        'contrasenaSedeCliente' : session.get('datos_cliente', {}).get('contrasenaSedeCliente', 'Contraseña_inexistente'),
        'telefonoSedeCliente' : session.get('datos_cliente', {}).get('telefonoSedeCliente', 'Telefono_inexistente'),
        'departamentoSedeCliente' : session.get('datos_cliente', {}).get('departamentoSedeCliente', 'Departamento_inexistente'),
        'nombreEncargadoSedeCliente' : session.get('datos_cliente', {}).get('nombreEncargadoSedeCliente', 'Nombre_e_inexistente'),
        'telefonoEncargadoSedeCliente' : session.get('datos_cliente', {}).get('telefonoEncargadoSedeCliente', 'Telefono_e_inexistente'),
        'gmailEncargadoSedeCliente' : session.get('datos_cliente', {}).get('gmailEncargadoSedeCliente', 'Gmail_e_inexistente'),
        'fotoEncargadoSedeCliente' : session.get('datos_cliente', {}).get('fotoEncargadoSedeCliente', 'Foto_e_inexistente'),
        'idClienteFk' : session.get('datos_cliente', {}).get('idClienteFk', 'FK_Id_inexistente'),
        'servicios_contexto' : servicios_contexto
    }
    return render_template('sede_cliente/Sede_cliente_servi.html', **context)































# PÁGINA SOLICITUD SERVICIOS
@Sede_cliente.route('/Sede_cliente_solicitud_servi')
def Sede_cliente_solicitud_servi():
    from flask import session, render_template, redirect, url_for
    from app import mysql

    # Obtener el ID de la sede cliente desde la sesión
    idSedeCliente = session.get('datos_cliente', {}).get('idSedeCliente ', None)

    if not idSedeCliente:
        return "Error: Sede Cliente no asignada a este usuario", 400

    # Consulta para obtener el nombre comercial, logo del cliente y foto del encargado de la sede
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT cliente.nombreComercialCliente, cliente.logoCliente, sedescliente.fotoEncargadoSedeCliente
        FROM cliente
        JOIN sedescliente ON cliente.idCliente = sedescliente.idClienteFk
        WHERE sedescliente.idSedeCliente = %s;
    """, (idSedeCliente,))
    resultado = cur.fetchone()
    cur.close()

    if not resultado:
        return f"Error: No se encontraron datos para esta sede cliente con idSedeCliente = {idSedeCliente}", 404

    # Asignar valores desde el resultado de la consulta
    nombre_comercial_cliente = resultado[0]
    logo_cliente = resultado[1]
    foto_encargado = resultado[2]  # Nueva variable para la foto del encargado

    context = {
        'nombre_comercial_cliente' : nombre_comercial_cliente,
        'idSedeCliente': idSedeCliente,
        'logoCliente': logo_cliente,
        'fotoEncargadoSedeCliente': foto_encargado, 
        'idSedeCliente' : session.get('datos_cliente', {}).get('idSedeCliente', 'Id_inexistente'),
        'nitSedeCliente' : session.get('datos_cliente', {}).get('nitSedeCliente', 'Nit_inexistente'),
        'nombreSedeCliente' : session.get('datos_cliente', {}).get('nombreSedeCliente', 'Nombre_inexistente'),
        'direccionSedeCliente' : session.get('datos_cliente', {}).get('direccionSedeCliente', 'Direccion_inexistente'),
        'gmailSedeCliente' : session.get('datos_cliente', {}).get('gmailSedeCliente', 'Gmail_inexistente'),
        'contrasenaSedeCliente' : session.get('datos_cliente', {}).get('contrasenaSedeCliente', 'Contraseña_inexistente'),
        'telefonoSedeCliente' : session.get('datos_cliente', {}).get('telefonoSedeCliente', 'Telefono_inexistente'),
        'departamentoSedeCliente' : session.get('datos_cliente', {}).get('departamentoSedeCliente', 'Departamento_inexistente'),
        'nombreEncargadoSedeCliente' : session.get('datos_cliente', {}).get('nombreEncargadoSedeCliente', 'Nombre_e_inexistente'),
        'telefonoEncargadoSedeCliente' : session.get('datos_cliente', {}).get('telefonoEncargadoSedeCliente', 'Telefono_e_inexistente'),
        'gmailEncargadoSedeCliente' : session.get('datos_cliente', {}).get('gmailEncargadoSedeCliente', 'Gmail_e_inexistente'),
        'fotoEncargadoSedeCliente' : session.get('datos_cliente', {}).get('fotoEncargadoSedeCliente', 'Foto_e_inexistente'),
        'idClienteFk' : session.get('datos_cliente', {}).get('idClienteFk', 'FK_Id_inexistente'),
    }

    cur = mysql.connection.cursor()
    cur.execute("SELECT nombreEmpresaFumigadora FROM empresafumigadora where estadoEmpresa = 1")
    empresas = cur.fetchall()

    session['empresas'] = []

    for empresas_sede in empresas:
        session['empresas'].append({
            'nombre_empresa' : empresas_sede[0]
        }) 
    return render_template('Sede_cliente/Sede_cliente_solicitud_servi.html', **context)

































@Sede_cliente.route("/Solicitar_servicio", methods=['POST'])
def Solicitar_servicio():
    from app import mysql
    from flask import session, render_template, request, redirect, url_for

    idSedeCliente = session.get('datos_cliente', {}).get('idSedeCliente ', None)

    if not idSedeCliente:
        return "Error: Sede Cliente no asignada a este usuario", 400

    # Consulta para obtener el nombre comercial, logo del cliente y foto del encargado de la sede
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT cliente.nombreComercialCliente, cliente.logoCliente, sedescliente.fotoEncargadoSedeCliente
        FROM cliente
        JOIN sedescliente ON cliente.idCliente = sedescliente.idClienteFk
        WHERE sedescliente.idSedeCliente = %s;
    """, (idSedeCliente,))
    resultado = cur.fetchone()
    cur.close()


    # Asignar valores desde el resultado de la consulta
    nombre_comercial_cliente = resultado[0]
    logo_cliente = resultado[1]
    foto_encargado = resultado[2] 




    empresa_fumigadora = request.form.get('empre')
    nivel_infestacion = request.form.get('nivelInfestacion')
    descripcion = request.form.get('descripcion')
    if not empresa_fumigadora or not nivel_infestacion or not descripcion:
        return "Error: Todos los campos son requeridos", 400
    

    cur = mysql.connection.cursor()
    cur.execute("""
            INSERT INTO servicio (descripcionServicio, nivelInfestacionDetallesServicio, estadoServicio, idSedeClienteFk)
            VALUES (%s, %s, %s, %s)
        """, (descripcion,  nivel_infestacion,'En Espera', idSedeCliente))
    mysql.connection.commit()
    resultado_request = cur.fetchone()
    cur.close()
    
    



    context = {
        'idSedeCliente': idSedeCliente,
        'nombreComercialCliente': nombre_comercial_cliente,
        'logoCliente': logo_cliente,
        'fotoEncargadoSedeCliente': foto_encargado,
        'nitSedeCliente': session.get('datos_cliente', {}).get('nitSedeCliente ', 'Nit_inexistente'),
        'nombreSedeCliente': session.get('datos_cliente', {}).get('nombreSedeCliente ', 'Nombre_inexistente'),
        'direccionSedeCliente': session.get('datos_cliente', {}).get('direccionSedeCliente ', 'Direccion_inexistente'),
        'gmailSedeCliente': session.get('datos_cliente', {}).get('gmailSedeCliente ', 'Gmail_inexistente'),
        'contrasenaSedeCliente': session.get('datos_cliente', {}).get('contrasenaSedeCliente ', 'Contraseña_inexistente'),
        'telefonoSedeCliente': session.get('datos_cliente', {}).get('telefonoSedeCliente ', 'Telefono_inexistente'),
        'departamentoSedeCliente': session.get('datos_cliente', {}).get('departamentoSedeCliente ', 'Departamento_inexistente'),
        'nombreEncargadoSedeCliente': session.get('datos_cliente', {}).get('nombreEncargadoSedeCliente ', 'Nombre_e_inexistente'),
        'telefonoEncargadoSedeCliente': session.get('datos_cliente', {}).get('telefonoEncargadoSedeCliente ', 'Telefono_e_inexistente'),
        'gmailEncargadoSedeCliente': session.get('datos_cliente', {}).get('gmailEncargadoSedeCliente ', 'Gmail_e_inexistente')
    }

    

    return render_template('sede_cliente/Sede_cliente_servi_solicitado.html', **context)








# PÁGINA SERVICIO SOLICITADO
@Sede_cliente.route("/Sede_cliente_servi_solicitado")
def Sede_cliente_servi_solicitado():
    from app import mysql
        # Obtener el ID de la sede cliente desde la sesión
    idSedeCliente = session.get('datos_cliente', {}).get('idSedeCliente ', None)

    if not idSedeCliente:
        return "Error: Sede Cliente no asignada a este usuario", 400

    # Consulta para obtener el nombre comercial, logo del cliente y foto del encargado de la sede
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT cliente.nombreComercialCliente, cliente.logoCliente, sedescliente.fotoEncargadoSedeCliente
        FROM cliente
        JOIN sedescliente ON cliente.idCliente = sedescliente.idClienteFk
        WHERE sedescliente.idSedeCliente = %s;
    """, (idSedeCliente,))
    resultado = cur.fetchone()
    cur.close()

    if not resultado:
        return f"Error: No se encontraron datos para esta sede cliente con idSedeCliente = {idSedeCliente}", 404

    # Asignar valores desde el resultado de la consulta
    nombre_comercial_cliente = resultado[0]
    logo_cliente = resultado[1]
    foto_encargado = resultado[2]  # Nueva variable para la foto del encargado

    # Contexto para la plantilla con las claves de sesión y foto del encargado
    context = {
        'idSedeCliente': idSedeCliente,
        'nombreComercialCliente': nombre_comercial_cliente,
        'logoCliente': logo_cliente,
        'fotoEncargadoSedeCliente': foto_encargado,
        'nitSedeCliente': session.get('datos_cliente', {}).get('nitSedeCliente ', 'Nit_inexistente'),
        'nombreSedeCliente': session.get('datos_cliente', {}).get('nombreSedeCliente ', 'Nombre_inexistente'),
        'direccionSedeCliente': session.get('datos_cliente', {}).get('direccionSedeCliente ', 'Direccion_inexistente'),
        'gmailSedeCliente': session.get('datos_cliente', {}).get('gmailSedeCliente ', 'Gmail_inexistente'),
        'contrasenaSedeCliente': session.get('datos_cliente', {}).get('contrasenaSedeCliente ', 'Contraseña_inexistente'),
        'telefonoSedeCliente': session.get('datos_cliente', {}).get('telefonoSedeCliente ', 'Telefono_inexistente'),
        'departamentoSedeCliente': session.get('datos_cliente', {}).get('departamentoSedeCliente ', 'Departamento_inexistente'),
        'nombreEncargadoSedeCliente': session.get('datos_cliente', {}).get('nombreEncargadoSedeCliente ', 'Nombre_e_inexistente'),
        'telefonoEncargadoSedeCliente': session.get('datos_cliente', {}).get('telefonoEncargadoSedeCliente ', 'Telefono_e_inexistente'),
        'gmailEncargadoSedeCliente': session.get('datos_cliente', {}).get('gmailEncargadoSedeCliente ', 'Gmail_e_inexistente')
    }

    return render_template('sede_cliente/Sede_cliente_servi_solicitado.html', **context)















# PÁGINA DE NO DETALLES DE SERVICIO
@Sede_cliente.route('/Sede_cliente_no_det_servicio')
def Sede_cliente_no_det_servicio():
    from app import mysql
        # Obtener el ID de la sede cliente desde la sesión
    idSedeCliente = session.get('datos_cliente', {}).get('idSedeCliente ', None)

    if not idSedeCliente:
        return "Error: Sede Cliente no asignada a este usuario", 400

    # Consulta para obtener el nombre comercial, logo del cliente y foto del encargado de la sede
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT cliente.nombreComercialCliente, cliente.logoCliente, sedescliente.fotoEncargadoSedeCliente
        FROM cliente
        JOIN sedescliente ON cliente.idCliente = sedescliente.idClienteFk
        WHERE sedescliente.idSedeCliente = %s;
    """, (idSedeCliente,))
    resultado = cur.fetchone()
    cur.close()

    if not resultado:
        return f"Error: No se encontraron datos para esta sede cliente con idSedeCliente = {idSedeCliente}", 404

    # Asignar valores desde el resultado de la consulta
    nombre_comercial_cliente = resultado[0]
    logo_cliente = resultado[1]
    foto_encargado = resultado[2]  # Nueva variable para la foto del encargado

    # Contexto para la plantilla con las claves de sesión y foto del encargado
    context = {
        'idSedeCliente': idSedeCliente,
        'nombreComercialCliente': nombre_comercial_cliente,
        'logoCliente': logo_cliente,
        'fotoEncargadoSedeCliente': foto_encargado,
        'nitSedeCliente': session.get('datos_cliente', {}).get('nitSedeCliente ', 'Nit_inexistente'),
        'nombreSedeCliente': session.get('datos_cliente', {}).get('nombreSedeCliente ', 'Nombre_inexistente'),
        'direccionSedeCliente': session.get('datos_cliente', {}).get('direccionSedeCliente ', 'Direccion_inexistente'),
        'gmailSedeCliente': session.get('datos_cliente', {}).get('gmailSedeCliente ', 'Gmail_inexistente'),
        'contrasenaSedeCliente': session.get('datos_cliente', {}).get('contrasenaSedeCliente ', 'Contraseña_inexistente'),
        'telefonoSedeCliente': session.get('datos_cliente', {}).get('telefonoSedeCliente ', 'Telefono_inexistente'),
        'departamentoSedeCliente': session.get('datos_cliente', {}).get('departamentoSedeCliente ', 'Departamento_inexistente'),
        'nombreEncargadoSedeCliente': session.get('datos_cliente', {}).get('nombreEncargadoSedeCliente ', 'Nombre_e_inexistente'),
        'telefonoEncargadoSedeCliente': session.get('datos_cliente', {}).get('telefonoEncargadoSedeCliente ', 'Telefono_e_inexistente'),
        'gmailEncargadoSedeCliente': session.get('datos_cliente', {}).get('gmailEncargadoSedeCliente ', 'Gmail_e_inexistente')
    }
    return render_template('sede_cliente/Sede_cliente_no_det_servicio.html', **context)

















# PÁGINA DE NO SERVICIO
@Sede_cliente.route('/Sede_cliente_no_servicio')
def Sede_cliente_no_servicio():
    from app import mysql
        # Obtener el ID de la sede cliente desde la sesión
    idSedeCliente = session.get('datos_cliente', {}).get('idSedeCliente ', None)

    if not idSedeCliente:
        return "Error: Sede Cliente no asignada a este usuario", 400

    # Consulta para obtener el nombre comercial, logo del cliente y foto del encargado de la sede
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT cliente.nombreComercialCliente, cliente.logoCliente, sedescliente.fotoEncargadoSedeCliente
        FROM cliente
        JOIN sedescliente ON cliente.idCliente = sedescliente.idClienteFk
        WHERE sedescliente.idSedeCliente = %s;
    """, (idSedeCliente,))
    resultado = cur.fetchone()
    cur.close()

    if not resultado:
        return f"Error: No se encontraron datos para esta sede cliente con idSedeCliente = {idSedeCliente}", 404

    # Asignar valores desde el resultado de la consulta
    nombre_comercial_cliente = resultado[0]
    logo_cliente = resultado[1]
    foto_encargado = resultado[2]  # Nueva variable para la foto del encargado

    # Contexto para la plantilla con las claves de sesión y foto del encargado
    context = {
        'idSedeCliente': idSedeCliente,
        'nombreComercialCliente': nombre_comercial_cliente,
        'logoCliente': logo_cliente,
        'fotoEncargadoSedeCliente': foto_encargado,
        'nitSedeCliente': session.get('datos_cliente', {}).get('nitSedeCliente ', 'Nit_inexistente'),
        'nombreSedeCliente': session.get('datos_cliente', {}).get('nombreSedeCliente ', 'Nombre_inexistente'),
        'direccionSedeCliente': session.get('datos_cliente', {}).get('direccionSedeCliente ', 'Direccion_inexistente'),
        'gmailSedeCliente': session.get('datos_cliente', {}).get('gmailSedeCliente ', 'Gmail_inexistente'),
        'contrasenaSedeCliente': session.get('datos_cliente', {}).get('contrasenaSedeCliente ', 'Contraseña_inexistente'),
        'telefonoSedeCliente': session.get('datos_cliente', {}).get('telefonoSedeCliente ', 'Telefono_inexistente'),
        'departamentoSedeCliente': session.get('datos_cliente', {}).get('departamentoSedeCliente ', 'Departamento_inexistente'),
        'nombreEncargadoSedeCliente': session.get('datos_cliente', {}).get('nombreEncargadoSedeCliente ', 'Nombre_e_inexistente'),
        'telefonoEncargadoSedeCliente': session.get('datos_cliente', {}).get('telefonoEncargadoSedeCliente ', 'Telefono_e_inexistente'),
        'gmailEncargadoSedeCliente': session.get('datos_cliente', {}).get('gmailEncargadoSedeCliente ', 'Gmail_e_inexistente')
    }
    return render_template('sede_cliente/Sede_cliente_no_servicio.html', **context)



























#SERVICIOS

# PARTE REPORTE
@Sede_cliente.route("/reporte")
def reporte():
    from app import mysql

    idSedeCliente = session.get('datos_cliente', {}).get('idSedeCliente ', None)

    if not idSedeCliente:
        return "Error: Sede Cliente no asignada a este usuario", 400

    # Consulta para obtener el nombre comercial, logo del cliente y foto del encargado de la sede
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT cliente.nombreComercialCliente, cliente.logoCliente, sedescliente.fotoEncargadoSedeCliente
        FROM cliente
        JOIN sedescliente ON cliente.idCliente = sedescliente.idClienteFk
        WHERE sedescliente.idSedeCliente = %s;
    """, (idSedeCliente,))
    resultado = cur.fetchone()
    cur.close()

    if not resultado:
        return f"Error: No se encontraron datos para esta sede cliente con idSedeCliente = {idSedeCliente}", 404

    # Asignar valores desde el resultado de la consulta
    nombre_comercial_cliente = resultado[0]
    logo_cliente = resultado[1]
    foto_encargado = resultado[2]  # Nueva variable para la foto del encargado

    # Contexto para la plantilla con las claves de sesión y foto del encargado
    context = {
        'idSedeCliente': idSedeCliente,
        'nombreComercialCliente': nombre_comercial_cliente,
        'logoCliente': logo_cliente,
        'fotoEncargadoSedeCliente': foto_encargado,
        'nitSedeCliente': session.get('datos_cliente', {}).get('nitSedeCliente ', 'Nit_inexistente'),
        'nombreSedeCliente': session.get('datos_cliente', {}).get('nombreSedeCliente ', 'Nombre_inexistente'),
        'direccionSedeCliente': session.get('datos_cliente', {}).get('direccionSedeCliente ', 'Direccion_inexistente'),
        'gmailSedeCliente': session.get('datos_cliente', {}).get('gmailSedeCliente ', 'Gmail_inexistente'),
        'contrasenaSedeCliente': session.get('datos_cliente', {}).get('contrasenaSedeCliente ', 'Contraseña_inexistente'),
        'telefonoSedeCliente': session.get('datos_cliente', {}).get('telefonoSedeCliente ', 'Telefono_inexistente'),
        'departamentoSedeCliente': session.get('datos_cliente', {}).get('departamentoSedeCliente ', 'Departamento_inexistente'),
        'nombreEncargadoSedeCliente': session.get('datos_cliente', {}).get('nombreEncargadoSedeCliente ', 'Nombre_e_inexistente'),
        'telefonoEncargadoSedeCliente': session.get('datos_cliente', {}).get('telefonoEncargadoSedeCliente ', 'Telefono_e_inexistente'),
        'gmailEncargadoSedeCliente': session.get('datos_cliente', {}).get('gmailEncargadoSedeCliente ', 'Gmail_e_inexistente')
    }
    return render_template('sede_cliente/reporte.html', **context)









#certificados
@Sede_cliente.route('/certificados')
def certificados():
    from app import mysql

    # Obtener el ID de la sede cliente desde la sesión
    idSedeCliente = session.get('datos_cliente', {}).get('idSedeCliente ', None)

    if not idSedeCliente:
        return "Error: Sede Cliente no asignada a este usuario", 400

    # Consulta para obtener el nombre comercial, logo del cliente y foto del encargado de la sede
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT cliente.nombreComercialCliente, cliente.logoCliente, sedescliente.fotoEncargadoSedeCliente
        FROM cliente
        JOIN sedescliente ON cliente.idCliente = sedescliente.idClienteFk
        WHERE sedescliente.idSedeCliente = %s;
    """, (idSedeCliente,))
    resultado = cur.fetchone()
    cur.close()

    if not resultado:
        return f"Error: No se encontraron datos para esta sede cliente con idSedeCliente = {idSedeCliente}", 404

    # Asignar valores desde el resultado de la consulta
    nombre_comercial_cliente = resultado[0]
    logo_cliente = resultado[1]
    foto_encargado = resultado[2]  # Nueva variable para la foto del encargado

    # Contexto para la plantilla con las claves de sesión y foto del encargado
    context = {
        'idSedeCliente': idSedeCliente,
        'nombreComercialCliente': nombre_comercial_cliente,
        'logoCliente': logo_cliente,
        'fotoEncargadoSedeCliente': foto_encargado,
        'nitSedeCliente': session.get('datos_cliente', {}).get('nitSedeCliente ', 'Nit_inexistente'),
        'nombreSedeCliente': session.get('datos_cliente', {}).get('nombreSedeCliente ', 'Nombre_inexistente'),
        'direccionSedeCliente': session.get('datos_cliente', {}).get('direccionSedeCliente ', 'Direccion_inexistente'),
        'gmailSedeCliente': session.get('datos_cliente', {}).get('gmailSedeCliente ', 'Gmail_inexistente'),
        'contrasenaSedeCliente': session.get('datos_cliente', {}).get('contrasenaSedeCliente ', 'Contraseña_inexistente'),
        'telefonoSedeCliente': session.get('datos_cliente', {}).get('telefonoSedeCliente ', 'Telefono_inexistente'),
        'departamentoSedeCliente': session.get('datos_cliente', {}).get('departamentoSedeCliente ', 'Departamento_inexistente'),
        'nombreEncargadoSedeCliente': session.get('datos_cliente', {}).get('nombreEncargadoSedeCliente ', 'Nombre_e_inexistente'),
        'telefonoEncargadoSedeCliente': session.get('datos_cliente', {}).get('telefonoEncargadoSedeCliente ', 'Telefono_e_inexistente'),
        'gmailEncargadoSedeCliente': session.get('datos_cliente', {}).get('gmailEncargadoSedeCliente ', 'Gmail_e_inexistente')
    }
   
    return render_template('Sede_cliente/certificado.html', **context); 

















#DETALLES DE SERVICIOS

# PARTE REPORTE
@Sede_cliente.route("/reporte2")
def reporte2():
    from app import mysql

    # Obtener el ID de la sede cliente desde la sesión
    idSedeCliente = session.get('datos_cliente', {}).get('idSedeCliente ', None)

    if not idSedeCliente:
        return "Error: Sede Cliente no asignada a este usuario", 400

    # Consulta para obtener el nombre comercial, logo del cliente y foto del encargado de la sede
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT cliente.nombreComercialCliente, cliente.logoCliente, sedescliente.fotoEncargadoSedeCliente
        FROM cliente
        JOIN sedescliente ON cliente.idCliente = sedescliente.idClienteFk
        WHERE sedescliente.idSedeCliente = %s;
    """, (idSedeCliente,))
    resultado = cur.fetchone()
    cur.close()

    if not resultado:
        return f"Error: No se encontraron datos para esta sede cliente con idSedeCliente = {idSedeCliente}", 404

    # Asignar valores desde el resultado de la consulta
    nombre_comercial_cliente = resultado[0]
    logo_cliente = resultado[1]
    foto_encargado = resultado[2]  # Nueva variable para la foto del encargado

    # Contexto para la plantilla con las claves de sesión y foto del encargado
    context = {
        'idSedeCliente': idSedeCliente,
        'nombreComercialCliente': nombre_comercial_cliente,
        'logoCliente': logo_cliente,
        'fotoEncargadoSedeCliente': foto_encargado,
        'nitSedeCliente': session.get('datos_cliente', {}).get('nitSedeCliente ', 'Nit_inexistente'),
        'nombreSedeCliente': session.get('datos_cliente', {}).get('nombreSedeCliente ', 'Nombre_inexistente'),
        'direccionSedeCliente': session.get('datos_cliente', {}).get('direccionSedeCliente ', 'Direccion_inexistente'),
        'gmailSedeCliente': session.get('datos_cliente', {}).get('gmailSedeCliente ', 'Gmail_inexistente'),
        'contrasenaSedeCliente': session.get('datos_cliente', {}).get('contrasenaSedeCliente ', 'Contraseña_inexistente'),
        'telefonoSedeCliente': session.get('datos_cliente', {}).get('telefonoSedeCliente ', 'Telefono_inexistente'),
        'departamentoSedeCliente': session.get('datos_cliente', {}).get('departamentoSedeCliente ', 'Departamento_inexistente'),
        'nombreEncargadoSedeCliente': session.get('datos_cliente', {}).get('nombreEncargadoSedeCliente ', 'Nombre_e_inexistente'),
        'telefonoEncargadoSedeCliente': session.get('datos_cliente', {}).get('telefonoEncargadoSedeCliente ', 'Telefono_e_inexistente'),
        'gmailEncargadoSedeCliente': session.get('datos_cliente', {}).get('gmailEncargadoSedeCliente ', 'Gmail_e_inexistente')
    }
    return render_template("sede_cliente/Reporte.html", ** context)








# certificados
@Sede_cliente.route('/certificado2')
def certificado2():
    from app import mysql

    # Obtener el ID de la sede cliente desde la sesión
    idSedeCliente = session.get('datos_cliente', {}).get('idSedeCliente ', None)

    if not idSedeCliente:
        return "Error: Sede Cliente no asignada a este usuario", 400

    # Consulta para obtener el nombre comercial, logo del cliente y foto del encargado de la sede
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT cliente.nombreComercialCliente, cliente.logoCliente, sedescliente.fotoEncargadoSedeCliente
        FROM cliente
        JOIN sedescliente ON cliente.idCliente = sedescliente.idClienteFk
        WHERE sedescliente.idSedeCliente = %s;
    """, (idSedeCliente,))
    resultado = cur.fetchone()
    cur.close()

    if not resultado:
        return f"Error: No se encontraron datos para esta sede cliente con idSedeCliente = {idSedeCliente}", 404

    # Asignar valores desde el resultado de la consulta
    nombre_comercial_cliente = resultado[0]
    logo_cliente = resultado[1]
    foto_encargado = resultado[2]  # Nueva variable para la foto del encargado

    # Contexto para la plantilla con las claves de sesión y foto del encargado
    context = {
        'idSedeCliente': idSedeCliente,
        'nombreComercialCliente': nombre_comercial_cliente,
        'logoCliente': logo_cliente,
        'fotoEncargadoSedeCliente': foto_encargado,
        'nitSedeCliente': session.get('datos_cliente', {}).get('nitSedeCliente ', 'Nit_inexistente'),
        'nombreSedeCliente': session.get('datos_cliente', {}).get('nombreSedeCliente ', 'Nombre_inexistente'),
        'direccionSedeCliente': session.get('datos_cliente', {}).get('direccionSedeCliente ', 'Direccion_inexistente'),
        'gmailSedeCliente': session.get('datos_cliente', {}).get('gmailSedeCliente ', 'Gmail_inexistente'),
        'contrasenaSedeCliente': session.get('datos_cliente', {}).get('contrasenaSedeCliente ', 'Contraseña_inexistente'),
        'telefonoSedeCliente': session.get('datos_cliente', {}).get('telefonoSedeCliente ', 'Telefono_inexistente'),
        'departamentoSedeCliente': session.get('datos_cliente', {}).get('departamentoSedeCliente ', 'Departamento_inexistente'),
        'nombreEncargadoSedeCliente': session.get('datos_cliente', {}).get('nombreEncargadoSedeCliente ', 'Nombre_e_inexistente'),
        'telefonoEncargadoSedeCliente': session.get('datos_cliente', {}).get('telefonoEncargadoSedeCliente ', 'Telefono_e_inexistente'),
        'gmailEncargadoSedeCliente': session.get('datos_cliente', {}).get('gmailEncargadoSedeCliente ', 'Gmail_e_inexistente')
    }
    return render_template('Sede_cliente/certificado.html', **context); 

