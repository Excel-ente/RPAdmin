from django.shortcuts import redirect, render
from .models import *
from django.db.models import Sum, Count,F, Case, When
from django.core.paginator import Paginator
import json
import requests
import pdfkit
from .BdLogs import MigrarLog
from datetime import date

def monitoreo(request):

    monitoreos = Monitoreo.objects.values('Proceso').annotate(
        gerencia=Count('Proceso'),
        total_error=Sum(Case(When(Tipo='Error', then=1), default=0, output_field=models.IntegerField())),
        total_fatal=Sum(Case(When(Tipo='Fatal', then=1), default=0, output_field=models.IntegerField())),
        total_warn=Sum(Case(When(Tipo='Warn', then=1), default=0, output_field=models.IntegerField())),
        total_finalizado=Sum(Case(When(Tipo='Proceso Finalizado', then=1), default=0, output_field=models.IntegerField()))
    )

    fecha_desde = request.GET.get('desde_fecha')
    fecha_hasta = request.GET.get('hasta_fecha')

    if fecha_desde and fecha_hasta:
        monitoreos = monitoreos.filter(Fecha__range=(fecha_desde, fecha_hasta))

    fecha_actual = date.today()

    # Obtener los datos filtrados por proceso y tipo de monitoreo
    datos_filtrados = []

    #ordenamiento
    monitoreos = monitoreos.order_by('-total_finalizado')

    for monitoreo in monitoreos:
        proceso = monitoreo['Proceso']
        total_warn = monitoreo['total_warn']
        total_finalizado = monitoreo['total_finalizado']
        total_error = monitoreo['total_error']
        total_fatal = monitoreo['total_fatal']
        datos_filtrados.append({
            'proceso': proceso,
            'total_warn': total_warn,
            'total_finalizado': total_finalizado,
            'total_error': total_error,
            'total_fatal': total_fatal
        })

    context = {
        'datos_filtrados': datos_filtrados,  # Agregar los datos filtrados al contexto
        'monitoreos': monitoreos,
        'procesos_disponibles': Monitoreo.objects.values_list('Proceso', flat=True).distinct(),
        'fecha_desde': fecha_desde,
        'fecha_hasta': fecha_hasta,
        'fecha_actual':fecha_actual,
    }

    return render(request, 'monitoreo.html', context)


def monitoreoGerencias(request):

    monitoreos = Monitoreo.objects.values('Gerencia').annotate(
        gerencia=Count('Gerencia'),
        total_error=Sum(Case(When(Tipo='Error', then=1), default=0, output_field=models.IntegerField())),
        total_fatal=Sum(Case(When(Tipo='Fatal', then=1), default=0, output_field=models.IntegerField())),
        total_warn=Sum(Case(When(Tipo='Warn', then=1), default=0, output_field=models.IntegerField())),
        total_finalizado=Sum(Case(When(Tipo='Proceso Finalizado', then=1), default=0, output_field=models.IntegerField()))
    )

    fecha_desde = request.GET.get('desde_fecha')
    fecha_hasta = request.GET.get('hasta_fecha')

    if fecha_desde and fecha_hasta:
        monitoreos = monitoreos.filter(Fecha__range=(fecha_desde, fecha_hasta))

    fecha_actual = date.today()

    # Obtener los datos filtrados por proceso y tipo de monitoreo
    datos_filtrados = []

    #ordenamiento
    monitoreos = monitoreos.order_by('-total_finalizado')

    for monitoreo in monitoreos:
        gerencia = monitoreo['gerencia']
        total_warn = monitoreo['total_warn']
        total_finalizado = monitoreo['total_finalizado']
        total_error = monitoreo['total_error']
        total_fatal = monitoreo['total_fatal']
        datos_filtrados.append({
            'gerencia': gerencia,
            'total_warn': total_warn,
            'total_finalizado': total_finalizado,
            'total_error': total_error,
            'total_fatal': total_fatal
        })

    context = {
        'datos_filtrados': datos_filtrados,  # Agregar los datos filtrados al contexto
        'monitoreos': monitoreos,
        'procesos_disponibles': Monitoreo.objects.values_list('Proceso', flat=True).distinct(),
        'fecha_desde': fecha_desde,
        'fecha_hasta': fecha_hasta,
        'fecha_actual':fecha_actual,
    }

    return render(request, 'monitoreo.html', context)


