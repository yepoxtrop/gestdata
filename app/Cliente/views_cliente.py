from . import Cliente; 
from app.config import configracion_base;
secret_key = configracion_base.SECRET_KEY; 
from flask import render_template, redirect, url_for, flash, request, session;
from datetime import datetime, timedelta, date;
from werkzeug.security import generate_password_hash
from app.Cliente.funciones_mutimedia import foto_encargado, logo_cliente; 


@Cliente.route('/plantilla')
def plantilla():
    return render_template('cliente/components/plantilla.html')

#mensaje de bienvenida
@Cliente.route('/ui')
def ui_cliente():
    
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('idCliente', 'id_inexistente'),
        'nombre_Comercial_Cliente' : session.get('datos_cliente', {}).get('nombreComercialCliente', 'nombre_inexistente'),
        'razon_Social_Cliente' : session.get('datos_cliente', {}).get('razonSocialCliente', 'razon_inexistente'),
        'telefono_Cliente' : session.get('datos_cliente', {}).get('telefonoCliente', 'telefono_no_encontrado'),
        'gmail_Cliente' : session.get('datos_cliente', {}).get('gmailCliente', 'gmail_inexistente'),
        'direcion_Cliente' : session.get('datos_cliente', {}).get('direcionCliente', 'direccion_inexistente'),
        'descripcion_Cliente' : session.get('datos_cliente', {}).get('descripcionCliente', 'descripcion_inexistente'),
        'logo_Cliente' : session.get('datos_cliente', {}).get('logoCliente', 'logo_inexistente'),
        'contrasena_Cliente' : session.get('datos_cliente', {}).get('contrasenaCliente', 'contraseña_inexistente'),
        'estado_Cliente' : session.get('datos_cliente', {}).get('estadoCliente', 'estado_inexistente')
    }
    return render_template('cliente/ui_cliente.html', **context)

#servicios solicitados
@Cliente.route('/servicio')
def servicio():
    
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('idCliente', 'id_inexistente'),
        'nombre_Comercial_Cliente' : session.get('datos_cliente', {}).get('nombreComercialCliente', 'nombre_inexistente'),
        'razon_Social_Cliente' : session.get('datos_cliente', {}).get('razonSocialCliente', 'razon_inexistente'),
        'telefono_Cliente' : session.get('datos_cliente', {}).get('telefonoCliente', 'telefono_no_encontrado'),
        'gmail_Cliente' : session.get('datos_cliente', {}).get('gmailCliente', 'gmail_inexistente'),
        'direcion_Cliente' : session.get('datos_cliente', {}).get('direcionCliente', 'direccion_inexistente'),
        'descripcion_Cliente' : session.get('datos_cliente', {}).get('descripcionCliente', 'descripcion_inexistente'),
        'logo_Cliente' : session.get('datos_cliente', {}).get('logoCliente', 'logo_inexistente'),
        'contrasena_Cliente' : session.get('datos_cliente', {}).get('contrasenaCliente', 'contraseña_inexistente'),
        'estado_Cliente' : session.get('datos_cliente', {}).get('estadoCliente', 'estado_inexistente')
    }
    
    from app import mysql;
    cur = mysql.connection.cursor(); 
    
    cur.execute("select empresaFumigadora.idEmpresaFumigadora, empresaFumigadora.nombreEmpresaFumigadora, sedesCliente.idSedeCliente, sedesCliente.nombreSedeCliente, servicio.idServicio, servicio.descripcionServicio, servicio.fechaSolicitudServicio, servicio.fechaInicioServicio, servicio.fechaFinalServicio, servicio.estadoServicio, empleado.nombresEmpleado from empresaFumigadora left join empleado on empresaFumigadora.idEmpresaFumigadora = empleado.idEmpresaFumigadoraFk right join servicio on servicio.idEmpleadoFk = empleado.idEmpleado inner join sedesCliente on servicio.idSedeClienteFk = sedesCliente.idSedeCliente inner join cliente on cliente.idCliente = sedesCliente.idClienteFk where cliente.idCliente =%s;", (context['id_cliente'],))
    servicios = cur.fetchall(); 
    
    if servicios:
        session['servicios'] = []
        
        for servicios_cliente in servicios:
            session['servicios'].append({
                'id_empresa_fumigadora' : servicios_cliente[0],
                'empresa_fumigadora' : servicios_cliente[1],
                'id_sede' : servicios_cliente[2],
                'sede' : servicios_cliente[3],
                'id_servicio' : servicios_cliente[4],
                'descripcion' : servicios_cliente[5],
                'solicitud' : servicios_cliente[6],
                'inicio' : servicios_cliente[7],
                'final' : servicios_cliente[8],
                'estado' : servicios_cliente[9],
                'empleado' : servicios_cliente[10]
            })
        print (session['servicios'])
    else:
        return render_template('cliente/servicios/no_servicios.html', **context)
    
    
    return render_template('cliente/Servicios.html', **context)

