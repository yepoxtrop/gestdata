from flask import render_template, redirect, url_for, session, make_response
from . import Documentos
from xhtml2pdf import pisa
import io

@Documentos.route('/plantilla')
def plantilla():
    return render_template('/pdfs/Plantilla.html')

@Documentos.route('/plantilla_descargar')
def plantilla_descargar():
    return render_template('/pdfs/Plantilla_descargar.html')

@Documentos.route('/plantilla_reporte')
def plantilla_reporte():
    return render_template('/empresa_fumigadora/Reporte.html')

@Documentos.route('/descargar_certificado/<string:nombre_cliente>/<string:sede_cliente>/<string:encargado_sede>/<string:encargado_empresa_fumigador>/<string:fecha_final>/<string:empresa_fumigadora>')
def descargar_certificado(nombre_cliente,sede_cliente,encargado_sede,encargado_empresa_fumigador,fecha_final,empresa_fumigadora):
    context2 = {
        'nombre_cliente' : nombre_cliente,
        'sede_cliente'  : sede_cliente,
        'encargado_sede'  : encargado_sede,
        'encargado_empresa_fumigador' : encargado_empresa_fumigador,
        'fecha_final' : fecha_final,
        'empresa_fumigadora' : empresa_fumigadora
    }
    
    #html del certificado
    html_certificado = render_template('/empresa_fumigadora/Certificados_descargar.html', **context2)
    
    # Crear el PDF
    pdf = io.BytesIO()
    pisa_status = pisa.CreatePDF(io.StringIO(html_certificado), dest=pdf)
    
    #excepción por error al generar PDF
    if pisa_status.err:
        return "Hubo un error al generar el PDF", 500
    
    # Configurar la respuesta para descargar el PDF
    pdf.seek(0)
    response = make_response(pdf.read())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=archivo.pdf'
    
    return response

@Documentos.route('/descargar_certificado2/<string:nombre_cliente>/<string:sede_cliente>/<string:encargado_sede>/<string:encargado_empresa_fumigador>/<string:fecha_final>/<string:empresa_fumigadora>')
def descargar_certificado2(nombre_cliente,sede_cliente,encargado_sede,encargado_empresa_fumigador,fecha_final,empresa_fumigadora):
    context2 = {
        'nombre_cliente' : nombre_cliente,
        'sede_cliente'  : sede_cliente,
        'encargado_sede'  : encargado_sede,
        'encargado_empresa_fumigador' : encargado_empresa_fumigador,
        'fecha_final' : fecha_final,
        'empresa_fumigadora' : empresa_fumigadora
    }
    
    #html del certificado
    html_certificado = render_template('/cliente/servicios/certificado_descargar.html', **context2)
    
    # Crear el PDF
    pdf = io.BytesIO()
    pisa_status = pisa.CreatePDF(io.StringIO(html_certificado), dest=pdf)
    
    #excepción por error al generar PDF
    if pisa_status.err:
        return "Hubo un error al generar el PDF", 500
    
    # Configurar la respuesta para descargar el PDF
    pdf.seek(0)
    response = make_response(pdf.read())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=archivo.pdf'
    
    return response