def servidor(request):

    servers = servidores.objects.all()

    Desarrollo = servidores.objects.all().filter(TIPO="Desarrollo").count()
    Produccion = servidores.objects.all().filter(TIPO="Produccion").count()
    PreProduccion = servidores.objects.all().filter(TIPO="Pre-Produccion").count()
    Test = servidores.objects.all().filter(TIPO="Test").count()

    SrvDesarrollo = servidores.objects.all().filter(TIPO="Desarrollo")
    SrvProduccion = servidores.objects.all().filter(TIPO="Produccion")
    SrvPreProduccion = servidores.objects.all().filter(TIPO="Pre-Produccion")
    SrvTest = servidores.objects.all().filter(TIPO="Test")

    context = {
        "servers": servers,

        "Desarrollo": Desarrollo,
        "PreProduccion": PreProduccion,
        "Produccion": Produccion,
        "Test": Test,

        "SrvDesarrollo": SrvDesarrollo,
        "SrvPreProduccion": SrvPreProduccion,
        "SrvProduccion": SrvProduccion,
        "SrvTest": SrvTest,

    }
    return render(request, 'servidores.html', context)


def procesos(request):

    robot = robots.objects.all()

    SrvsProduccion = servidores.objects.all().filter(TIPO="Produccion")

    NombresServersProductivos = []
    ClavesPX = []
    CantidadProcesosServer = []

    for Srv in SrvsProduccion:
        NombresServersProductivos.append(Srv.HOSTNAME)
        ClavesPX.append(Srv.pk)

    VarVar = robots.objects.all().filter().count()

    for X in ClavesPX:
        VarVar = robots.objects.all().filter(SERVIDOR=X).count()
        CantidadProcesosServer.append(VarVar)

    context = {

        "NombresServersProductivos": NombresServersProductivos,

        "CantidadProcesosServer": CantidadProcesosServer,

        "SrvsProduccion": SrvsProduccion,

        "robot": robot,

    }
    return render(request, 'procesos.html', context)


def ejecuciones(request):

    SrvsProduccion = servidores.objects.all().filter(TIPO="Produccion")

    EjecsPrd = ejecucionesProcesos.objects.all()

    NombresServersProductivos = []

    for Srv in SrvsProduccion:
        NombresServersProductivos.append(Srv.HOSTNAME)

    context = {

        "NombresServersProductivos": NombresServersProductivos,

        "SrvsProduccion": SrvsProduccion,

        "EjecsPrd": EjecsPrd,

    }
    return render(request, 'ejecuciones.html', context)


def dashboard(request):

    Robots = robots.objects.all()
    gerencias = Gerencia.objects.all()

    gerencias_labels = []
    gerencias_values = []
    grafico_data = []

    for gerencia in gerencias:

        robots_count = robots.objects.filter(GERENCIA=gerencia, ESTADO="Activo").count()

        if robots_count > 0:
            gerencias_labels.append(gerencia.GERENCIA)
            gerencias_values.append(robots_count)

    gerencias_data = list(zip(gerencias_labels, gerencias_values))
    gerencias_data = sorted(gerencias_data, key=lambda x: x[1], reverse=True)

    paginator = Paginator(gerencias_data, 10)
    page = request.GET.get('page')
    gerencias_data = paginator.get_page(page)



    for Rob in Robots:
        if Rob.ESTADO =="Activo":
            cantidad_ejecuciones = Rob.ejecucionesprocesos_set.all().aggregate(Sum('CANTIDAD_EJECUCIONES_MENSUALES',default=0))['CANTIDAD_EJECUCIONES_MENSUALES__sum']
            duracion_tarea = Rob.ejecucionesprocesos_set.all().aggregate(Sum('DURACION_TAREA_MINUTOS_MANUAL',default=0))['DURACION_TAREA_MINUTOS_MANUAL__sum']
            espacio_agenda = Rob.ejecucionesprocesos_set.all().aggregate(Sum('ESPACIO_AGENDA_MIN',default=0))['ESPACIO_AGENDA_MIN__sum']
            cantidad_ejecuciones_horas, cantidad_ejecuciones_minutos = divmod(cantidad_ejecuciones*espacio_agenda, 60)
            duracion_tarea_horas, duracion_tarea_minutos = divmod(cantidad_ejecuciones * duracion_tarea, 60)
            grafico_data.append({'nombre': Rob.NOMBRE, 'cantidad_ejecuciones': cantidad_ejecuciones_horas, 'duracion_tarea': duracion_tarea_horas})

    print(grafico_data)


    context = {
        'gerencias_labels': gerencias_labels,
        'gerencias_values': gerencias_values,
        "gerencias_data":gerencias_data,
        "grafico_data":grafico_data,

        }

    return render(request, 'dashboard.html', context)


