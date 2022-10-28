from datetime import datetime
from family.models import Familiar
from django.shortcuts import render, redirect
from family.forms import FamiliarFormulario, BusquedaFamiliarFormulario
from django.views.generic.edit import UpdateView, DeleteView

def crear_familiar(request):
    
    if request.method == 'POST':
        
        formulario = FamiliarFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
        
            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            fecha_creacion = data.get('fecha_creacion', datetime.now()) 
            
            familiar = Familiar(nombre=nombre, apellido=apellido, edad=edad, fecha=datetime.now())
            familiar.save()
            
            return redirect('ver_familiares')
        
        else: 
             return render(request, 'family/crear_familiar.html', {'formulario' : formulario} )
        
    formulario = FamiliarFormulario()
   
    return render(request, 'family/crear_familiar.html', {'formulario' : formulario} )

def ver_familiares(request):
        
    nombre = request.GET.get('nombre', None)
    
    if nombre:
        familiares = Familiar.objects.filter(nombre__icontains=nombre)
    else:
        familiares = Familiar.objects.all()

    formulario = BusquedaFamiliarFormulario()
    return render(request, 'family/ver_familiares.html', {'familiares':familiares, 'formulario':formulario})

def index(request):
    return render(request, 'family/index.html')

class EditarFamiliar(UpdateView):
    model = Familiar
    success_url = '/'
    template_name = 'family/editar_familiar_cbv.html'
    fields = ['nombre', 'apellido', 'edad', 'fecha']
    
class EliminarFamiliar(DeleteView):
    model = Familiar
    success_url = '/'
    template_name = 'family/eliminar_familiar_cbv.html'
      

