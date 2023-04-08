from django.contrib import admin
from administracion.models import Monitoreo,robots

@admin.action(description="Actualizar Gerencias")
def Actualizar(modeladmin,request,queryset):

    Monitoreos = Monitoreo.objects.all()

    Robots = robots.objects.all()
    
    for monitoreo in Monitoreos:

        for robot in Robots:

            if str(monitoreo.Proceso) == str(robot.NOMBRE):
                
                monitoreo.Gerencia = robot.GERENCIA.GERENCIA

                monitoreo.save()

@admin.action(description="Actualizar Robots")
def ActualizarRobots2(modeladmin,request,queryset):

    Robots = robots.objects.all()

    Monitoreos = Monitoreo.objects.all()
    
    for robot in Robots:

        robot.EJECUCIONES = 0
        robot.FATAL = 0
        robot.ERRORES = 0

        robot.save()

        for monitoreo in Monitoreos:

            if str(robot.NOMBRE) == str(monitoreo.Proceso):
                
                if monitoreo.Tipo == "Proceso Finalizado":
                    robot.EJECUCIONES += 1
                    robot.save()
                elif monitoreo.Tipo == "Fatal":
                    robot.FATAL += 1
                    robot.save()
                elif monitoreo.Tipo == "Error":
                    robot.ERRORES  += 1
                    robot.save()
                else:
                    pass

@admin.action(description="Actualizar Robots")
def ActualizarRobots(modeladmin,request,queryset):

    Robots = robots.objects.all()

    for robot in Robots:

        robot.ESTADO=="Inactivo"

        if robot.EJECUCIONES > 0 :
            robot.ESTADO=="Inactivo"
            robot.save()
        else:
            robot.ESTADO=="Activo"
            robot.save()

        