#certificado
@Cliente.route('/certificado/<int:index>')
def certificado(index):
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('idCliente', 'id_inexistente'),
        'nombre_Comercial_Cliente' : session.get('datos_cliente', {}).get('nombreComercialCliente', 'nombre_inexistente'),
        'razon_Social_Cliente' : session.get('datos_cliente', {}).get('razonSocialCliente', 'razon_inexistente'),
        'telefono_Cliente' : session.get('datos_cliente', {}).get('telefonoCliente', 'telefono_no_encontrado'),
        'gmail_Cliente' : session.get('datos_cliente', {}).get('gmailCliente', 'gmail_inexistente'),
        'direcion_Cliente' : session.get('datos_cliente', {}).get('direcionCliente', 'direccion_inexistente'),
        'descripcion_Cliente' : session.get('datos_cliente', {}).get('descripcionCliente', 'descripcion_inexistente'),
        'logo_Cliente' : session.get('datos_cliente', {}).get('logoCliente', 'logo_inexistente'),
        'contrasena_Cliente' : session.get('datos_cliente', {}).get('contrasenaCliente', 'contraseña_inexistente'),
        'estado_Cliente' : session.get('datos_cliente', {}).get('estadoCliente', 'estado_inexistente')
    }
    
    
    id_empresa_fumigadora = session['servicios'][index]['id_empresa_fumigadora']
    empresa_fumigadora = session['servicios'][index]['empresa_fumigadora']
    id_sede = session['servicios'][index]['id_sede']
    sede = session['servicios'][index]['sede']
    id_servicio = session['servicios'][index]['id_servicio']
    descripcion = session['servicios'][index]['descripcion']
    solicitud = session['servicios'][index]['solicitud']
    inicio = session['servicios'][index]['inicio']
    final = session['servicios'][index]['final']
    estado = session['servicios'][index]['estado']
    empleado = session['servicios'][index]['empleado']
    
    from app import mysql
    cur = mysql.connection.cursor()
    
    if empresa_fumigadora == None or inicio == None or final == None or estado=='en espera' or empleado==None:
        return render_template('cliente/servicios/no_certificado.html', **context)
    
    cur.execute("select nombreEncargadoEmpresaFumigadora from empresaFumigadora where idEmpresaFumigadora = %s", (id_empresa_fumigadora,))
    encargado_fumigadora = cur.fetchone()
    
    cur.execute("select nombreEncargadoSedeCliente from sedesCliente where idSedeCliente =%s", (id_sede,))
    encargado_sede = cur.fetchone()
    
    context2 = {
        'id_empresa_fumigadora' : id_empresa_fumigadora,
        'empresa_fumigadora' : empresa_fumigadora,
        'id_sede' : id_sede,
        'sede' : sede,
        'id_servicio' : id_servicio,
        'descripcion' : descripcion,
        'solicitud' : solicitud,
        'inicio' : inicio,
        'final' : final,
        'estado' : estado,
        'empleado' : empleado,
        'encargado_fumigadora': encargado_fumigadora[0],
        'encargado_sede': encargado_sede[0]
    }
    
    
    
    return render_template('cliente/servicios/certificado.html', **context, **context2)

@Cliente.route('/desacragr_certificado/<string:nombre_Comercial_Cliente>/<string:sede>/<string:encargado_sede>/<string:encargado_fumigadora>/<string:final>/<string:empresa_fumigadora>')
def desacragr_certificado(nombre_Comercial_Cliente, sede, encargado_sede, encargado_fumigadora, final, empresa_fumigadora):
    context2 = {
        'nombre_Comercial_Cliente' : nombre_Comercial_Cliente,
        'sede'  : sede,
        'encargado_sede'  : encargado_sede,
        'encargado_fumigadora' : encargado_fumigadora,
        'final' : final,
        'empresa_fumigadora' : empresa_fumigadora
    }
    return redirect(url_for('Documentos.descargar_certificado2', nombre_cliente=context2['nombre_Comercial_Cliente'], sede_cliente=context2['sede'], encargado_sede=context2['encargado_sede'], encargado_empresa_fumigador=context2['encargado_fumigadora'], fecha_final=context2['final'], empresa_fumigadora=context2['empresa_fumigadora']))

