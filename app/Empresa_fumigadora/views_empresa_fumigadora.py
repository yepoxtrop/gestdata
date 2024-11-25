from . import Empresa_fumigadora;
from flask import render_template, redirect, url_for, flash, request, session, jsonify;
from flask import session;
from app.config import configracion_base;
from datetime import datetime, timedelta, date;
from werkzeug.security import generate_password_hash
import smtplib
from email.mime.text import MIMEText

secret_key = configracion_base.SECRET_KEY; 

@Empresa_fumigadora.route('/plantilla')
def plantilla():
    return render_template('empresa_fumigadora/components/plantilla.html')

@Empresa_fumigadora.route('/ui')
def ui_empresa_fumigadora_index():
    
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    return render_template('empresa_fumigadora/ui_empresa_fumigadora.html', **context)

#Servicios completos
@Empresa_fumigadora.route('/Servicios')
def servicios_atendidos():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    
    from app import mysql;
    
    cur = mysql.connection.cursor(); 
    
    cur.execute("""select empresafumigadora.nombreEmpresaFumigadora,
	               cliente.nombreComercialCliente,
	               sedescliente.nombreSedeCliente,
                   servicio.descripcionServicio,
                   servicio.fechaSolicitudServicio,
                   servicio.fechaInicioServicio,
                   servicio.fechaFinalServicio,
                   servicio.estadoServicio,
                   empleado.nombresEmpleado,
                   servicio.idServicio,
                   sedescliente.nombreEncargadoSedeCliente
                   from servicio 
                   inner join sedescliente on servicio.idSedeClienteFk = sedescliente.idSedeCliente
                   inner join cliente on cliente.idCliente = sedescliente.idClienteFk
                   inner join empleado on empleado.idEmpleado = servicio.idEmpleadoFk
                   inner join empresafumigadora on empresafumigadora.idEmpresaFumigadora  = empleado.idEmpresaFumigadoraFk
                   where servicio.estadoServicio = 'finalizado' and empresafumigadora.idEmpresaFumigadora=%s;
                   """, (context['id_cliente'],))
    servicios = cur.fetchall(); 
    print(servicios); 
    
    if servicios:
        session['servicios_atenddos'] = []
        
        for sevicios_atendidos in servicios:
            session['servicios_atenddos'].append({
                'empresa_fumigadora' : sevicios_atendidos[0],
                'cliente' : sevicios_atendidos[1],
                'sede_cliente' : sevicios_atendidos[2],
                'descripcion_servicio' : sevicios_atendidos[3],
                'fecha_solicitud' : sevicios_atendidos[4],
                'fecha_inicio' : sevicios_atendidos[5],
                'fecha_fin' : sevicios_atendidos[6],
                'estado_Servicio' : sevicios_atendidos[7],
                'empleado' : sevicios_atendidos[8],
                'id_servicio' : sevicios_atendidos[9],
                'encargado_cliente' : sevicios_atendidos[10]
            })
    
    else:
        return  render_template('empresa_fumigadora/servicios/mensaje_no_encontrado/servicios_completos.html', **context)

    print(session['servicios_atenddos']); 
    return render_template('empresa_fumigadora/Servicios.html', **context)

#Certificado
@Empresa_fumigadora.route('/Capturar_indice/<int:index>')
def capturar_indice(index):
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    
    nombre_cliente = session['servicios_atenddos'][index]['cliente']; 
    sede_cliente = session['servicios_atenddos'][index]['sede_cliente']; 
    encargado_sede = session['servicios_atenddos'][index]['encargado_cliente']; 
    encargado_empresa_fumigador = context['encargado_nombre']; 
    fecha_final = session['servicios_atenddos'][index]['fecha_fin']; 
    empresa_fumigadora = session['servicios_atenddos'][index]['empresa_fumigadora']; 
    
    if fecha_final == None:
        fecha_final = 'Fecha no definida'
    
    context2 = {
        'nombre_cliente' : nombre_cliente,
        'sede_cliente'  : sede_cliente,
        'encargado_sede'  : encargado_sede,
        'encargado_empresa_fumigador' : encargado_empresa_fumigador,
        'fecha_final' : fecha_final,
        'empresa_fumigadora' : empresa_fumigadora
    }
    #Certificados_descargar.html
    return render_template('empresa_fumigadora/Certificados.html', **context2); 

@Empresa_fumigadora.route('/desacragr_certificado/<string:nombre_cliente>/<string:sede_cliente>/<string:encargado_sede>/<string:encargado_empresa_fumigador>/<string:fecha_final>/<string:empresa_fumigadora>')
def desacragr_certificado(nombre_cliente, sede_cliente, encargado_sede, encargado_empresa_fumigador, fecha_final, empresa_fumigadora):
    context2 = {
        'nombre_cliente' : nombre_cliente,
        'sede_cliente'  : sede_cliente,
        'encargado_sede'  : encargado_sede,
        'encargado_empresa_fumigador' : encargado_empresa_fumigador,
        'fecha_final' : fecha_final,
        'empresa_fumigadora' : empresa_fumigadora
    }
    return redirect(url_for('Documentos.descargar_certificado', nombre_cliente=context2['nombre_cliente'], sede_cliente=context2['sede_cliente'], encargado_sede=context2['encargado_sede'], encargado_empresa_fumigador=context2['encargado_empresa_fumigador'], fecha_final=context2['fecha_final'], empresa_fumigadora=context2['empresa_fumigadora']))

