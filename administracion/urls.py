from django.urls import path
from django.contrib import admin
from administracion.views import *
from django.views.generic import RedirectView

from django.contrib.auth.views import LoginView, LogoutView

from django_pdfkit import PDFView

urlpatterns = [
    
    path('', dashboard, name='dashboard'),
    path('monitoreo/', monitoreo, name='monitoreo'),
    path('monitoreo/gerencias/', monitoreo, name='monitoreoGerencias'),
    path('admin/', admin.site.urls, name='admin'),
    path('servidores/', servidor, name='servidores'),
    path('procesos/', procesos, name='procesos'),
    path('ejecuciones/', ejecuciones , name='ejecuciones'),
    path('export/',export_pdf,name='export'),
    path('login/',login_view,name='login'),
    
]