from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio),
    path('cursos/', views.cursos),
    path('profesores/', views.profesores),
    path('cursestudiantesos/', views.estudiantes),
    path('entregables/', views.entregables),
]