def export_pdf(request):
    
    servers = servidores.objects.all()
    Robots = robots.objects.all()

    grafico_data = []
    server_data = []

    for server in servers:
        server_total = ejecucionesProcesos.objects.filter(SERVIDOR=server).aggregate(Sum('CONSUMO_TOTAL'))['CONSUMO_TOTAL__sum']
        if server_total:
            server_data.append({'name': server.HOSTNAME, 'usage': server_total })
    
    gerencias = Gerencia.objects.values('id','GERENCIA').annotate(horas_totales=Sum(F('robots__ejecucionesprocesos__CANTIDAD_EJECUCIONES_MENSUALES') * F('robots__ejecucionesprocesos__DURACION_TAREA_MINUTOS_MANUAL'), output_field=models.IntegerField()))

    BenefGerencia = [(x['GERENCIA'], x['horas_totales']) for x in gerencias]

    gerencias = [x[0] for x in BenefGerencia]
    horas_totales = [x[1] for x in BenefGerencia]

    gerencias2 = Gerencia.objects.values('GERENCIA').annotate(cantidad_robots=Count('robots'))
    gerencias_data = [(x['GERENCIA'], x['cantidad_robots']) for x in gerencias2]

    gerencias_labels = [x[0] for x in gerencias_data]
    gerencias_values = [x[1] for x in gerencias_data]

    gerencias_labels = json.dumps(gerencias_labels)
    gerencias_values = json.dumps(gerencias_values)

    for robot in Robots:
        cantidad_ejecuciones = robot.ejecucionesprocesos_set.all().aggregate(Sum('CANTIDAD_EJECUCIONES_MENSUALES',default=0))['CANTIDAD_EJECUCIONES_MENSUALES__sum']
        duracion_tarea = robot.ejecucionesprocesos_set.all().aggregate(Sum('DURACION_TAREA_MINUTOS_MANUAL',default=0))['DURACION_TAREA_MINUTOS_MANUAL__sum']
        espacio_agenda = robot.ejecucionesprocesos_set.all().aggregate(Sum('ESPACIO_AGENDA_MIN',default=0))['ESPACIO_AGENDA_MIN__sum']
        cantidad_ejecuciones_horas, cantidad_ejecuciones_minutos = divmod(cantidad_ejecuciones*espacio_agenda, 60)
        duracion_tarea_horas, duracion_tarea_minutos = divmod(cantidad_ejecuciones * duracion_tarea, 60)
        grafico_data.append({'nombre': robot.NOMBRE, 'cantidad_ejecuciones': cantidad_ejecuciones_horas, 'duracion_tarea': duracion_tarea_horas})

    gerencias2 = Gerencia.objects.values('GERENCIA').annotate(cantidad_robots=Count('robots'))
    gerencias_data = [(x['GERENCIA'], x['cantidad_robots']) for x in gerencias2]
    
    gerencias_select = Gerencia.objects.values('GERENCIA').annotate(cantidad_robots=Count('robots'))

    context = {
        'server_data': server_data,
        'BenefGerencia': BenefGerencia,
        'gerencias':gerencias,
        'horas_totales':horas_totales,
        'gerencias_labels':gerencias_labels,
        'gerencias_values':gerencias_values,
        'grafico_data': grafico_data,
        'gerencias_data': gerencias_data,
        'gerencias_select': gerencias_select,
        }

    return render(request, 'dashboard.html', context)

