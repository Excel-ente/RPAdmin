from django.db import models
from .listas import *
from datetime import datetime, timedelta

#>>>> MODELO GERENCIAS
class Gerencia(models.Model):
    GERENCIA=models.CharField(max_length=50,null=False,blank=False)
    PROCESOS_ACTIVOS=models.IntegerField(blank=True,null=True)
    HORAS_BENEFICIO=models.DecimalField(max_digits=8,decimal_places=2,blank=True,null=True)
    class Meta:
        verbose_name = 'Gerencia'
        verbose_name_plural ='Gerencias'

    def __str__(self): #ESTE METODO REESCRIBE EL "TITULO" DE LA TABLA
        return self.GERENCIA
#>>>> FIN USUARIOS

#>>>> MODELO USUARIOS
class Usuario(models.Model):
    NOMBRE_APELLIDO=models.CharField(max_length=120,null=False,blank=False) 
    GERENCIA=models.ForeignKey(Gerencia,on_delete=models.PROTECT,null=True,blank=True)
    MAIL=models.EmailField(blank=True,null=True)
    TELEFONO= models.CharField(max_length=20,null=True,blank=True)
    COMENTARIOS=models.TextField(null=True,blank=True)
 
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural ='Usuarios'

    def __str__(self): #ESTE METODO REESCRIBE EL "TITULO" DE LA TABLA
        return self.NOMBRE_APELLIDO
#>>>> FIN USUARIOS

#>>>> MODELO PROVEEDORES
class Proveedor(models.Model):
    NOMBRE_APELLIDO=models.CharField(max_length=120,null=False,blank=False) 
    EMPRESA=models.CharField(max_length=60,null=True,blank=True)
    CARGO=models.CharField(max_length=50,null=True,blank=True)
    MAIL=models.EmailField(blank=True,null=True)
    TELEFONO= models.CharField(max_length=20,null=True,blank=True)
    COMENTARIOS=models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural ='Proveedores'

    def __str__(self): #ESTE METODO REESCRIBE EL "TITULO" DE LA TABLA
        return self.NOMBRE_APELLIDO 
#>>>> FIN PROVEEDORES

#>>>> MODELO SERVIDORES (BASE DE DATOS DE LOS SERVIDORES)
class servidores(models.Model):

    HOSTNAME=models.CharField(max_length=20,unique=True,null=False,blank=False) 
    IP=models.CharField(max_length=20,null=True,blank=True)
    TIPO= models.CharField(max_length=20,choices=TIPO_SERVER,default=1,null=False,blank=False)
    SISTEMA_OPERATIVO= models.CharField(max_length=20,choices=CHOICES_SO,default=1,null=False,blank=False)
    PROCESADOR=models.CharField(max_length=200,null=True,blank=True)
    MEMORIA_RAM=models.CharField(max_length=20,null=True,blank=True)
    ARQUITECTURA=models.CharField(max_length=20,null=True,blank=True)
    NOMBRE_COMPLETO=models.CharField(max_length=50,null=True,blank=True)
    DOMINIO=models.CharField(max_length=50,null=True,blank=True)
    COMENTARIOS=models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = 'Servidor'
        verbose_name_plural ='Servidores'

    def __str__(self): #ESTE METODO REESCRIBE EL "TITULO" DE LA TABLA
        return self.HOSTNAME

#>>>> MODELO ROBOTS (BASE DE DATOS DE LOS ROBOTS)
class robots(models.Model):
    NOMBRE=models.CharField(unique=True,max_length=120,null=False,blank=False)
    SERVIDOR=models.ForeignKey(servidores,default=1,on_delete=models.PROTECT)
    FECHA_PUESTA_PRD=models.DateField(null=True,blank=True)
    GERENCIA=models.ForeignKey(Gerencia,on_delete=models.PROTECT,blank=False,null=False)
    USUARIO=models.ForeignKey(Usuario,on_delete=models.PROTECT,blank=False,null=False)
    PROVEEDOR=models.ForeignKey(Proveedor,verbose_name="DESARROLLADOR",on_delete=models.PROTECT,blank=True,null=True)
    ATENDIDO=models.CharField(max_length=11,choices=ATENDIDO_DESATENDIDO,default="ATENDIDO",null=False,blank=False)
    ESTADO=models.CharField(max_length=20,default="Inactivo",choices=ESTADO,null=False,blank=False)
    ULTIMO_PAQUETE=models.CharField(max_length=20,null=True,blank=True)
    ULTIMA_ACTUALIZACION=models.DateField(null=True,blank=True)
    RUTAS_REPOSITORIO=models.CharField(max_length=255,null=False,blank=False)
    RUTAS_INPUT=models.CharField(max_length=255,null=True,blank=True)
    RUTAS_OUTPUT=models.CharField(max_length=255,null=True,blank=True)
    DESCRIPCION_BREVE=models.TextField(null=True,blank=True)
    COMENTARIOS=models.TextField(null=True,blank=True)
    EJECUCIONES=models.IntegerField(null=True,blank=True)
    ERRORES=models.IntegerField(null=True,blank=True)
    FATAL=models.IntegerField(null=True,blank=True)
    
    class Meta:
        verbose_name = 'Robot'
        verbose_name_plural ='Robots'

    def __str__(self): #ESTE METODO REESCRIBE EL "TITULO" DE LA TABLA
        return self.NOMBRE

