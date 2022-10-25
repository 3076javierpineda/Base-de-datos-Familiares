from django.urls import path
from family import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ver-familiares/', views.ver_familiares, name='ver_familiares'),
    path('crear-familiar/', views.crear_familiar, name='crear_familiar'),
     path('editar-familiar/<int:id>', views.editar_familiar, name='editar_familiar')
]