from django.http import HttpResponse
from datetime import datetime
from family.models import Familiar
from django.template import Context, Template, loader

def crear_familiar(request, nombre, apellido, edad):
    
    familiar = Familiar(nombre=nombre, apellido=apellido, edad=edad, fecha=datetime.now())
    familiar.save()
    template = loader.get_template('crear_familiar.html')
    template_renderizado = template.render({'familiar': familiar})
    
    return HttpResponse(template_renderizado)

def ver_familiares(request):
    
    familiares = Familiar.objects.all()
    
    template = loader.get_template('ver_familiares.html')
    template_renderizado = template.render({'familiares': familiares})
    
    return HttpResponse(template_renderizado)