#reporte
@Cliente.route("/reporte/<int:indice>")
def reporte(indice):
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('idCliente', 'id_inexistente'),
        'nombre_Comercial_Cliente' : session.get('datos_cliente', {}).get('nombreComercialCliente', 'nombre_inexistente'),
        'razon_Social_Cliente' : session.get('datos_cliente', {}).get('razonSocialCliente', 'razon_inexistente'),
        'telefono_Cliente' : session.get('datos_cliente', {}).get('telefonoCliente', 'telefono_no_encontrado'),
        'gmail_Cliente' : session.get('datos_cliente', {}).get('gmailCliente', 'gmail_inexistente'),
        'direcion_Cliente' : session.get('datos_cliente', {}).get('direcionCliente', 'direccion_inexistente'),
        'descripcion_Cliente' : session.get('datos_cliente', {}).get('descripcionCliente', 'descripcion_inexistente'),
        'logo_Cliente' : session.get('datos_cliente', {}).get('logoCliente', 'logo_inexistente'),
        'contrasena_Cliente' : session.get('datos_cliente', {}).get('contrasenaCliente', 'contraseña_inexistente'),
        'estado_Cliente' : session.get('datos_cliente', {}).get('estadoCliente', 'estado_inexistente')
    }
    
    id_empresa_fumigadora = session['servicios'][indice]['id_empresa_fumigadora']
    empresa_fumigadora = session['servicios'][indice]['empresa_fumigadora']
    id_sede = session['servicios'][indice]['id_sede']
    sede = session['servicios'][indice]['sede']
    id_servicio = session['servicios'][indice]['id_servicio']
    descripcion = session['servicios'][indice]['descripcion']
    solicitud = session['servicios'][indice]['solicitud']
    inicio = session['servicios'][indice]['inicio']
    final = session['servicios'][indice]['final']
    estado = session['servicios'][indice]['estado']
    empleado = session['servicios'][indice]['empleado']
    print(id_servicio)
    
    from app import mysql;
    
    cur = mysql.connection.cursor(); 
    
    cur.execute(" select detallesServicio.valorDetalle, detallesServicio.idCaracteristicaFk, clases.nombreClases, caracteristicas.nombreCaracteristicas, caracteristicas.idclasesFk from detallesServicio inner join caracteristicas on caracteristicas.idCaracteristicas = detallesServicio.idCaracteristicaFk inner join clases on clases.idClases = caracteristicas.idClasesFk where idServicioFk = %s order by detallesServicio.idCaracteristicaFk ASC", (id_servicio,))    
    detalles_servicios = cur.fetchall(); 
    cantidad_detalle = len(detalles_servicios); 
    
    if cantidad_detalle == 0:
        return render_template('cliente/servicios/no_reporte.html', **context); 
    
    session['detalles_servicios_1'] = []
    session['detalles_servicios_2'] = []
    session['detalles_servicios_3'] = []


    for detalles_servicio in detalles_servicios:
        if detalles_servicio[4] == 2: 
            session['detalles_servicios_1'].append({
                'detalle' : detalles_servicio[0],
                'id_caracteristica' : detalles_servicio[1],
                'clase' : detalles_servicio[2], 
                'caracteristica' : detalles_servicio[3],
                'id_clase' : detalles_servicio[4]
            })
            
        if detalles_servicio[4] == 1:
            session['detalles_servicios_2'].append({
                'detalle' : detalles_servicio[0],
                'id_caracteristica' : detalles_servicio[1],
                'clase' : detalles_servicio[2], 
                'caracteristica' : detalles_servicio[3],
                'id_clase' : detalles_servicio[4]
            })
            
        if detalles_servicio[4] == 3:
            session['detalles_servicios_3'].append({
                'detalle' : detalles_servicio[0],
                'id_caracteristica' : detalles_servicio[1],
                'clase' : detalles_servicio[2], 
                'caracteristica' : detalles_servicio[3],
                'id_clase' : detalles_servicio[4]
            })
    
    longitud1 = len(session['detalles_servicios_1'])
    longitud2 = len(session['detalles_servicios_2'])
    longitud3 = len(session['detalles_servicios_3'])
    
    
    print(longitud1)
    print(longitud2)
    print(longitud3)
    
    cur.execute("select *from empresaFumigadora where idEmpresaFumigadora = %s", (id_empresa_fumigadora,))
    cosulta = cur.fetchone()

    context4 = {
        'id_emp' : cosulta[0],
        'nit_emp' : cosulta[2],
        'direccion_emp' : cosulta[4],
        'dep_emp' : cosulta[5],
        'tel_emp' : cosulta[8],
        'email_emp' : cosulta[9],
        'encarg_nom' : cosulta[10],
        'encarg_email' : cosulta[11],
        'encar_tel' : cosulta[12],
    }
    
    context2 ={
        'empresa_fumigadora' :empresa_fumigadora,
        'nit' : context4['nit_emp'],
        'telefono' : context4['tel_emp'],
        'encargado_telefono' : context4['encar_tel'],
        'direccion' : context4['direccion_emp'],
        'departamento' : context4['dep_emp'],
        'correo' : context4['email_emp'],
        'encargado_correo' : context4['encarg_email'],
        'nombre_cliente' : context['nombre_Comercial_Cliente'],
        'empleado' : empleado
    }
    
    context3 ={
        'longitud1' : longitud1,
        'longitud2' : longitud2,
        'longitud3' : longitud3
    }
    
    return render_template('cliente/servicios/reporte.html', **context2, **context3)

#solicitar servicios
@Cliente.route("/solicitar")
def solicitar():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('idCliente', 'id_inexistente'),
        'nombre_Comercial_Cliente' : session.get('datos_cliente', {}).get('nombreComercialCliente', 'nombre_inexistente'),
        'razon_Social_Cliente' : session.get('datos_cliente', {}).get('razonSocialCliente', 'razon_inexistente'),
        'telefono_Cliente' : session.get('datos_cliente', {}).get('telefonoCliente', 'telefono_no_encontrado'),
        'gmail_Cliente' : session.get('datos_cliente', {}).get('gmailCliente', 'gmail_inexistente'),
        'direcion_Cliente' : session.get('datos_cliente', {}).get('direcionCliente', 'direccion_inexistente'),
        'descripcion_Cliente' : session.get('datos_cliente', {}).get('descripcionCliente', 'descripcion_inexistente'),
        'logo_Cliente' : session.get('datos_cliente', {}).get('logoCliente', 'logo_inexistente'),
        'contrasena_Cliente' : session.get('datos_cliente', {}).get('contrasenaCliente', 'contraseña_inexistente'),
        'estado_Cliente' : session.get('datos_cliente', {}).get('estadoCliente', 'estado_inexistente')
    }
    
    from app import mysql;
    
    cur = mysql.connection.cursor(); 
    
    cur.execute("select nombreSedeCliente from sedesCliente where idClienteFk=%s", (context['id_cliente'],))
    sedes = cur.fetchall(); 
    
    session['sedes'] = []
    
    for sedes_cliente in sedes:
        session['sedes'].append({
            'nombre_sede' : sedes_cliente[0]
        })
    return render_template('cliente/servicios/solicitar.html', **context)