#Reporte
@Empresa_fumigadora.route('/reporte/<int:indice>')
def reporte(indice):
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    
    id_servicio = session['servicios_atenddos'][indice]['id_servicio']; 
    nombre_cliente = session['servicios_atenddos'][indice]['cliente']; 
    sede_cliente = session['servicios_atenddos'][indice]['sede_cliente']; 
    encargado_sede = session['servicios_atenddos'][indice]['encargado_cliente']; 
    fecha_final = session['servicios_atenddos'][indice]['fecha_fin']; 
    empleado = session['servicios_atenddos'][indice]['empleado'];
    empresa_fumigadora = session['servicios_atenddos'][indice]['empresa_fumigadora'];  
    
    
    from app import mysql;
    
    cur = mysql.connection.cursor(); 
    
    cur.execute(" select detallesservicio.valorDetalle, detallesservicio.idCaracteristicaFk, clases.nombreClases, caracteristicas.nombreCaracteristicas, caracteristicas.idclasesFk from detallesservicio inner join caracteristicas on caracteristicas.idCaracteristicas = detallesservicio.idCaracteristicaFk inner join clases on clases.idClases = caracteristicas.idClasesFk where idServicioFk = %s order by detallesservicio.idCaracteristicaFk ASC", (id_servicio,))    
    detalles_servicios = cur.fetchall(); 
    cantidad_detalle = len(detalles_servicios); 

    
    if cantidad_detalle<1:
        return render_template('empresa_fumigadora/No_reporte.html', **context); 
    
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
    context2 ={
        'empresa_fumigadora' :empresa_fumigadora,
        'nit' : context['nit'],
        'telefono' : context['telefono'],
        'encargado_telefono' : context['encargado_telefono'],
        'direccion' : context['direccion'],
        'departamento' : context['departamento'],
        'correo' : context['correo'],
        'encargado_correo' : context['encargado_correo'],
        'nombre_cliente' : nombre_cliente,
        'empleado' : empleado
    }
    
    context3 ={
        'longitud1' : longitud1,
        'longitud2' : longitud2,
        'longitud3' : longitud3
    }
    
    return render_template('empresa_fumigadora/Reporte.html', **context2, **context3)

#Editar servicios completos
@Empresa_fumigadora.route('/actualizar_servicio/<int:index_servicio>')
def actualizar_servicio(index_servicio):
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    
    id_servicio = session['servicios_atenddos'][index_servicio]['id_servicio']; 
    cliente = session['servicios_atenddos'][index_servicio]['cliente']; 
    sede_cliente = session['servicios_atenddos'][index_servicio]['sede_cliente']; 
    fecha_solicitud = session['servicios_atenddos'][index_servicio]['fecha_solicitud']; 
    fecha_inicio = session['servicios_atenddos'][index_servicio]['fecha_inicio']; 
    fecha_fin = session['servicios_atenddos'][index_servicio]['fecha_fin']; 
    
    from app import mysql; 
    
    cur = mysql.connection.cursor(); 
    
    cur.execute("select idEmpleado, correoEmpresarialEmpleado from empleado where idEmpresaFumigadoraFk = %s", (context['id_cliente'],)); 
    consulta_empleados = cur.fetchall(); 
    print(consulta_empleados)
     
    if consulta_empleados:
        
        session['empleados'] = []
        for empleados in consulta_empleados:
            session['empleados'].append({
                'id_empleado':empleados[0],
                'nombre_empleado':empleados[1]
            })
        
    context2 = {
        'id_servicio'  : id_servicio,
        'cliente' : cliente,
        'sede_cliente' : sede_cliente ,
        'fecha_solicitud' : fecha_solicitud,
        'fecha_inicio' : fecha_inicio, 
        'fecha_fin' : fecha_fin
    }
    
    print(fecha_solicitud)
    return render_template('empresa_fumigadora/servicios/actualizar_servicios_final.html', **context, **context2)

@Empresa_fumigadora.route('/editar_servicio', methods=['POST'])
def editar_servicio():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    
    id_servicio = request.form['id']; 
    fecha_solicitud = request.form['fecha_solictud']; 
    fecha_inicio = request.form['fecha_inicio']; 
    fecha_final = request.form['fecha_fin']; 
    empleado = request.form['empleados']; 
    estado = request.form['estado']
    
    from app import mysql;
    
    cur = mysql.connection.cursor(); 
    
    cur.execute("select idEmpleado from empleado where correoEmpresarialEmpleado = %s;", (empleado,)); 
    consulta_empleado = cur.fetchone();
    id_empleado = consulta_empleado[0]
    
    cur.execute("update servicio set fechaSolicitudServicio=%s, fechaInicioServicio = %s, fechaFinalServicio = %s,  estadoServicio = %s , idEmpleadoFk = %s where idServicio = %s", (fecha_solicitud,fecha_inicio,fecha_final,estado, id_empleado, id_servicio,)); 
    cur.connection.commit(); 
    
    return render_template('empresa_fumigadora/servicios/mensajes/servicios_completado_actualizado.html', **context)

#Servicios incompletos
@Empresa_fumigadora.route('/servicios_incompletos')
def servicios_icompletos():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    
    from app import mysql;
    
    cur = mysql.connection.cursor(); 
    
    cur.execute("""select empresafumigadora.nombreEmpresaFumigadora,
	               cliente.nombreComercialCliente,
	               sedescliente.nombreSedeCliente,
                   servicio.descripcionServicio,
                   servicio.fechaSolicitudServicio,
                   servicio.fechaInicioServicio,
                   servicio.fechaFinalServicio,
                   servicio.estadoServicio,
                   empleado.nombresEmpleado,
                   servicio.idServicio
                   from servicio 
                   inner join sedescliente on servicio.idSedeClienteFk = sedescliente.idSedeCliente
                   inner join cliente on cliente.idCliente = sedescliente.idClienteFk
                   inner join empleado on empleado.idEmpleado = servicio.idEmpleadoFk
                   inner join empresafumigadora on empresafumigadora.idEmpresaFumigadora  = empleado.idEmpresaFumigadoraFk
                   where servicio.estadoServicio = 'en espera' and empresafumigadora.idEmpresaFumigadora=%s;
                   """, (context['id_cliente'],))
    servicios_incompletos = cur.fetchall(); 
    print(servicios_incompletos); 
    
    if servicios_incompletos:
        session['servicios_incompletos'] = []
        
        for servicios_no_Completos in servicios_incompletos:
            session['servicios_incompletos'].append({
                'empresa_fumigadora' : servicios_no_Completos[0],
                'cliente' : servicios_no_Completos[1],
                'sede_cliente' : servicios_no_Completos[2],
                'descripcion_servicio' : servicios_no_Completos[3],
                'fecha_solicitud' : servicios_no_Completos[4],
                'fecha_inicio' : servicios_no_Completos[5],
                'fecha_fin' : servicios_no_Completos[6],
                'estado_Servicio' : servicios_no_Completos[7],
                'empleado' : servicios_no_Completos[8],
                'id_servicio' : servicios_no_Completos[9]
            })
    
    else:
        return  render_template('empresa_fumigadora/servicios/mensaje_no_encontrado/servicios_incompletos.html', **context)

    print(session['servicios_atenddos']); 
    return render_template('empresa_fumigadora/servicios/servicios_incompletos.html', **context)

