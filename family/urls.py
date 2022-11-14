from django.urls import path
from family import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ver-familiares/', views.ver_familiares, name='ver_familiares'),
    path('crear-familiar/', views.crear_familiar, name='crear_familiar'),
    path('editar-familiar/<int:pk>', views.EditarFamiliar.as_view(), name='editar_familiar'),
    path('eliminar-familiar/<int:pk>', views.EliminarFamiliar.as_view(), name='eliminar_familiar'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path('video/', views.video, name='video')
]