#>>>> MODELO EJECUCIONES (BASE DE DATOS DE LAS EJECUCIONES DE LOS ROBOTS)
class ejecucionesProcesos(models.Model):
    SERVIDOR=models.ForeignKey(servidores,on_delete=models.PROTECT,null=False,blank=True)
    ROBOT=models.ForeignKey(robots,on_delete=models.PROTECT,null=False,blank=False)
    TIPO_EJECUCION=models.CharField(max_length=20,choices=PERIODICIDAD,default="Diario",null=False,blank=False)

    DOM=models.BooleanField(default=False)
    LUN=models.BooleanField(default=False)
    MAR=models.BooleanField(default=False)
    MIE=models.BooleanField(default=False)
    JUE=models.BooleanField(default=False)
    VIE=models.BooleanField(default=False)
    SAB=models.BooleanField(default=False)

    CANTIDAD_EJECUCIONES_MENSUALES = models.IntegerField(null=True,blank=True,default=0)
    ESPACIO_AGENDA_MIN=models.IntegerField(verbose_name="MINUTOS RESERVADOS EN AGENDA",null=True,blank=True,default=15)
    EJECUCIONES_ACUMULADO=models.BigIntegerField(verbose_name="ACUM. EJECUCIONES (30 dias)",null=True,blank=True)
    DURACION_TAREA_MINUTOS_MANUAL=models.IntegerField(verbose_name="DURACION DE LA TAREA (manualmente) Min.",null=True,blank=False)
    DURACION_MENSUAL=models.IntegerField(verbose_name="HS LABORABLES MENSUALES",null=True,blank=False)
    TIPO_ESFUERZO=models.CharField(max_length=10,choices=TIPO_ESFUERZO,default="Medio",null=False,blank=False)
    FTE=models.DecimalField(verbose_name="FTE",max_digits=10,decimal_places=2,null=True,blank=True,default=0)
    CONSUMO_TOTAL =models.DecimalField(max_digits=5,verbose_name="TOTAL HORAS AGENDA (mensual)",decimal_places=2,null=True,blank=True,default=0)
    COMENTARIOS=models.TextField(null=True,blank=True)
    FECHA_INICIO =  models.DateField(null=True,blank=True)
    HORA_INICIO_EJECUCION = models.TimeField(null=True,blank=True)
    HORA_FIN_CALCULADA = models.TimeField(null=True,blank=True)
    LISTA=models.TextField(null=True,blank=True)


    class Meta:
        verbose_name = 'Ejecucion'
        verbose_name_plural ='Ejecuciones'

    def __str__(self): #ESTE METODO REESCRIBE EL "TITULO" DE LA TABLA
        texto = str(self.ROBOT)
        return texto
                                    
    def save(self, *args, **kwargs): #ESTE METODO REESCRIBE EL "GUARDADO" DE LA TABLA.(podemos disparar func. desde este método)
        
        hora_inicio = self.HORA_INICIO_EJECUCION
        minutos = self.ESPACIO_AGENDA_MIN
        hora_fin = datetime.now().replace(hour=hora_inicio.hour, minute=hora_inicio.minute) + timedelta(minutes=minutos)
        self.HORA_FIN_CALCULADA = hora_fin


        self.SERVIDOR = self.ROBOT.SERVIDOR
        
        cant = 0

        if self.TIPO_EJECUCION =="Diario":

            if self.DOM==True:
                cant += 1

            if self.LUN==True:
                cant += 1

            if self.MAR==True:
                cant += 1

            if self.MIE==True:
                cant += 1

            if self.JUE==True:
                cant += 1

            if self.VIE==True:
                cant += 1

            if self.SAB==True:
                cant += 1

        if self.TIPO_EJECUCION=="Diario":   
            self.CANTIDAD_EJECUCIONES_MENSUALES =  cant * 4 + 2
        elif self.TIPO_EJECUCION=="Quincenal":
            self.CANTIDAD_EJECUCIONES_MENSUALES = 2
        elif self.TIPO_EJECUCION=="Mensual":
            self.CANTIDAD_EJECUCIONES_MENSUALES = 1
        else:
            self.CANTIDAD_EJECUCIONES_MENSUALES = 0
        
        CONSUM = self.CANTIDAD_EJECUCIONES_MENSUALES * self.ESPACIO_AGENDA_MIN

        if CONSUM > 0:
            self.CONSUMO_TOTAL = CONSUM / 60


        lista = []

        if self.DOM == True:
            lista.append("DOM")
        
        if self.LUN == True:
            lista.append("LUN")

        if self.MAR == True:
            lista.append("MAR")

        if self.MIE == True:
            lista.append("MIE")

        if self.JUE == True:
            lista.append("JUE")

        if self.VIE == True:
            lista.append("VIE")

        if self.SAB == True:
            lista.append("SAB")

        self.LISTA = lista

        super(ejecucionesProcesos, self).save(*args, **kwargs)

