from django.http import HttpResponse
from datetime import datetime
from family.models import Familiar
from django.template import Context, Template, loader
from django.shortcuts import render

def crear_familiar(request):
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        edad = request.POST.get('edad')
        familiar = Familiar(nombre=nombre, apellido=apellido, edad=edad, fecha=datetime.now())
        familiar.save()
   
    return render(request, 'family/crear_familiar.html', {})

def ver_familiares(request):
    
    familiares = Familiar.objects.all()

    return render(request, 'family/ver_familiares.html', {'familiares':familiares})

def index(request):
    return render(request, 'family/index.html')