@Cliente.route("/solicitar_servicio", methods=['POST'])
def solicitar_servicio():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('idCliente', 'id_inexistente'),
        'nombre_Comercial_Cliente' : session.get('datos_cliente', {}).get('nombreComercialCliente', 'nombre_inexistente'),
        'razon_Social_Cliente' : session.get('datos_cliente', {}).get('razonSocialCliente', 'razon_inexistente'),
        'telefono_Cliente' : session.get('datos_cliente', {}).get('telefonoCliente', 'telefono_no_encontrado'),
        'gmail_Cliente' : session.get('datos_cliente', {}).get('gmailCliente', 'gmail_inexistente'),
        'direcion_Cliente' : session.get('datos_cliente', {}).get('direcionCliente', 'direccion_inexistente'),
        'descripcion_Cliente' : session.get('datos_cliente', {}).get('descripcionCliente', 'descripcion_inexistente'),
        'logo_Cliente' : session.get('datos_cliente', {}).get('logoCliente', 'logo_inexistente'),
        'contrasena_Cliente' : session.get('datos_cliente', {}).get('contrasenaCliente', 'contraseña_inexistente'),
        'estado_Cliente' : session.get('datos_cliente', {}).get('estadoCliente', 'estado_inexistente')
    }
    
    sede = request.form['sede']
    descripcion = request.form['descripcion']
    
    from app import mysql
    
    cur = mysql.connection.cursor(); 
    
    cur.execute("select idSedeCliente from sedesCliente where idClienteFk=%s and nombreSedeCliente=%s",(context['id_cliente'], sede,))
    id_sede=cur.fetchone()
    
    cur.execute("insert into servicio(descripcionServicio, idSedeClienteFk) value(%s, %s)", (descripcion, id_sede[0]))
    cur.connection.commit(); 
    
    return render_template('cliente/servicios/mensajes/servicio_solicitado.html', **context)

#sedes
@Cliente.route("/sedes")
def sedes():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('idCliente', 'id_inexistente'),
        'nombre_Comercial_Cliente' : session.get('datos_cliente', {}).get('nombreComercialCliente', 'nombre_inexistente'),
        'razon_Social_Cliente' : session.get('datos_cliente', {}).get('razonSocialCliente', 'razon_inexistente'),
        'telefono_Cliente' : session.get('datos_cliente', {}).get('telefonoCliente', 'telefono_no_encontrado'),
        'gmail_Cliente' : session.get('datos_cliente', {}).get('gmailCliente', 'gmail_inexistente'),
        'direcion_Cliente' : session.get('datos_cliente', {}).get('direcionCliente', 'direccion_inexistente'),
        'descripcion_Cliente' : session.get('datos_cliente', {}).get('descripcionCliente', 'descripcion_inexistente'),
        'logo_Cliente' : session.get('datos_cliente', {}).get('logoCliente', 'logo_inexistente'),
        'contrasena_Cliente' : session.get('datos_cliente', {}).get('contrasenaCliente', 'contraseña_inexistente'),
        'estado_Cliente' : session.get('datos_cliente', {}).get('estadoCliente', 'estado_inexistente')
    }

    from app import mysql; 
    cur = mysql.connect.cursor(); 

    cur.execute("select *from sedesCliente where idClienteFk = %s", (context['id_cliente'],))
    sedes= cur.fetchall()
    print(sedes)

    if len(sedes) ==0:
        return render_template('cliente/sedes/no_hay.html', **context)

    session['sedes'] =[]

    for sedes_cliente in sedes:
        session['sedes'].append({
            'idSedeCliente': sedes_cliente[0],
            'nitSedeCliente': sedes_cliente[1],
            'nombreSedeCliente': sedes_cliente[2],
            'direccionSedeCliente': sedes_cliente[3],
            'gmailSedeCliente': sedes_cliente[4],
            'contrasenaSedeCliente': sedes_cliente[5],
            'telefonoSedeCliente': sedes_cliente[6],
            'departamentoSedeCliente': sedes_cliente[7],
            'logoSedeCliente': sedes_cliente[8],
            'nombreEncargadoSedeCliente': sedes_cliente[9],
            'telefonoEncargadoSedeCliente': sedes_cliente[10],
            'gmailEncargadoSedeCliente': sedes_cliente[11],
            'fotoEncargadoSedeCliente': sedes_cliente[12],
            'idClienteFk': sedes_cliente[13],
            'estadoSede': sedes_cliente[14]
        })

    return render_template('cliente/Sedes.html', **context)

#insertar sede
@Cliente.route("/sedes_form")
def sedes_form():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('idCliente', 'id_inexistente'),
        'nombre_Comercial_Cliente' : session.get('datos_cliente', {}).get('nombreComercialCliente', 'nombre_inexistente'),
        'razon_Social_Cliente' : session.get('datos_cliente', {}).get('razonSocialCliente', 'razon_inexistente'),
        'telefono_Cliente' : session.get('datos_cliente', {}).get('telefonoCliente', 'telefono_no_encontrado'),
        'gmail_Cliente' : session.get('datos_cliente', {}).get('gmailCliente', 'gmail_inexistente'),
        'direcion_Cliente' : session.get('datos_cliente', {}).get('direcionCliente', 'direccion_inexistente'),
        'descripcion_Cliente' : session.get('datos_cliente', {}).get('descripcionCliente', 'descripcion_inexistente'),
        'logo_Cliente' : session.get('datos_cliente', {}).get('logoCliente', 'logo_inexistente'),
        'contrasena_Cliente' : session.get('datos_cliente', {}).get('contrasenaCliente', 'contraseña_inexistente'),
        'estado_Cliente' : session.get('datos_cliente', {}).get('estadoCliente', 'estado_inexistente')
    }
    return render_template('cliente/sedes/crear.html', **context)