#Editar servicios incompletos
@Empresa_fumigadora.route('/actualizar_servicio_incompleto/<int:index_servicio_incompleto>')
def actualizar_servicio_incompleto(index_servicio_incompleto):
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    
    id_servicio = session['servicios_incompletos'][index_servicio_incompleto]['id_servicio']; 
    cliente = session['servicios_incompletos'][index_servicio_incompleto]['cliente']; 
    sede_cliente = session['servicios_incompletos'][index_servicio_incompleto]['sede_cliente']; 
    fecha_solicitud = session['servicios_incompletos'][index_servicio_incompleto]['fecha_solicitud']; 
    fecha_inicio = session['servicios_incompletos'][index_servicio_incompleto]['fecha_inicio']; 
    fecha_fin = session['servicios_incompletos'][index_servicio_incompleto]['fecha_fin']; 
    
    from app import mysql; 
    
    cur = mysql.connection.cursor(); 
    
    cur.execute("select idEmpleado, correoEmpresarialEmpleado from empleado where idEmpresaFumigadoraFk = %s", (context['id_cliente'],)); 
    consulta_empleados = cur.fetchall(); 
    print(consulta_empleados)
     
    if consulta_empleados:
        
        session['empleados'] = []
        for empleados in consulta_empleados:
            session['empleados'].append({
                'id_empleado':empleados[0],
                'nombre_empleado':empleados[1]
            })
        
    context2 = {
        'id_servicio'  : id_servicio,
        'cliente' : cliente,
        'sede_cliente' : sede_cliente ,
        'fecha_solicitud' : fecha_solicitud,
        'fecha_inicio' : fecha_inicio, 
        'fecha_fin' : fecha_fin
    }
    
    print(fecha_solicitud)
    return render_template('empresa_fumigadora/servicios/actualizar_servicios_incompletos.html', **context, **context2)

@Empresa_fumigadora.route('/editar_servicio_incompleto', methods=['POST'])
def editar_servicio_incompleto():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    
    id_servicio = request.form['id']; 
    fecha_solicitud = request.form['fecha_solictud']; 
    fecha_inicio = request.form['fecha_inicio']; 
    fecha_final = request.form['fecha_fin']; 
    empleado = request.form['empleados']; 
    estado = request.form['estado']
    
    from app import mysql;
    
    cur = mysql.connection.cursor(); 
    
    cur.execute("select idEmpleado from empleado where correoEmpresarialEmpleado = %s;", (empleado,)); 
    consulta_empleado = cur.fetchone();
    id_empleado = consulta_empleado[0]
    
    cur.execute("update servicio set fechaSolicitudServicio=%s, fechaInicioServicio = %s, fechaFinalServicio = %s,  estadoServicio = %s , idEmpleadoFk = %s where idServicio = %s", (fecha_solicitud,fecha_inicio,fecha_final,estado, id_empleado, id_servicio,)); 
    cur.connection.commit(); 
    
    return render_template('empresa_fumigadora/servicios/mensajes/servicios_completado_actualizado.html', **context)

#Servicios disponibles
@Empresa_fumigadora.route('/servicios_disponibles')
def servicios_disponibles():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    
    from app import mysql;
    
    cur = mysql.connection.cursor(); 
    
    cur.execute("""select servicio.idServicio,
	               cliente.nombreComercialCliente,
	               sedescliente.nombreSedeCliente,
                   servicio.descripcionServicio,
                   servicio.fechaSolicitudServicio
                   from servicio 
                   inner join sedescliente on servicio.idSedeClienteFk = sedescliente.idSedeCliente
                   inner join cliente on cliente.idCliente = sedescliente.idClienteFk
                   where servicio.idEmpleadoFk is null;
                   """)
    servicios_disponibles = cur.fetchall(); 
    print(servicios_disponibles); 
    
    if servicios_disponibles:
        session['servicios_disponibles'] = []
        
        for servicios_posibles in servicios_disponibles:
            session['servicios_disponibles'].append({
                'id_servicio' : servicios_posibles[0],
                'cliente' : servicios_posibles[1],
                'sede' : servicios_posibles[2],
                'descripcion_servicio' : servicios_posibles[3],
                'fecha_solicitud' : servicios_posibles[4]
            })
    
    else:
        return  render_template('empresa_fumigadora/servicios/mensaje_no_encontrado/servicios_disponibles.html', **context)

    # print(session['servicios_atenddos']); 
    return render_template('empresa_fumigadora/servicios/servicios_disponibles.html', **context)

@Empresa_fumigadora.route('/aceptar_servicio/<int:id_servicio_disponible>')
def aceptar_servicio(id_servicio_disponible):
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    
    id_servicio = session['servicios_disponibles'][id_servicio_disponible]['id_servicio']; 
    cliente = session['servicios_disponibles'][id_servicio_disponible]['cliente']; 
    sede = session['servicios_disponibles'][id_servicio_disponible]['sede']; 
    descripcion_servicio = session['servicios_disponibles'][id_servicio_disponible]['descripcion_servicio']; 
    fecha_solicitud = session['servicios_disponibles'][id_servicio_disponible]['fecha_solicitud']; 
    
    from app import mysql;
    
    cur = mysql.connection.cursor(); 
    
    cur.execute("select correoEmpresarialEmpleado from empleado where idEmpresaFumigadoraFk = %s;", (context['id_cliente'],)); 
    empleados = cur.fetchall(); 
    print(empleados); 
    
    session['empleados'] = []; 
    
    for empleado in empleados:
        session['empleados'].append({
            'correo_empresarial' : empleado[0]
        })
    
    print(session['empleados'])
    
    context2 = {
        'id_servicio':id_servicio,
        'cliente': cliente,
        'sede': sede,
        'descripcion_servicio' : descripcion_servicio,
        'fecha_solicitud' : fecha_solicitud
    }
    
    return render_template('empresa_fumigadora/servicios/aceptar_servicios.html', **context, **context2)

