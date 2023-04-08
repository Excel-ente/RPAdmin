from django.contrib import admin
from .models import *
# Register your models here.

from import_export.admin import ImportExportModelAdmin

from .BdLogs import MigrarLog
from .Imporador import *


@admin.register(Path)
class clasePath(ImportExportModelAdmin):
    list_display=('servidor','path',)


@admin.register(servidores)
class claseServidores(ImportExportModelAdmin):
    list_display=('HOSTNAME','TIPO','SISTEMA_OPERATIVO','PROCESADOR','MEMORIA_RAM','ARQUITECTURA','DOMINIO',)
    ordering=('TIPO',)
    search_fields= ('HOSTNAME',)
    list_per_page = 20
    list_display_links=('HOSTNAME',)

@admin.register(robots)
class claseRobots(ImportExportModelAdmin):

    list_display=('NOMBRE','ESTADO','EJECUCIONES','ERRORES','FATAL','SERVIDOR','USUARIO','GERENCIA','PROVEEDOR',)
    ordering=('NOMBRE',)
    search_fields= ('NOMBRE',)
    list_per_page = 50
    list_filter=('SERVIDOR','ESTADO',)
    list_display_links=('NOMBRE',)
    exclude =('ULTIMA_ACTUALIZACION','EJECUCIONES','ERRORES',)
    actions=[ActualizarRobots,]

@admin.register(Gerencia)
class claseRobots(ImportExportModelAdmin):
    list_display=('GERENCIA',)

@admin.register(Usuario)
class claseRobots(ImportExportModelAdmin):
    list_display=('NOMBRE_APELLIDO','GERENCIA','MAIL','TELEFONO','COMENTARIOS',)

@admin.register(Proveedor)
class claseRobots(ImportExportModelAdmin):
    list_display=('NOMBRE_APELLIDO','EMPRESA','CARGO','MAIL','TELEFONO','COMENTARIOS',)

@admin.register(ejecucionesProcesos)
class claseEjecuciones(admin.ModelAdmin):

    list_display=('ROBOT','HORA_INICIO_EJECUCION','HORA_FIN_CALCULADA','SERVIDOR','TIPO_EJECUCION','ESPACIO_AGENDA_MIN','CONSUMO_TOTAL','DURACION_MENSUAL','CANTIDAD_EJECUCIONES_MENSUALES','FTE','COMENTARIOS',)
    ordering=('CONSUMO_TOTAL',)
    list_filter=('SERVIDOR',)
    exclude=('FTE','CONSUMO_TOTAL','EJECUCIONES_ACUMULADO','SERVIDOR','CANTIDAD_EJECUCIONES_MENSUALES','LISTA','HORA_FIN_CALCULADA',)
    list_per_page = 100

@admin.register(incidencias)
class clasePs(admin.ModelAdmin):
    list_display=('NOMBRE_INDICENCIA','N_INCIDENTE','FECHA_SOLICITUD','ESTADO','ASIGNADO_A','COMENTARIOS',)
    ordering=('-ULTIMA_ACTUALIZACION',)
    search_fields= ('NOMBRE_INDICENCIA',)
    list_filter=('ESTADO',)
    list_per_page = 20
    list_editable=('ESTADO',)
    list_display_links=('NOMBRE_INDICENCIA',)
    exclude=('N_INCIDENTE',)

@admin.register(Monitoreo)
class claseMonitoreoDb(ImportExportModelAdmin):
    list_display=('Fecha','Server','HoraEjecucion','Tipo','Proceso','Gerencia','Mensaje','Duracion','Paquete',)
    exclude=('clave','Fecha','HoraEjecucion','Tipo','Proceso','Mensaje','Server','Paquete',)
    ordering=('-Fecha','-HoraEjecucion',)
    search_fields= ('Proceso','Mensaje','Server',)
    list_filter=('Tipo','Proceso','Gerencia','Server',)
    list_per_page = 500
    list_display_links=('Proceso',)
    actions=[MigrarLog,Actualizar]




   