@Cliente.route("/insertar", methods=['POST'])
def insertar_sede():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('idCliente', 'id_inexistente'),
        'nombre_Comercial_Cliente' : session.get('datos_cliente', {}).get('nombreComercialCliente', 'nombre_inexistente'),
        'razon_Social_Cliente' : session.get('datos_cliente', {}).get('razonSocialCliente', 'razon_inexistente'),
        'telefono_Cliente' : session.get('datos_cliente', {}).get('telefonoCliente', 'telefono_no_encontrado'),
        'gmail_Cliente' : session.get('datos_cliente', {}).get('gmailCliente', 'gmail_inexistente'),
        'direcion_Cliente' : session.get('datos_cliente', {}).get('direcionCliente', 'direccion_inexistente'),
        'descripcion_Cliente' : session.get('datos_cliente', {}).get('descripcionCliente', 'descripcion_inexistente'),
        'logo_Cliente' : session.get('datos_cliente', {}).get('logoCliente', 'logo_inexistente'),
        'contrasena_Cliente' : session.get('datos_cliente', {}).get('contrasenaCliente', 'contraseña_inexistente'),
        'estado_Cliente' : session.get('datos_cliente', {}).get('estadoCliente', 'estado_inexistente')
    }
    
    if request.method == 'GET':
        flash("Error al crear la sede"); 
        return render_template('cliente/sedes/crear.html', **context)
    else:
        archivo_logo = request.files['logo_cliente']
        archivo_empleado = request.files['foto_encargado']
        nit = request.form['nit']
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        correo1 = request.form['correo1']
        telefono = request.form['telefono']
        departamento = request.form['departamento']
        encargado = request.form['encargado']
        correo2 = request.form['correo2']
        encargado_tel = request.form['encargado_tel']
        contaseña = request.form['contraseña']
        contraseña_cifrda = generate_password_hash(contaseña, 'pbkdf2:sha256:5', 5)
        
        path_logo = logo_cliente(nombre, archivo_logo)
        path_empleado = foto_encargado(encargado, archivo_empleado)
    
    
    
        from app import mysql; 
    
        cur = mysql.connection.cursor()
    
        cur.execute("select *from sedesCliente where nitSedeCliente = %s or gmailSedeCliente = %s or telefonoSedeCliente = %s or gmailEncargadoSedeCliente  = %s or telefonoEncargadoSedeCliente = %s", (nit, correo1, telefono, correo2, encargado_tel))
        consulta1 = cur.fetchall(); 
    
        if len(consulta1) >0:
            flash("Algún correo/nit/teléfono ya existe"); 
            return render_template('cliente/sedes/crear.html', **context)
    
    
        cur.execute("insert into sedesCliente(nitSedeCliente, nombreSedeCliente, direccionSedeCliente, gmailSedeCliente, contrasenaSedeCliente, telefonoSedeCliente, departamentoSedeCliente, logoSedeCliente, nombreEncargadoSedeCliente, telefonoEncargadoSedeCliente, gmailEncargadoSedeCliente, fotoEncargadoSedeCliente, idClienteFk) value(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (nit, nombre, direccion, correo1, contraseña_cifrda, telefono, departamento, path_logo, encargado, encargado_tel, correo2, path_empleado, context['id_cliente'],))
        cur.connection.commit()
    
    return render_template('cliente/sedes/creada.html', **context)

#editar_sede
@Cliente.route("/editar_Sede/<int:index>")
def editar_sede(index):
    id_sede = session['sedes'][index]['idSedeCliente']
    nitSedeCliente = session['sedes'][index]['nitSedeCliente']
    nombreSedeCliente = session['sedes'][index]['nombreSedeCliente']
    gmailSedeCliente = session['sedes'][index]['gmailSedeCliente']
    telefonoSedeCliente = session['sedes'][index]['telefonoSedeCliente']
    nombreEncargadoSedeCliente = session['sedes'][index]['nombreEncargadoSedeCliente']
    
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('idCliente', 'id_inexistente'),
        'nombre_Comercial_Cliente' : session.get('datos_cliente', {}).get('nombreComercialCliente', 'nombre_inexistente'),
        'razon_Social_Cliente' : session.get('datos_cliente', {}).get('razonSocialCliente', 'razon_inexistente'),
        'telefono_Cliente' : session.get('datos_cliente', {}).get('telefonoCliente', 'telefono_no_encontrado'),
        'gmail_Cliente' : session.get('datos_cliente', {}).get('gmailCliente', 'gmail_inexistente'),
        'direcion_Cliente' : session.get('datos_cliente', {}).get('direcionCliente', 'direccion_inexistente'),
        'descripcion_Cliente' : session.get('datos_cliente', {}).get('descripcionCliente', 'descripcion_inexistente'),
        'logo_Cliente' : session.get('datos_cliente', {}).get('logoCliente', 'logo_inexistente'),
        'contrasena_Cliente' : session.get('datos_cliente', {}).get('contrasenaCliente', 'contraseña_inexistente'),
        'estado_Cliente' : session.get('datos_cliente', {}).get('estadoCliente', 'estado_inexistente')
    }
    
    context2 = {
        'id_sede' : id_sede,
        'nitSedeCliente' : nitSedeCliente,
        'nombreSedeCliente' : nombreSedeCliente,
        'gmailSedeCliente' : gmailSedeCliente, 
        'telefonoSedeCliente' : telefonoSedeCliente,
        'nombreEncargadoSedeCliente' : nombreEncargadoSedeCliente
    }
    
    return render_template('cliente/sedes/editar.html', **context, **context2)

