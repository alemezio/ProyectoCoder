from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio,name="Inicio"),
    path('cursos/', views.cursos,name="Cursos"),
    path('profesores/', views.profesores,name="Profesores"),
    path('estudiantes/', views.estudiantes,name="Estudiantes"),
    path('entregables/', views.entregables,name="Entregables"),
    path('buscar/', views.buscar,name="Buscar"),
]
