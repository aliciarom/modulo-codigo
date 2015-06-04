# -*- coding: utf-8 -*-

import time
from openerp.report import report_sxw
from openerp.osv import osv
from openerp import pooler

class sm_etiquetas(report_sxw.rml_parse):
  #variable que define al reporte
  _name = "sm_etiquetas"
  _description = "Etiquetas"

  #######################################################################################################################
  #                                Metodos Privados (Independientes al API de OpenERP)                                  #
  ####################################################################################################################### 
  #----------------------------------------------------------------------------------------------------------------------
  def __init__( self, cr, uid, name, context = None ) :
    """
    Método "__init__" para instanciar objetos a partir de esta clase y pasar de formato rml a pdf
    * Argumentos OpenERP: [cr, uid, ids, name, context]	
    """
    if context is None:
      context = {}
    super( sm_etiquetas, self ).__init__( cr, uid, name, context = context )
    self.localcontext.update({
      'time': time,
      'get_datos_etiquetas': self.get_datos_etiquetas,
    })
    self.context = context
  #----------------------------------------------------------------------------------------------------------------------
  def get_datos_etiquetas( self ):
    self.cr.execute(
      """
      SELECT cod_barras AS ean13, 
      descripcion AS nombre, 
      precio AS precio,
      ruta_codigo AS ruta,
      fecha AS fecha,
      precio_str AS precio_s,
      fecha_str AS fecha_muestra
      FROM listado_codigo 
      """
    )
    etiqueta = self.cr.dictfetchall()
    return etiqueta

#########################################################################################################################
#------------------------------------------------------------------------------------------------------------------------
#Nombre del reporte, nombre del modelo,ruta del rml, parser con el nombre de la clase y header el encabezado del reporte
#para emplear el template rml definido
imprimir = report_sxw.report_sxw('report.sm_etiquetas',
                      'listado_codigo',
                      'addons/codigos/report/sm_etiquetas.rml',
                      parser = sm_etiquetas,
                      header=False
                      )

