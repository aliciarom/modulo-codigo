# -*- coding: utf-8 -*-

######################################################################################################################################################
#  @version     : 1.0                                                                                                                                #
#  @autor       : SUPERMAS                                                                                                                       #
#  @creación    : 2015-05-21                                                                                                                         #
#  @linea       : Maximo 150 chars                                                                                                                   #
######################################################################################################################################################

#OpenERP Imports
from osv import fields, osv
from datetime import datetime, date


#Modulo ::
class listado_codigo(osv.osv):
  #--------------------------------------------------------Variables Privadas y Publicas--------------------------------------------------------------
  ### //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// ###
  ###                                                                                                                                              ###
  ###                                                                 METODOS                                                                      ###
  ###                                                                                                                                              ###
  ### //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// ###


  ### //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// ###
  ###                                                                                                                                              ###
  ###                                                  Atributos basicos de un modelo OPENERP                                                      ###
  ###                                                                                                                                              ###
  ### //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// ###
  
  #Nombre del modelo
  _name = 'listado_codigo'
  #Nombre de la tabla
  _table = 'listado_codigo'
 
  _columns = {
    'codigo_barras' : fields.integer("Codigo de Barras", required=False),    
    'descripcion':fields.char("Descripción", required=False),
    'precio':fields.float('precio', required=False),
    'codigos_m2o_id': fields.many2one('codigo', 'codigoo')
    # 'fecha':fields.date("fecha", required=False),

  }
    
  #Valores por defecto de los campos del diccionario [_columns]
  _defaults = {
  }

#se cierra la clase
listado_codigo() 