@Cliente.route("/actualizar_sede", methods=['POST'])
def actualizar_sede():
    
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('idCliente', 'id_inexistente'),
        'nombre_Comercial_Cliente' : session.get('datos_cliente', {}).get('nombreComercialCliente', 'nombre_inexistente'),
        'razon_Social_Cliente' : session.get('datos_cliente', {}).get('razonSocialCliente', 'razon_inexistente'),
        'telefono_Cliente' : session.get('datos_cliente', {}).get('telefonoCliente', 'telefono_no_encontrado'),
        'gmail_Cliente' : session.get('datos_cliente', {}).get('gmailCliente', 'gmail_inexistente'),
        'direcion_Cliente' : session.get('datos_cliente', {}).get('direcionCliente', 'direccion_inexistente'),
        'descripcion_Cliente' : session.get('datos_cliente', {}).get('descripcionCliente', 'descripcion_inexistente'),
        'logo_Cliente' : session.get('datos_cliente', {}).get('logoCliente', 'logo_inexistente'),
        'contrasena_Cliente' : session.get('datos_cliente', {}).get('contrasenaCliente', 'contraseña_inexistente'),
        'estado_Cliente' : session.get('datos_cliente', {}).get('estadoCliente', 'estado_inexistente')
    }
    
    id_sede = request.form['id_sede']
    nitSedeCliente = request.form['nit']
    nombreSedeCliente = request.form['nombre']
    gmailSedeCliente = request.form['correo']
    telefonoSedeCliente = request.form['telefono']
    nombreEncargadoSedeCliente = request.form['gerente']
    
    from app import mysql; 
    
    cur = mysql.connection.cursor()
    
    cur.execute("select *from sedesCliente where nitSedeCliente = %s or  telefonoSedeCliente = %s or gmailSedeCliente=%s", (nitSedeCliente, telefonoSedeCliente, gmailSedeCliente,))
    consulta = cur.fetchall()
    
    if len(consulta)>0:
        flash("El nit/telefono/correo puede que este repetido")
        return render_template('cliente/Sedes.html', **context)
    
    cur.execute("update sedesCliente set nitSedeCliente = %s, nombreSedeCliente=%s, gmailSedeCliente=%s, telefonoSedeCliente=%s, nombreEncargadoSedeCliente=%s where idSedeCliente=%s", (nitSedeCliente, nombreSedeCliente, gmailSedeCliente,telefonoSedeCliente,nombreEncargadoSedeCliente,id_sede,))
    cur.connection.commit()
    
    return render_template('cliente/sedes/editado.html', **context)

#gerentes
@Cliente.route("/gerentes")
def gerentes():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('idCliente', 'id_inexistente'),
        'nombre_Comercial_Cliente' : session.get('datos_cliente', {}).get('nombreComercialCliente', 'nombre_inexistente'),
        'razon_Social_Cliente' : session.get('datos_cliente', {}).get('razonSocialCliente', 'razon_inexistente'),
        'telefono_Cliente' : session.get('datos_cliente', {}).get('telefonoCliente', 'telefono_no_encontrado'),
        'gmail_Cliente' : session.get('datos_cliente', {}).get('gmailCliente', 'gmail_inexistente'),
        'direcion_Cliente' : session.get('datos_cliente', {}).get('direcionCliente', 'direccion_inexistente'),
        'descripcion_Cliente' : session.get('datos_cliente', {}).get('descripcionCliente', 'descripcion_inexistente'),
        'logo_Cliente' : session.get('datos_cliente', {}).get('logoCliente', 'logo_inexistente'),
        'contrasena_Cliente' : session.get('datos_cliente', {}).get('contrasenaCliente', 'contraseña_inexistente'),
        'estado_Cliente' : session.get('datos_cliente', {}).get('estadoCliente', 'estado_inexistente')
    }

    from app import mysql; 
    cur = mysql.connection.cursor()

    cur.execute("select idSedeCliente, nombreEncargadoSedeCliente, telefonoEncargadoSedeCliente, gmailEncargadoSedeCliente, nombreSedeCliente from sedesCliente where idClienteFk = %s", (context['id_cliente'],))
    gerentes = cur.fetchall()

    if len(gerentes) == 0:
        return render_template('cliente/gerente/no_gerentes.html', **context)

    session['gerentes']=[]

    for gerentes_sedes in gerentes:
        session['gerentes'].append({
            'idsede' : gerentes_sedes[0],
            'nombre': gerentes_sedes[1],
            'tel': gerentes_sedes[2],
            'gmail': gerentes_sedes[3],
            'sede': gerentes_sedes[4],
        })
        
    print(session['gerentes'])

    return render_template('cliente/gerente/gerentes.html', **context)

#editar gerente
@Cliente.route("/gerentes_Editar/<int:index>")
def gerentes_editar(index):
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('idCliente', 'id_inexistente'),
        'nombre_Comercial_Cliente' : session.get('datos_cliente', {}).get('nombreComercialCliente', 'nombre_inexistente'),
        'razon_Social_Cliente' : session.get('datos_cliente', {}).get('razonSocialCliente', 'razon_inexistente'),
        'telefono_Cliente' : session.get('datos_cliente', {}).get('telefonoCliente', 'telefono_no_encontrado'),
        'gmail_Cliente' : session.get('datos_cliente', {}).get('gmailCliente', 'gmail_inexistente'),
        'direcion_Cliente' : session.get('datos_cliente', {}).get('direcionCliente', 'direccion_inexistente'),
        'descripcion_Cliente' : session.get('datos_cliente', {}).get('descripcionCliente', 'descripcion_inexistente'),
        'logo_Cliente' : session.get('datos_cliente', {}).get('logoCliente', 'logo_inexistente'),
        'contrasena_Cliente' : session.get('datos_cliente', {}).get('contrasenaCliente', 'contraseña_inexistente'),
        'estado_Cliente' : session.get('datos_cliente', {}).get('estadoCliente', 'estado_inexistente')
    }
    
    idsede = session['gerentes'][index]['idsede']; 
    nom_encargado = session['gerentes'][index]['nombre']; 
    tel_encargado = session['gerentes'][index]['tel']; 
    correo_encargado = session['gerentes'][index]['gmail']; 
    
    context2={
        'idsede' : idsede,
        'nom_encargado' : nom_encargado, 
        'tel_encargado' : tel_encargado, 
        'correo_encargado' : correo_encargado
    }
    
    print(context2)
    return render_template('cliente/gerente/editar.html', **context, **context2)

