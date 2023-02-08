from django.shortcuts import render
from AppProyectos.models import *
from AppProyectos.forms import *

# Create your views here.

def inicio(request):
    return render(request, 'AppProyectos/inicio.html')

def ver_contactos(request):

    return render(request, 'AppProyectos/verContactos.html')

def ver_proyectos(request):
    return render(request, 'AppProyectos/verProyectos.html')

def ver_responsables(request):
    return render(request, 'AppProyectos/verResponsables.html')

def crear_contacto(request): 

    if request.method == 'POST':

        FormularioContacto = ContactoForm(request.POST)

        if FormularioContacto.is_valid():

            infoDic = FormularioContacto.cleaned_data

            contacto1 = Contacto(nombre=infoDic["nombre"], apellido = infoDic["apellido"], empresa = infoDic["empresa"], profesion = infoDic["profesion"], email = infoDic["email"])

            contacto1.save()

            return render(request, "AppProyectos/inicio.html")

    else:
        FormularioContacto = ContactoForm()


    return render(request, "AppProyectos/crearContacto.html", {"FormularioContacto":FormularioContacto})

def crear_proyecto(request): 

    if request.method == 'POST':

        FormularioProyecto = ProyectoForm(request.POST)

        if FormularioProyecto.is_valid():

            infoDic = FormularioProyecto.cleaned_data

            proyecto1 = Proyecto(codigo=infoDic["codigo"], fecha_recibido = infoDic["fecha_recibido"], plazo = infoDic["plazo"], categoria = infoDic["categoria"])

            proyecto1.save()

            return render(request, "AppProyectos/inicio.html")

    else:
        FormularioProyecto = ProyectoForm()


    return render(request, "AppProyectos/crearProyecto.html", {"FormularioProyecto":FormularioProyecto})

def crear_responsable(request): 

    if request.method == 'POST':

        FormularioResponsable = ResponsableForm(request.POST)

        if FormularioResponsable.is_valid():

            infoDic = FormularioResponsable.cleaned_data

            responsable1 = Responsable(nombre=infoDic["nombre"], apellido = infoDic["apellido"])

            responsable1.save()

            return render(request, "AppProyectos/inicio.html")

    else:
        FormularioResponsable = ResponsableForm()


    return render(request, "AppProyectos/crearResponsable.html", {"FormularioResponsable":FormularioResponsable})



def buscarProyecto(request):
    return render(request, 'AppProyectos/buscarProyecto.html')

def resultados(request):
    categoriaBusqueda = request.GET['categoria']
    resultadosProyectos = Proyecto.objects.filter(categoria_icontains=categoriaBusqueda)
    return render(request, 'AppProyectos/resultados.html', {'d1':categoriaBusqueda, 'd2':resultadosProyectos})