@Empresa_fumigadora.route('/actualizar_servicio_nuevo', methods=['POST'])
def actualizar_servicio_nuevo():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    
    id_servicio = request.form['id']; 
    fecha_inicio = request.form['fecha_inicio']; 
    fecha_fin = request.form['fecha_fin']; 
    empleados = request.form['empleados']; 
    estado = request.form['estado']; 
    prioridad = request.form['prioridad']; 
    infestacion = request.form['infestacion']; 
    
    
    from app import mysql;
    
    cur = mysql.connection.cursor(); 
    cur.execute("select idEmpleado from empleado where correoEmpresarialEmpleado = %s",(empleados,))
    id_empleado = cur.fetchone(); 
    indice_empleado = id_empleado[0]; 
    
    cur.execute("update servicio set fechaInicioServicio = %s, fechaFinalServicio = %s, nivelInfestacionDetallesServicio = %s, prioridadServicio = %s, estadoServicio = %s, idEmpleadoFk = %s where idServicio = %s" , (fecha_inicio, fecha_fin, infestacion, prioridad, estado, indice_empleado, id_servicio,)); 
    cur.connection.commit()
    
    
    return render_template('empresa_fumigadora/servicios/mensajes/servicios_completado_actualizado.html', **context)

#Encargado
@Empresa_fumigadora.route('/Encargado')
def datos_encargado():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    print(context['file_path_encargado'])
    return render_template('empresa_fumigadora/Encargado.html', **context)

#Detalles de servicios
@Empresa_fumigadora.route('/Consulta_detalles')
def consulta_detalles_servicios():
    from app import mysql
    
    cur = mysql.connection.cursor()
    
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    
    cur.execute('''select servicio.idServicio, 
                   empresafumigadora.nombreEmpresaFumigadora,
                   empresafumigadora.nombreEncargadoEmpresaFumigadora,
                   cliente.nombreComercialCliente,
                   sedescliente.nombreSedeCliente,
                   sedescliente.nombreEncargadoSedeCliente,
                   clases.nombreClases,
                   caracteristicas.nombreCaracteristicas,
                   detallesservicio.valorDetalle,
                   servicio.fechaFinalServicio,
                   detallesservicio.idDetalle from cliente 
                   inner join sedescliente on cliente.idCliente = sedescliente.idClienteFk 
                   inner join servicio on sedescliente.idSedeCliente = servicio.idSedeClienteFk 
                   inner join detallesservicio on  servicio.idServicio = detallesservicio.idServicioFk 
                   inner join caracteristicas on detallesservicio.idCaracteristicaFk = caracteristicas.idCaracteristicas 
                   inner join clases on caracteristicas.idClasesFk = clases.idClases 
                   inner join empleado on empleado.idEmpleado = servicio.idEmpleadoFk 
                   inner join empresafumigadora on empresafumigadora.idEmpresaFumigadora = empleado.idEmpresaFumigadoraFk 
                   where servicio.estadoServicio = 'finalizado' and empresafumigadora.idEmpresaFumigadora = %s order by servicio.idServicio asc''', (context['id_cliente'], ))
    consulta_detalles = cur.fetchall()
    print(consulta_detalles)
    cur.close()

    if consulta_detalles:
        session['detalles_servicios'] = []
    
        for consulta in consulta_detalles:
            session['detalles_servicios'].append({
                'id_servicio': consulta[0],
                'empresa_fumigadora': consulta[1],
                'encargado_empresa_fumigador': consulta[2],
                'nombre_cliente': consulta[3],
                'sede_cliente': consulta[4],
                'encargado_sede': consulta[5],
                'clase': consulta[6],
                'caracteristica': consulta[7],
                'detalle': consulta[8],
                'fecha_final': consulta[9],
                'id_detalle': consulta[10]
            })     
    else:
        return render_template('empresa_fumigadora/detalles_servicios/contenido_no_encontrado/detallles_servicios.html', **context)    
    return redirect(url_for('Empresa_fumigadora.detalles_servicios' ))

@Empresa_fumigadora.route('/Detalles_servicios')
def detalles_servicios():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'id_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'path_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'nit_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_inexistente'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'direccion_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'departamento_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'contraseña_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'descripcion_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'telefono_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'correo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'nombre_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'correo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'telefono_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'path_inexistente')
    }
    return render_template('empresa_fumigadora/Detalles_servicios.html', **context, )

#Eliminar detalle de servicio
@Empresa_fumigadora.route('/Eliminar_detalle/<int:index_detalle>')
def elimar_detalle(index_detalle):
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'id_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'path_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'nit_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_inexistente'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'direccion_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'departamento_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'contraseña_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'descripcion_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'telefono_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'correo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'nombre_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'correo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'telefono_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'path_inexistente')
    }
    
    id_detalle = session['detalles_servicios'][index_detalle]['id_detalle']; 
    
    print(id_detalle)
    
    from app import mysql; 
    cur = mysql.connection.cursor(); 
    
    cur.execute("""delete from detallesservicio 
                   where idDetalle = %s""", (id_detalle,)); 
    cur.connection.commit(); 
    
        
    return render_template('empresa_fumigadora/detalles_servicios/mensajes/detalle_eliminado.html', **context)

#Editar detalle de servicio
@Empresa_fumigadora.route('/Editar_detalle/<int:inex_detalle>')
def editar_detalle(inex_detalle):
    
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'id_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'path_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'nit_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_inexistente'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'direccion_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'departamento_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'contraseña_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'descripcion_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'telefono_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'correo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'nombre_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'correo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'telefono_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'path_inexistente')
    }
    
    from app import mysql; 
    cur = mysql.connection.cursor(); 
    
    id_servicio = session['detalles_servicios'][inex_detalle]['id_servicio']; 
    empresa_fumigadora = session['detalles_servicios'][inex_detalle]['empresa_fumigadora']; 
    encargado_empresa_fumigador = session['detalles_servicios'][inex_detalle]['encargado_empresa_fumigador']; 
    encargado_empresa_fumigador = session['detalles_servicios'][inex_detalle]['encargado_empresa_fumigador']; 
    nombre_cliente = session['detalles_servicios'][inex_detalle]['nombre_cliente']; 
    sede_cliente = session['detalles_servicios'][inex_detalle]['sede_cliente']; 
    encargado_sede = session['detalles_servicios'][inex_detalle]['encargado_sede']; 
    clase = session['detalles_servicios'][inex_detalle]['clase']; 
    caracteristica = session['detalles_servicios'][inex_detalle]['caracteristica']; 
    detalle = session['detalles_servicios'][inex_detalle]['detalle']; 
    id_detalle = session['detalles_servicios'][inex_detalle]['id_detalle']; 
    
    context2 = {
        'id_servicio' : id_servicio,
        'empresa_fumigadora' : empresa_fumigadora,
        'encargado_empresa_fumigador' : encargado_empresa_fumigador, 
        'encargado_empresa_fumigador' : encargado_empresa_fumigador,
        'nombre_cliente' : nombre_cliente,
        'sede_cliente' : sede_cliente,
        'encargado_sede' : encargado_sede,
        'clase' : clase,
        'caracteristica' : caracteristica,
        'detalle' : detalle,
        'id_detalle' : id_detalle
    }
    
    cur.execute("Select idClases, nombreClases, nombreClases as campo2  from clases"); 
    consulta1 = cur.fetchall(); 
    print(consulta1); 
    
    cur.execute("select caracteristicas.idCaracteristicas, caracteristicas.nombreCaracteristicas, caracteristicas.idClasesFk, clases.nombreClases from caracteristicas inner join clases on clases.idClases = caracteristicas.idClasesFk"); 
    consulta2 = cur.fetchall(); 
    print(consulta2); 
    
    if consulta1:
        session['clases'] = []
    
        for consultas1 in consulta1:
            session['clases'].append({
                'id_clase': consultas1[0],
                'nombre_clase': consultas1[1],
                'campo2': consultas1[2].replace(" ", "-")
            })     
    else:
        return redirect(url_for('Empresa_fumigadora.detalles_servicios'))
    
    if consulta2:
        session['caracteristicas'] = []
    
        for consultas2 in consulta2:
            session['caracteristicas'].append({
                'id_caracteristica': consultas2[0],
                'nombre_caracteristica': consultas2[1],
                'id_clase_fk': consultas2[2],
                'nombre_clase_fk': consultas2[3].replace(" ", "_")
                
            })     
    else:
        return redirect(url_for('Empresa_fumigadora.detalles_servicios'))
    
    
    
    return render_template('empresa_fumigadora/detalles_servicios/editar_detalle.html', **context, **context2)

