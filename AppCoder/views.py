from django.shortcuts import render
from django.http import HttpResponse
from AppCoder import models
from AppCoder.forms import CursoFormulario,BuscarCamada,ProfesFormulario,BuscarProfe
from AppCoder.forms import EstudFormulario,BuscarEstud,EntregFormulario,BuscarEntreg
# import datetime
# from django.template import Template,Context
# from django.template import loader

# Create your views here.

def inicio(request):
    return render(request, 'AppCoder/index.html')


def profesores(request):
    if request.method == 'POST':
        miFormulario=ProfesFormulario(request.POST)
        # print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor = models.Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion["profesion"])
            profesor.save()
            return render(request, "AppCoder/gracias_ingreso.html",{"campo_ingresado":"Profesor"})
    else:
        miFormulario = ProfesFormulario()
        buscar_apellido=BuscarProfe()
    return render(request, "AppCoder/formulario_generico.html", {"mi_form": miFormulario,"busqueda":buscar_apellido,"registro":"Profesores","clave":"Apellido"})


def cursos(request):
    if request.method == 'POST':
        miFormulario=CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = models.Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "AppCoder/gracias_ingreso.html",{"campo_ingresado":"Curso y Camada"})
    else:
        miFormulario = CursoFormulario()
        buscar_camada=BuscarCamada()
    return render(request, "AppCoder/formulario_generico.html", {"mi_form": miFormulario,"busqueda":buscar_camada,"registro":"Cursos","clave":"Camada"})


def estudiantes(request):
    if request.method == 'POST':
        miFormulario=EstudFormulario(request.POST)
        # print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            estudiante = models.Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
            estudiante.save()
            return render(request, "AppCoder/gracias_ingreso.html",{"campo_ingresado":"Estudiante"})
    else:
        miFormulario = EstudFormulario()
        buscar_apellido=BuscarEstud()
    return render(request, "AppCoder/formulario_generico.html", {"mi_form": miFormulario,"busqueda":buscar_apellido,"registro":"Estudiantes","clave":"Apellido"})


def entregables(request):
    if request.method == 'POST':
        miFormulario=EntregFormulario(request.POST)
        # print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            entregable = models.Entregable(nombre=informacion["nombre"], fecha_entrega=informacion["fecha_entrega"],entregado=informacion["entregado"])
            entregable.save()
            return render(request, "AppCoder/gracias_ingreso.html",{"campo_ingresado":"Entregable"})
    else:
        miFormulario = EntregFormulario()
        buscar_entregable=BuscarEntreg()
    return render(request, "AppCoder/formulario_generico.html", {"mi_form": miFormulario,"busqueda":buscar_entregable,"registro":"Entregables","clave":"Nombre"})

def buscar(request):
    # respuesta = f'Estoy buscando la camada nro {request.GET["camada"]}'
    if 'camada' in request.GET:
        camada = request.GET['camada']
        cursos = models.Curso.objects.filter(camada__icontains=camada)
        return render(request,'AppCoder/resultados_cursos.html',{'cursos':cursos,'camada':camada})
    elif 'apellido_profe' in request.GET:
        p_apellido = request.GET['apellido_profe']
        profes = models.Profesor.objects.filter(apellido__icontains=p_apellido)
        return render(request,'AppCoder/resultados_profesores.html',{'profes':profes,'apellido':p_apellido})
    elif 'apellido_estud' in request.GET:
        e_apellido = request.GET['apellido_estud']
        estudiantes = models.Estudiante.objects.filter(apellido__icontains=e_apellido)
        return render(request,'AppCoder/resultados_estudiantes.html',{'estudiantes':estudiantes,'apellido':e_apellido})
    elif 'nombre_e' in request.GET:
        e_nombre = request.GET['nombre_e']
        entregables = models.Entregable.objects.filter(nombre__icontains=e_nombre)
        return render(request,'AppCoder/resultados_entregables.html',{'entregables':entregables,'nombre':e_nombre})
    else:
        respuesta ='No enviaste datos.'
        return HttpResponse(respuesta)

