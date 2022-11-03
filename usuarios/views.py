from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as acceso

def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            acceso(request, usuario)
            
            return redirect('index')
            
    else:
        formulario = AuthenticationForm()
        
    return render(request, 'usuarios/login.html', {'formulario': formulario})


# Create your views here.