@Empresa_fumigadora.route('/Actualizar_detalle', methods=['POST'])
def actualizar_detalle():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'id_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'path_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'nit_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_inexistente'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'direccion_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'departamento_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'contraseña_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'descripcion_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'telefono_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'correo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'nombre_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'correo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'telefono_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'path_inexistente')
    }
    
    clase =  request.form['clase']; 
    caracteristica = request.form['caracteristica']; 
    detalle = request.form['detalle_servicio']; 
    id_detalle = request.form['id']; 
    
    print(f'la caracteristica es {caracteristica} y la clase {clase}')
    
    from app import mysql;
    cur = mysql.connection.cursor(); 
    
    cur.execute("select idClases from clases where nombreClases = %s", (clase,)); 
    consulta1 = cur.fetchone(); 
    
    cur.execute("select idCaracteristicas from caracteristicas where nombreCaracteristicas = %s", (caracteristica,)); 
    consulta2 = cur.fetchone(); 
    id_caracteristica = consulta2[0]
    
    cur.execute("update detallesservicio set valorDetalle = %s, idCaracteristicaFk = %s where idDetalle = %s", (detalle, id_caracteristica, id_detalle,)); 
    cur.connection.commit(); 
    
    
    return render_template('empresa_fumigadora/detalles_servicios/mensajes/detalle_editado.html', **context)

#Empleados
@Empresa_fumigadora.route('/Consultar_empleados')
def consultar_empleados():
    from app import mysql
    cur = mysql.connection.cursor()
    
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    
    cur.execute("""select empleado.idEmpleado,
	               empleado.nombresEmpleado,
	               empleado.apellidosEmpleado,
                   empleado.correoPersonalEmpleado,
                   empleado.correoEmpresarialEmpleado,
                   count(servicio.idEmpleadoFk),
                   empleado.estadoEmpleado
                   from empleado 
                   left join servicio on empleado.idEmpleado = servicio.idEmpleadoFk
                   inner join empresaFumigadora on empresaFumigadora.idEmpresaFumigadora = empleado.idEmpresaFumigadoraFk
                   where estadoEmpleado = true and empresaFumigadora.idEmpresaFumigadora = %s
                   group by empleado.idEmpleado;
                """, (context['id_cliente'],)); 
    consulta_empleados = cur.fetchall(); 
    cur.close(); 
    
    if consulta_empleados:
        session['empleados_datos'] = []
    
        for consulta_empleado in consulta_empleados:
            session['empleados_datos'].append({
                'id_empleado': consulta_empleado[0],
                'nombre_empleado': consulta_empleado[1],
                'apellido_empleado': consulta_empleado[2],
                'correo_personal': consulta_empleado[3],
                'correo_empresarial': consulta_empleado[4],
                'servicios_atendidos': consulta_empleado[5],
                'estado_empleado' : consulta_empleado[6]
            })
            print(consulta_empleado[5])        
    else:
        return render_template('empresa_fumigadora/empleado/contenido_no_encontrado/empleados_activos.html', **context)
    
    
    return redirect(url_for('Empresa_fumigadora.emplados'))

@Empresa_fumigadora.route('/Empleados')
def emplados():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'id_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'path_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'nit_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_inexistente'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'direccion_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'departamento_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'contraseña_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'descripcion_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'telefono_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'correo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'nombre_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'correo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'telefono_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'path_inexistente')
    }
    return render_template('empresa_fumigadora/Empleados.html', **context)

#actualizar empleado
@Empresa_fumigadora.route('/Editar_empleados/<int:index_empleado_modificar>')
def editar_empleado(index_empleado_modificar):
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'id_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'path_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'nit_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_inexistente'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'direccion_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'departamento_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'contraseña_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'descripcion_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'telefono_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'correo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'nombre_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'correo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'telefono_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'path_inexistente')
    }
    datos_actualizar = {
        'id_empleado' : session['empleados_datos'][index_empleado_modificar]['id_empleado'],
        'nombre_empleado' : session['empleados_datos'][index_empleado_modificar]['nombre_empleado'],
        'apellido_empleado' : session['empleados_datos'][index_empleado_modificar]['apellido_empleado'],
        'correo_personal' : session['empleados_datos'][index_empleado_modificar]['correo_personal'],
        'correo_empresarial' : session['empleados_datos'][index_empleado_modificar]['correo_empresarial']
    }    
    
    print(datos_actualizar)
    
    # Almacenar en la sesión
    session['datos_actualizar'] = datos_actualizar
    
    return redirect(url_for('Empresa_fumigadora.form_actualizar', ))

