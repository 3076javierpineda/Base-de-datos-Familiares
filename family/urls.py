from django.urls import path
from family import views

urlpatterns = [
    path('', views.index),
    path('ver-familiares/', views.ver_familiares),
    path('crear-familiar/<str:nombre>/<str:apellido>/<int:edad>/', views.crear_familiar)
]