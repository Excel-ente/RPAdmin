# LISTAS A UTILIZAR EN MODELOS

# -- CHOICES TIPO DE SERVIDOR  --
TIPO_SERVER = [
    ("Desarrollo","Desarrollo"),
    ("Test","Test"),
    ("Pre-Produccion","Pre-Produccion"),
    ("Produccion","Produccion"),
]

 # -- VARIABLES CHOICES OPERATIVOS
CHOICES_SO = [  # -- LISTA CHOICES OPERATIVOS
    ("Windows","Windows"),
    ("Linux","Linux"),
    ("Mac","Mac"),
]
# -------------

# -- VARIABLES CHOICES ESTADO --
ESTADO = [ # -- LISTA CHOICES OPERATIVOS
    ("Activo","Activo"),
    ("Inactivo","Inactivo"),
]
# -------------




















# -- CHOICES ESTADO INCIDENCIAS  --
ESTADO_INCIDENCIAS = [
    ("Recibido","Recibido"),
    ("En Proceso","En Proceso"),
    ("Finalizado","Finalizado"),
]
# -------------

# -------------

# -- CHOICES SI/NO --

YES_NO = [
    ("SI","SI"),
    ("NO","NO"),
]
# -------------
# -- CHOICES TIPO EJECUCION  --
at="at"
de="de"
TIPO_EJECUCION = [
    (at,"Atendido"),
    (de,"Desatendido"),
]
# -------------
# -- CHOICES PERIODICIDAD  --

PERIODICIDAD = [
    ("Diario","Diario"),
    ("Quincenal","Quincenal"),
    ("Mensual","Mensual"),
    ("Bimestral","Bimestral"),
    ("Trimestral","Trimestral"),
    ("Semestral","Semestral"),
    ("Anual","Anual"),
]
# -------------
# -- CHOICES TIPO ESFUERZO  --

TIPO_ESFUERZO = [
    ("Bajo","Bajo"),
    ("Medio","Medio"),
    ("Alto","Alto"),
]
# ------------

# -------------
DIAS = [
    ("Lunes","Lunes"),
    ("Martes","Martes"),
    ("Miercoles","Miercoles"),
    ("Jueves","Jueves"),
    ("Viernes","Viernes"),
    ("Sabado","Sabado"),
    ("Domingo","Domingo"),
]

ATENDIDO_DESATENDIDO = [
    ("Atendido","Atendido"),
    ("Desatendido","Desatendido"),
]