@Empresa_fumigadora.route('/Actualizar_empleado')
def form_actualizar():
    
    datos_actualizar = session.get('datos_actualizar', {})
    context_2 = {
        'id_empleado' : datos_actualizar.get('id_empleado','dato_no_encontrado'),
        'nombre_empleado' : datos_actualizar.get('nombre_empleado','dato_no_encontrado'),
        'apellido_empleado' : datos_actualizar.get('apellido_empleado','dato_no_encontrado'),
        'correo_personal' : datos_actualizar.get('correo_personal','dato_no_encontrado'),
        'correo_empresarial' : datos_actualizar.get('correo_empresarial','dato_no_encontrado')
    }
    
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'id_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'path_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'nit_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_inexistente'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'direccion_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'departamento_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'contraseña_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'descripcion_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'telefono_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'correo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'nombre_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'correo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'telefono_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'path_inexistente')
    }
    return render_template('empresa_fumigadora/empleado/actualizar_empleado.html', **context, **context_2)

@Empresa_fumigadora.route('/Modificar_empleado', methods=['POST'])
def actualizar_empleado():
    
    #id del empleado
    datos_actualizar = session.get('datos_actualizar', {})
    id_empleado = datos_actualizar.get('id_empleado','dato_no_encontrado')
    
    #conexion
    from app import mysql; 
    cur = mysql.connection.cursor(); 
    
    #datos del formulario
    nombre_empelado = request.form['nombre_empleado']
    apellido_empleado = request.form['apellido_empleado']
    correo_personal = request.form['correo_personal']
    correo_empresarial = request.form['correo_empresarial']
    
    cur.execute("select *from empleado where correoEmpresarialEmpleado = %s", (correo_empresarial,)); 
    consulta1 = cur.fetchall(); 
    similitud1 = len(consulta1); 
    
    cur.execute("select *from empleado where correoPersonalEmpleado = %s", (correo_personal,));
    consulta2 = cur.fetchall(); 
    similitud2 = len(consulta2); 
    
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'id_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'path_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'nit_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_inexistente'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'direccion_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'departamento_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'contraseña_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'descripcion_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'telefono_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'correo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'nombre_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'correo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'telefono_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'path_inexistente')
    }
    
    if similitud1>0 or similitud2>0:
        flash("Correos existentes en la base de datos");
        return redirect(url_for('Empresa_fumigadora.form_actualizar')); 
    else:
        cur.execute("""update empleado set nombresEmpleado = %s,
                 apellidosEmpleado = %s,
                 correoEmpresarialEmpleado = %s,
                 correoPersonalEmpleado = %s
                 where idEmpleado = %s""" , (nombre_empelado, apellido_empleado, correo_empresarial, correo_personal, id_empleado))
        mysql.connection.commit()
        
    
        return render_template('empresa_fumigadora/empleado/mensajes/editar_empleados.html', **context)

#Inhabilitar empleado
@Empresa_fumigadora.route('/Eliminar_empleado/<int:index_empleado>')
def eliminar_empleado(index_empleado):

    from app import mysql;
    cur = mysql.connection.cursor(); 

    id_empleado = session['empleados_datos'][index_empleado]['id_empleado']
    estado_empleado = session['empleados_datos'][index_empleado]['estado_empleado']
    
    
    
    cur.execute("update empleado set estadoEmpleado = false where idEmpleado = %s", (id_empleado,)); 
    # Confirmar los cambios en la base de datos
    mysql.connection.commit()
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'id_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'path_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'nit_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_inexistente'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'direccion_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'departamento_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'contraseña_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'descripcion_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'telefono_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'correo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'nombre_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'correo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'telefono_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'path_inexistente')
    }
    return render_template('empresa_fumigadora/empleado/mensajes/inhabilitar_empleado.html', **context)

#Empleados inhabilitados
@Empresa_fumigadora.route('/Empleados_inhabilitados')
def consultar_empleados_inhabilitados():
    from app import mysql
    cur = mysql.connection.cursor()
    
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    
    cur.execute("""select empleado.idEmpleado,
	               empleado.nombresEmpleado,
	               empleado.apellidosEmpleado,
                   empleado.correoPersonalEmpleado,
                   empleado.correoEmpresarialEmpleado,
                   count(servicio.idEmpleadoFk),
                   empleado.estadoEmpleado
                   from empleado 
                   left join servicio on empleado.idEmpleado = servicio.idEmpleadoFk
                   inner join empresaFumigadora on empresaFumigadora.idEmpresaFumigadora = empleado.idEmpresaFumigadoraFk
                   where estadoEmpleado = false and empresaFumigadora.idEmpresaFumigadora = %s
                   group by empleado.idEmpleado;
                """, (context['id_cliente'],)); 
    consulta_empleados_inhabilitados = cur.fetchall(); 
    cur.close(); 
    
    if consulta_empleados_inhabilitados:
        session['empleados_inhabilitados_datos'] = []
    
        for inhbilitado_consulta_empleado in consulta_empleados_inhabilitados:
            session['empleados_inhabilitados_datos'].append({
                'id_empleado': inhbilitado_consulta_empleado[0],
                'nombre_empleado': inhbilitado_consulta_empleado[1],
                'apellido_empleado': inhbilitado_consulta_empleado[2],
                'correo_personal': inhbilitado_consulta_empleado[3],
                'correo_empresarial': inhbilitado_consulta_empleado[4],
                'servicios_atendidos': inhbilitado_consulta_empleado[5],
                'estado_empleado' : inhbilitado_consulta_empleado[6]
            })
            
    else:
        return render_template('empresa_fumigadora/empleado/contenido_no_encontrado/empleados_inactivos.html', **context); 
  
    return redirect(url_for('Empresa_fumigadora.emplados_inhabilitados'))

@Empresa_fumigadora.route('/Empleados_no_habilitados')
def emplados_inhabilitados():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'id_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'path_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'nit_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_inexistente'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'direccion_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'departamento_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'contraseña_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'descripcion_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'telefono_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'correo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'nombre_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'correo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'telefono_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'path_inexistente')
    }
    return render_template('empresa_fumigadora/empleado/Empleados_inhabilitados.html', **context); 

#Habilitar empleados
@Empresa_fumigadora.route('/Habilitar_epleado/<int:index_empleado_inhabilitado>')
def habilitar_empleado(index_empleado_inhabilitado):
    from app import mysql;
    cur = mysql.connection.cursor(); 

    id_empleado = session['empleados_inhabilitados_datos'][index_empleado_inhabilitado]['id_empleado']
    
    cur.execute("update empleado set estadoEmpleado = true where idEmpleado = %s", (id_empleado,)); 
    mysql.connection.commit()
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'id_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'path_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'nit_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_inexistente'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'direccion_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'departamento_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'contraseña_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'descripcion_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'telefono_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'correo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'nombre_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'correo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'telefono_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'path_inexistente')
    }
    return render_template('empresa_fumigadora/empleado/mensajes/habilitar_empleado.html', **context)

