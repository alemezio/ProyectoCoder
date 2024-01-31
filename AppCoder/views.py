from django.shortcuts import render
from django.http import HttpResponse
# import datetime
# from django.template import Template,Context
# from django.template import loader


# Create your views here.

def inicio(request):
    return render(request, 'AppCoder/index.html')


def cursos(request):
    return render(request, 'AppCoder/cursos.html')


def profesores(request):
    return render(request, 'AppCoder/profesores.html')


def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')


def entregables(request):
    return render(request, 'AppCoder/entregables.html')
