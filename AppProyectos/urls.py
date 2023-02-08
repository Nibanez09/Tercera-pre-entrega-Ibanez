from django.urls import path
from AppProyectos.views import *

urlpatterns = [
    path('inicio/', inicio, name="Start"),
    path('ver_contactos/', ver_contactos, name='Ver Contactos'),
    path('ver_proyectos/', ver_proyectos, name='Ver Proyectos'),
    path('ver_responsables/', ver_responsables, name='Ver Responsables'),
    path('agregar_contacto/', crear_contacto, name="Agregar contacto"),
    path('agregar_proyecto/', crear_proyecto, name="Agregar proyecto"),
    path('agregar_responsable/', crear_responsable, name="Agregar responsable"),
    path('buscarProyecto/', buscarProyecto),
]