#Agregar_empleados
@Empresa_fumigadora.route('/Agregar_empleado')
def Agregar_empleado():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    return render_template('empresa_fumigadora/empleado/Agregar_empleados.html', **context)

@Empresa_fumigadora.route('/Insertar_empleado', methods=['POST'])
def Insertar_empleado():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    
    #conexion a bd
    from app import mysql; 
    cur = mysql.connection.cursor(); 
    
    #campos del formulario
    nombre = request.form['nombre_empleado']; 
    apellido = request.form['apellido_empleado']; 
    telefono = request.form['numero_telefonico']; 
    correo_personal = request.form['correo_personal']; 
    correo_empresarial = request.form['correo_empresarial']; 
    contraseña = request.form['contraseña']; 
    contraseña_cifrada = generate_password_hash(contraseña, 'pbkdf2:sha256:5', 5)
    
    
    #insercion del usuario
    cur.execute("select *from empleado where correoEmpresarialEmpleado = %s", (correo_empresarial,)); 
    consulta1 = cur.fetchall(); 
    similitud1 = len(consulta1); 
    
    cur.execute("select *from empleado where correoPersonalEmpleado = %s", (correo_personal,));
    consulta2 = cur.fetchall(); 
    similitud2 = len(consulta2); 
    
    
    if similitud1 > 0 or similitud2 > 0:
        flash("Empelado ya existente en el sitema"); 
        return redirect(url_for('Empresa_fumigadora.Agregar_empleado')); 
    else:
        cur.execute("""insert into empleado( nombresEmpleado, 
                       apellidosEmpleado, 
                       numeroTelefonicoEmpleado, 
                       correoEmpresarialEmpleado, 
                       correoPersonalEmpleado, 
                       contrasenaEmpleado, 
                       idEmpresaFumigadoraFk) value (%s, %s, %s, %s, %s, %s, %s)""",
                       (nombre, apellido, telefono, correo_empresarial, correo_personal, contraseña_cifrada, context['id_cliente']))
        mysql.connection.commit()
    return render_template('empresa_fumigadora/empleado/mensajes/agregar_empleado.html', **context)

#Licencias 
@Empresa_fumigadora.route('/Licencias')
def licencias():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    
    from app import mysql; 
    
    cur = mysql.connection.cursor(); 
    
    cur.execute("""select empresafumigadora.idEmpresaFumigadora, 
	                empresafumigadora.nombreEmpresaFumigadora,
                    rentaSoftware.idRentaSoftware,
                    rentaSoftware.estadoRentaSoftware,
                    rentaSoftware.duracionRenta,
                    pagosSoftware.idPagosSoftware,
                    licencias.nombreLicencia,
                    metodosPagoSoftware.nombreMetodoPagoSoftware
                    from empresafumigadora
                    inner join rentaSoftware on empresafumigadora.idEmpresaFumigadora = rentaSoftware.idEmpresaFumigadoraFk
                    inner join pagosSoftware on rentaSoftware.idRentaSoftware = pagosSoftware.idRentaSoftwareFk
                    inner join licencias on pagosSoftware.idLicenciaFk = licencias.idLicencia
                    inner join metodosPagoSoftware on pagosSoftware.idMediosPagoFk = metodosPagoSoftware.idMetodoPagoSoftware
                    where rentaSoftware.estadoRentaSoftware=1 and empresafumigadora.idEmpresaFumigadora = %s;""",(context['id_cliente'],))
    consulta_licencia = cur.fetchone(); 
    print(consulta_licencia)
    
    if consulta_licencia:
        context2 = {
            'id_empresa' : consulta_licencia[0],
            'empresa' : consulta_licencia[1], 
            'id_renta' :  consulta_licencia[2],
            'estado_renta' :  consulta_licencia[3],
            'duracion_renta' :  consulta_licencia[4],
            'id_pago' :  consulta_licencia[5],
            'licencia' :  consulta_licencia[6],
            'metodo' :  consulta_licencia[7],
            'id_licencia_html' : consulta_licencia[6].replace(' ', '-')
            
        }
        print(context2['id_licencia_html'])
        
        print(f"La fehca es: {context2['duracion_renta']}.El tipo de dato de esta fehca es:{type(context2['duracion_renta'])}")
        
        actual = datetime.now().date(); 
        print(f"La fehca es: {actual}.El tipo de dato de esta fehca es:{type(actual)}")
       
        if actual >= context2['duracion_renta']:
           print("Licencia caduco")
           return render_template('empresa_fumigadora/licencias/licencia_no.html', **context)

        
        return render_template('empresa_fumigadora/Licencias.html', **context, **context2)   
    else:
        return render_template('empresa_fumigadora/licencias/licencia_no.html', **context)

@Empresa_fumigadora.route('/adquirir_licencia')
def adquirir_licencia():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    
    from app import mysql;
    
    cur = mysql.connection.cursor(); 
    
    cur.execute("select *from licencias"); 
    consulta_licencias = cur.fetchall(); 
    print(consulta_licencias)
    
    session['licencias'] = []
    
    for licencia in consulta_licencias:
        session['licencias'].append({
            'id_licencia' : licencia[0],
            'nombre_licencia' : licencia[1],
            'descripción_licencia' : licencia[2],
            'duracion_licencia' : licencia[3]
        })
    
    return render_template('empresa_fumigadora/licencias/catalogo_licencias.html', **context); 

@Empresa_fumigadora.route('/comprar_licencia/<int:indice_licencia>')
def comprar_licencia(indice_licencia):
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    
    id_licencia = session['licencias'][indice_licencia]['id_licencia']
    nombre_licencia = session['licencias'][indice_licencia]['nombre_licencia']
    
    context2={
        'id_licencia': id_licencia,
        'nombre_licencia':nombre_licencia
    }
    print(id_licencia)
    
    return render_template('empresa_fumigadora/licencias/comprar_licencia.html', **context, **context2); 

