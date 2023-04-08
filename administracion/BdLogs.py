from django.contrib import admin
from .models import Monitoreo
import os 
import glob
@admin.action(description="Importar LOG")
def MigrarLog(modeladmin, request, queryset):

    arrayDatos = [[],[],[],[],[],[],[],[],[]]
    
    MENSAJE = ""

    dir_path = '//xfs/UC/RPA/LOGS/Upload_Scanner'

    pattern = '*.log'

    # Buscar todos los archivos .log en el directorio
    for file_path in glob.glob(f'{dir_path}/{pattern}'):
        try:

            with open(file_path, 'r') as file:
                # Leer el contenido del archivo y agregarlo a la lista
                lines = file.readlines()

                for line in lines:

                    TIPO = line.split()[1]

                    DURACION = line.find("totalExecutionTimeInSeconds")

                    if DURACION > 0:

                        posicion = line.find("totalExecutionTimeInSeconds",0) + len("totalExecutionTimeInSeconds_:")
                        final = line.find(",",posicion) 
                        DURACION = float(line[posicion:final])
                            
                    else:

                        DURACION = 0
                        
                    posicion = line.find("timeStamp",0) + len("timeStamp_:_") 
                    FECHA = line[posicion:posicion + 10]

                    posicion = line.find("timeStamp",0) + len("timeStamp_:_YYYY-MM-DDT")
                    HORA = line[posicion:posicion + 14]

                    posicion = line.find("processName",0) + len("processName_:_")
                    final = line.find(",",posicion) - 1
                    PROCESO = line[posicion:final ]

                    posicion = line.find("message",0) + len("message_:_")
                    final = line.find(",",posicion) - 1
                    MENSAJE = line[posicion:final ]

                    posicion = line.find("machineName",0) + len("machineName_:_")
                    final = line.find(",",posicion) - 1
                    SERVER = line[posicion:final ]

                    posicion = line.find("processVersion",0) + len("processVersion_:_")
                    final = line.find(",",posicion) - 1
                    PAQUETE = line[posicion:final ]
                
                    posicion = line.find("fingerprint",0) + len("fingerprint_:_")
                    final = line.find(",",posicion) - 1

                    CLAVE = line[posicion:final ]

                    if DURACION > 0:
                        try:
                            p = Monitoreo.objects.create(Tipo="Proceso Finalizado",Fecha=FECHA,HoraEjecucion=HORA,Proceso=PROCESO,Mensaje=MENSAJE,Duracion=DURACION/60,Server=SERVER,Paquete=PAQUETE,clave=CLAVE)
                        except:
                            pass
                    elif TIPO == "Warn":
                        try:
                            p = Monitoreo.objects.create(Tipo=TIPO,Fecha=FECHA,HoraEjecucion=HORA,Proceso=PROCESO,Mensaje=MENSAJE,Duracion=DURACION,Server=SERVER,Paquete=PAQUETE,clave=CLAVE)
                        except:
                                pass
                    elif TIPO == "Fatal":
                        try:
                            p = Monitoreo.objects.create(Tipo=TIPO,Fecha=FECHA,HoraEjecucion=HORA,Proceso=PROCESO,Mensaje=MENSAJE,Duracion=DURACION,Server=SERVER,Paquete=PAQUETE,clave=CLAVE)
                        except:
                                pass
                    elif TIPO == "Error":
                        try:
                            p = Monitoreo.objects.create(Tipo=TIPO,Fecha=FECHA,HoraEjecucion=HORA,Proceso=PROCESO,Mensaje=MENSAJE,Duracion=DURACION,Server=SERVER,Paquete=PAQUETE,clave=CLAVE)
                        except:
                            pass
                    else:
                        try:
                            verifInicio= PROCESO + ' execution started'
                            if MENSAJE == verifInicio:
                                p = Monitoreo.objects.create(Tipo="Inicio Ejecucion",Fecha=FECHA,HoraEjecucion=HORA,Proceso=PROCESO,Mensaje=MENSAJE,Duracion=DURACION,Server=SERVER,Paquete=PAQUETE,clave=CLAVE)
                        except:
                            pass

        except:
            MENSAJE = "Un error en el archivo: " + file_path
            print(MENSAJE)