@Cliente.route("/actualizar_gerente", methods=['POST'])
def actualizar_gerente():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('idCliente', 'id_inexistente'),
        'nombre_Comercial_Cliente' : session.get('datos_cliente', {}).get('nombreComercialCliente', 'nombre_inexistente'),
        'razon_Social_Cliente' : session.get('datos_cliente', {}).get('razonSocialCliente', 'razon_inexistente'),
        'telefono_Cliente' : session.get('datos_cliente', {}).get('telefonoCliente', 'telefono_no_encontrado'),
        'gmail_Cliente' : session.get('datos_cliente', {}).get('gmailCliente', 'gmail_inexistente'),
        'direcion_Cliente' : session.get('datos_cliente', {}).get('direcionCliente', 'direccion_inexistente'),
        'descripcion_Cliente' : session.get('datos_cliente', {}).get('descripcionCliente', 'descripcion_inexistente'),
        'logo_Cliente' : session.get('datos_cliente', {}).get('logoCliente', 'logo_inexistente'),
        'contrasena_Cliente' : session.get('datos_cliente', {}).get('contrasenaCliente', 'contraseña_inexistente'),
        'estado_Cliente' : session.get('datos_cliente', {}).get('estadoCliente', 'estado_inexistente')
    }
    
    sede = request.form.get('id_sede')
    print(sede)
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    correo = request.form['correo']
    
    
    from app import mysql; 
    
    cur = mysql.connection.cursor()
    
    cur.execute("select idSedeCliente from sedesCliente where telefonoEncargadoSedeCliente = %s or gmailEncargadoSedeCliente = %s", (telefono, correo,))
    consulta = cur.fetchall()
    
    if len(consulta) >0:
        flash("Ya se encuentra repetido un dato correo o telefono")
        return redirect(url_for('Cliente.gerentes'))
    
    cur.execute("update sedesCliente set nombreEncargadoSedeCliente = %s, telefonoEncargadoSedeCliente = %s, gmailEncargadoSedeCliente = %s where idSedeCliente = %s", (nombre, telefono, correo, sede,))
    cur.connection.commit(); 
    
    return render_template('cliente/gerente/editado.html', **context)

#detalles
@Cliente.route("/detalles")
def detalles():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('idCliente', 'id_inexistente'),
        'nombre_Comercial_Cliente' : session.get('datos_cliente', {}).get('nombreComercialCliente', 'nombre_inexistente'),
        'razon_Social_Cliente' : session.get('datos_cliente', {}).get('razonSocialCliente', 'razon_inexistente'),
        'telefono_Cliente' : session.get('datos_cliente', {}).get('telefonoCliente', 'telefono_no_encontrado'),
        'gmail_Cliente' : session.get('datos_cliente', {}).get('gmailCliente', 'gmail_inexistente'),
        'direcion_Cliente' : session.get('datos_cliente', {}).get('direcionCliente', 'direccion_inexistente'),
        'descripcion_Cliente' : session.get('datos_cliente', {}).get('descripcionCliente', 'descripcion_inexistente'),
        'logo_Cliente' : session.get('datos_cliente', {}).get('logoCliente', 'logo_inexistente'),
        'contrasena_Cliente' : session.get('datos_cliente', {}).get('contrasenaCliente', 'contraseña_inexistente'),
        'estado_Cliente' : session.get('datos_cliente', {}).get('estadoCliente', 'estado_inexistente')
    }

    from app import mysql; 
    cur = mysql.connection.cursor()

    cur.execute("select empresaFumigadora.nombreEmpresaFumigadora, empleado.nombresEmpleado, servicio.idServicio, sedesCliente.nombreSedeCliente, clases.nombreClases, caracteristicas.nombreCaracteristicas, detallesServicio.valorDetalle from empresaFumigadora inner join empleado on empresaFumigadora.idEmpresaFumigadora = empleado.idEmpresaFumigadoraFk inner join servicio on servicio.idEmpleadoFk = empleado.idEmpleado inner join sedesCliente on servicio.idSedeClienteFk = sedesCliente.idSedeCliente inner join cliente on cliente.idCliente = sedesCliente.idClienteFk inner join detallesServicio on detallesServicio.idServicioFk = servicio.idServicio inner join  caracteristicas on detallesServicio.idCaracteristicaFk = caracteristicas.idCaracteristicas inner join clases on caracteristicas.idClasesFk = clases.idClases where cliente.idCliente = %s;", (context['id_cliente'],))
    detalles = cur.fetchall()
    print(detalles)
    
    
    if len(detalles) == 0:
        return render_template('cliente/detalles_servicios/no_detalles.html', **context)

    session['detalles']=[]
    
    for detalles_servicios in detalles:
        session['detalles'].append({
            'empresa':detalles_servicios[0],
            'empleado':detalles_servicios[1],
            'id_servicio':detalles_servicios[2],
            'sede':detalles_servicios[3],
            'clase':detalles_servicios[4],
            'caracteristica':detalles_servicios[5],
            'detalle':detalles_servicios[6]
        })
    return render_template('cliente/detalles_servicios/detalles.html', **context)