@Empresa_fumigadora.route('/guardar_pago', methods=['POST'])
def guardar_pago():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }

    #obtener json
    detalles = request.get_json()
    
    #id
    id_paypal_pago = detalles['id']; 
    
    #total a pagar
    total = detalles['purchase_units'][0]['amount']['value']; 
    total_int = float(total)
    
    #subtotal
    subtotal = total_int - (total_int*0.19)
    
    #estado de pago
    estado = detalles['purchase_units'][0]['payments']['captures'][0]['status']; 
    if estado == 'COMPLETED':
        estado = True; 
        
    #licencia id
    licencia = detalles['id_liencia']
    licencia_int = int(licencia)
        
    #fecha
    fecha = detalles['purchase_units'][0]['payments']['captures'][0]['create_time'];
    
    fecha_lista = list(fecha); 
    
    caracteres_fecha = len(fecha_lista)
    while caracteres_fecha>10:
        fecha_lista.pop(); 
        caracteres_fecha -= 1; 
    
    
    fecha_string = ''.join(fecha_lista); 
    
    fecha_datetime = datetime.strptime(fecha_string, "%Y-%m-%d"); 
    
    if licencia == '1':
        actualizar_fecha = fecha_datetime + timedelta(days=180)
    elif licencia == '2':
        actualizar_fecha = fecha_datetime + timedelta(days=270)
    elif licencia == '3':
        actualizar_fecha = fecha_datetime + timedelta(days=365)
    
    #base de datos
    from app import mysql;
    
    cur= mysql.connection.cursor(); 
    
    #actualzar renta
    cur.execute("update rentaSoftware set estadoRentaSoftware = True, duracionRenta = %s where idEmpresaFumigadoraFk = %s", (actualizar_fecha,context['id_cliente'],)); 
    cur.connection.commit(); 
    
    #buscar renta
    cur.execute("select idRentaSoftware from rentaSoftware where idEmpresaFumigadoraFk = %s", (context['id_cliente'],))
    consulta_renta = cur.fetchone(); 
    
    #insertar pago
    cur.execute("insert into pagosSoftware(subTotalPagosSoftware, fechaPagosSoftware, totalPagosSoftware, idPaypalPago, verificacionPago, idRentaSoftwareFk, idLicenciaFk) value(%s,%s,%s,%s,%s,%s,%s)", (subtotal, fecha_datetime, total_int, id_paypal_pago, estado, consulta_renta[0], licencia_int,)); 
    cur.connection.commit()
    
    #dihk cjbs rxgl uhfm
    #servidor email
    asunto = "COMPRA DE LICENCIA"
    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login("sarmientodiazluisangel@gmail.com", "dihk cjbs rxgl uhfm")
    
    msg = MIMEText(f"Hola nuevamente {context['nombre_comercial']}, esperamos te encuentres bien, este correo confirma y asegura la compra exitosa de nuestra licencia." )
    msg["From"] = "sarmientodiazluisangel@gmail.com"; 
    msg["To"] = context['correo']
    msg["Subject"]  = asunto
    
    servidor.sendmail("sarmientodiazluisangel@gmail.com", context['correo'], msg.as_string())
    
    servidor.quit(); 
    
    
    return jsonify({"status": "success", "message": "Pago procesado correctamente"}), 200

@Empresa_fumigadora.route('/licencia_comprada')
def licencia_comprada():
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    return render_template('empresa_fumigadora/licencias/licencia_comprada.html', **context); 

#Eliminar cuenta
@Empresa_fumigadora.route('/elimimitar_cuenta')
def eliminar_cuenta (): 
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    
    return render_template('empresa_fumigadora/perfil/eliminar.html', **context)


@Empresa_fumigadora.route('/hacer_eliminar_cuenta')
def hacer_eliminar_cuenta (): 
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    
    from app import mysql;
    cur = mysql.connection.cursor(); 
    
    cur.execute("update empresafumigadora set estadoEmpresa = false where idEmpresaFumigadora = %s", (context['id_cliente'],))
    cur.connection.commit(); 
    
    return redirect(url_for('Login.cerrar_sesion')); 

#editar_cuenta
@Empresa_fumigadora.route('/editar_cuenta')
def editar_cuenta (): 
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    
    return render_template('empresa_fumigadora/perfil/editar.html', **context)

#actualizar cuenta
@Empresa_fumigadora.route('/actualizar_cuenta', methods=['POST'])
def actualizar_cuenta (): 
    context = {
        'id_cliente' : session.get('datos_cliente', {}).get('id_cliente', 'logo_inexistente'),
        'file_path' : session.get('datos_cliente', {}).get('file_path', 'logo_inexistente'),
        'nit' : session.get('datos_cliente', {}).get('nit', 'logo_inexistente'),
        'nombre_comercial' : session.get('datos_cliente', {}).get('nombre_comercial', 'nombre_no_encontrado'),
        'direccion' : session.get('datos_cliente', {}).get('direccion', 'logo_inexistente'),
        'departamento' : session.get('datos_cliente', {}).get('departamento', 'logo_inexistente'),
        'contraseña_cifrada' : session.get('datos_cliente', {}).get('contraseña_cifrada', 'logo_inexistente'),
        'descripcion' : session.get('datos_cliente', {}).get('descripcion', 'logo_inexistente'),
        'telefono' : session.get('datos_cliente', {}).get('telefono', 'logo_inexistente'),
        'correo' : session.get('datos_cliente', {}).get('correo', 'logo_inexistente'),
        'encargado_nombre' : session.get('datos_cliente', {}).get('encargado_nombre', 'logo_inexistente'),
        'encargado_correo' : session.get('datos_cliente', {}).get('encargado_correo', 'logo_inexistente'),
        'encargado_telefono' : session.get('datos_cliente', {}).get('encargado_telefono', 'logo_inexistente'),
        'file_path_encargado' : session.get('datos_cliente', {}).get('file_path_encargado', 'logo_inexistente')
    }
    
    direccion = request.form['Dirección']; 
    departamento = request.form['Departamento']; 
    descripcion = request.form['Descripción']; 
    
    from app import mysql; 
    
    cur = mysql.connection.cursor()
    
    cur.execute("update empresafumigadora set direccionEmpresaFumigadora  = %s, departamentoEmpresaFumigadora =%s, descripcionEmpresaFumigadora =%s where idEmpresaFumigadora = %s", (direccion, departamento, descripcion, context['id_cliente'],))
    cur.connection.commit(); 
    
    return render_template('empresa_fumigadora/perfil/datos_actualizados.html', **context)