#>>>> MODELO INCIDENTES (BASE DE DATOS DE LOS INCIDENTES)
class incidencias(models.Model):
    N_INCIDENTE=models.CharField(max_length=255,blank=True,null=True)
    ROBOT=models.ForeignKey(robots,on_delete=models.PROTECT,null=False,blank=False)
    NOMBRE_INDICENCIA=models.CharField(max_length=100,null=True,blank=True)
    FECHA_SOLICITUD=models.DateField()
    ASIGNADO_A=models.ForeignKey(Usuario,on_delete=models.PROTECT,blank=True,null=True)
    ESTADO=models.CharField(max_length=30,choices=ESTADO_INCIDENCIAS,default="Recibido",null=True,blank=True)
    DESCRIPCION_INCIDENCIA=models.CharField(max_length=255,null=True,blank=True)
    DESCRIPCION_SOLUCION=models.CharField(max_length=255,null=True,blank=True)
    ULTIMA_ACTUALIZACION=models.DateField(auto_now_add=True)
    COMENTARIOS=models.TextField(null=True,blank=True)
    
    class Meta:
        verbose_name = 'Incidente'
        verbose_name_plural ='Incidentes'

    def save(self, *args, **kwargs):

        self.N_INCIDENTE =  'INC-' + str(self.pk)

        super(incidencias, self).save(*args, **kwargs)

#>>>> MODELO MONITOREO (BASE DE DATOS DE LOS LOGS DE LOS ROBOTS)
class Monitoreo(models.Model):
    Tipo=models.TextField(null=True,blank=True)
    Fecha=models.DateField(null=True,blank=True)
    HoraEjecucion=models.TextField(null=True,blank=True)
    Proceso=models.TextField(null=True,blank=True)
    Gerencia=models.TextField(null=True,blank=True)
    Mensaje=models.TextField(null=True,blank=True)
    Duracion=models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True,verbose_name="Duracion Minutos")
    Server=models.TextField(null=True,blank=True)
    Paquete=models.TextField(null=True,blank=True)
    Comentarios=models.CharField(max_length=120,null=True,blank=True)
    clave=models.TextField(unique=True,null=True,blank=True)

    class Meta:
        verbose_name = 'Monitoreo'
        verbose_name_plural ='Monitoreos'

                                    
    def save(self, *args, **kwargs): 
        
        Robots = robots.objects.all()
        
        for proceso in Robots:
            if str(proceso.NOMBRE) == str(self.Proceso):
                self.Gerencia = proceso.GERENCIA.GERENCIA

        super(Monitoreo, self).save(*args, **kwargs)


#>>>> MODELO MONITOREO (BASE DE DATOS DE LOS LOGS DE LOS ROBOTS)
class Path(models.Model):
    servidor=models.ForeignKey(servidores,on_delete=models.PROTECT,null=True,blank=True)
    path=models.TextField(null=False,blank=False)

    class Meta:
        verbose_name = 'Path'
        verbose_name_plural ='Path'

    def __str__(self):
        return self.path