#eliminar_cuenta
@Cliente.route("/eliminar_user")
def eliminar_user():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('idCliente', 'id_inexistente'),
        'nombre_Comercial_Cliente' : session.get('datos_cliente', {}).get('nombreComercialCliente', 'nombre_inexistente'),
        'razon_Social_Cliente' : session.get('datos_cliente', {}).get('razonSocialCliente', 'razon_inexistente'),
        'telefono_Cliente' : session.get('datos_cliente', {}).get('telefonoCliente', 'telefono_no_encontrado'),
        'gmail_Cliente' : session.get('datos_cliente', {}).get('gmailCliente', 'gmail_inexistente'),
        'direcion_Cliente' : session.get('datos_cliente', {}).get('direcionCliente', 'direccion_inexistente'),
        'descripcion_Cliente' : session.get('datos_cliente', {}).get('descripcionCliente', 'descripcion_inexistente'),
        'logo_Cliente' : session.get('datos_cliente', {}).get('logoCliente', 'logo_inexistente'),
        'contrasena_Cliente' : session.get('datos_cliente', {}).get('contrasenaCliente', 'contraseña_inexistente'),
        'estado_Cliente' : session.get('datos_cliente', {}).get('estadoCliente', 'estado_inexistente')
    }
    return render_template('cliente/perfil/eliminar.html', **context)

@Cliente.route("/hacer_eliminar_cuenta")
def hacer_eliminar_cuenta():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('idCliente', 'id_inexistente'),
        'nombre_Comercial_Cliente' : session.get('datos_cliente', {}).get('nombreComercialCliente', 'nombre_inexistente'),
        'razon_Social_Cliente' : session.get('datos_cliente', {}).get('razonSocialCliente', 'razon_inexistente'),
        'telefono_Cliente' : session.get('datos_cliente', {}).get('telefonoCliente', 'telefono_no_encontrado'),
        'gmail_Cliente' : session.get('datos_cliente', {}).get('gmailCliente', 'gmail_inexistente'),
        'direcion_Cliente' : session.get('datos_cliente', {}).get('direcionCliente', 'direccion_inexistente'),
        'descripcion_Cliente' : session.get('datos_cliente', {}).get('descripcionCliente', 'descripcion_inexistente'),
        'logo_Cliente' : session.get('datos_cliente', {}).get('logoCliente', 'logo_inexistente'),
        'contrasena_Cliente' : session.get('datos_cliente', {}).get('contrasenaCliente', 'contraseña_inexistente'),
        'estado_Cliente' : session.get('datos_cliente', {}).get('estadoCliente', 'estado_inexistente')
    }

    from app import mysql
    cur = mysql.connection.cursor()

    cur.execute("update cliente set estadoCliente = false where idCliente = %s", (context['id_cliente'],))
    cur.connection.commit()

    cur.execute("update sedesCliente set estadoSede = false where idClienteFk = %s", (context['id_cliente'],))
    cur.connection.commit()

    return redirect(url_for('Login.cerrar_sesion')); 

#Editar_Cuente
@Cliente.route("/editar_user")
def editar_user():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('idCliente', 'id_inexistente'),
        'nombre_Comercial_Cliente' : session.get('datos_cliente', {}).get('nombreComercialCliente', 'nombre_inexistente'),
        'razon_Social_Cliente' : session.get('datos_cliente', {}).get('razonSocialCliente', 'razon_inexistente'),
        'telefono_Cliente' : session.get('datos_cliente', {}).get('telefonoCliente', 'telefono_no_encontrado'),
        'gmail_Cliente' : session.get('datos_cliente', {}).get('gmailCliente', 'gmail_inexistente'),
        'direcion_Cliente' : session.get('datos_cliente', {}).get('direcionCliente', 'direccion_inexistente'),
        'descripcion_Cliente' : session.get('datos_cliente', {}).get('descripcionCliente', 'descripcion_inexistente'),
        'logo_Cliente' : session.get('datos_cliente', {}).get('logoCliente', 'logo_inexistente'),
        'contrasena_Cliente' : session.get('datos_cliente', {}).get('contrasenaCliente', 'contraseña_inexistente'),
        'estado_Cliente' : session.get('datos_cliente', {}).get('estadoCliente', 'estado_inexistente')
    }
    return render_template('cliente/perfil/editar.html', **context)

@Cliente.route("/editado_user", methods=['POST'])
def editado_user():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('idCliente', 'id_inexistente'),
        'nombre_Comercial_Cliente' : session.get('datos_cliente', {}).get('nombreComercialCliente', 'nombre_inexistente'),
        'razon_Social_Cliente' : session.get('datos_cliente', {}).get('razonSocialCliente', 'razon_inexistente'),
        'telefono_Cliente' : session.get('datos_cliente', {}).get('telefonoCliente', 'telefono_no_encontrado'),
        'gmail_Cliente' : session.get('datos_cliente', {}).get('gmailCliente', 'gmail_inexistente'),
        'direcion_Cliente' : session.get('datos_cliente', {}).get('direcionCliente', 'direccion_inexistente'),
        'descripcion_Cliente' : session.get('datos_cliente', {}).get('descripcionCliente', 'descripcion_inexistente'),
        'logo_Cliente' : session.get('datos_cliente', {}).get('logoCliente', 'logo_inexistente'),
        'contrasena_Cliente' : session.get('datos_cliente', {}).get('contrasenaCliente', 'contraseña_inexistente'),
        'estado_Cliente' : session.get('datos_cliente', {}).get('estadoCliente', 'estado_inexistente')
    }

    nombre = request.form['comercial']
    direccion = request.form['direccion']
    descripcion = request.form['Descripción']

    from app import mysql;

    cur = mysql.connection.cursor()

    cur.execute("update cliente set nombreComercialCliente=%s, direcionCliente=%s, descripcionCliente=%s where idCliente =%s", (nombre, direccion, descripcion, context['id_cliente'],))

    return render_template('cliente/perfil/datos_actualizados.html', **context)
