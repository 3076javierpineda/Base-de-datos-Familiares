from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as acceso
from usuarios.forms import MiFormularioDeCreacion, EditarPerfilFormulario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from usuarios.models import ExtensionUsuario





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


def registrar(request):
    if request.method == 'POST':
        formulario = MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    else:
        formulario = MiFormularioDeCreacion()
    
    return render(request, 'usuarios/registrar.html', {'formulario': formulario})

@login_required
def perfil(request):
    extensionUsuario, es_nuevo = ExtensionUsuario.objects.get_or_create(user=request.user)
    return render(request, 'usuarios/perfil.html', {})
 
@login_required
def editar_perfil(request):
    
    user = request.user
    
    user.extensionusuario

    
    if request.method == 'POST':
       
        if request.method == 'POST':
            formulario = EditarPerfilFormulario(request.POST, request.FILES)
            
            if formulario.is_valid():
                data_nueva = formulario.cleaned_data
                user.first_name = data_nueva['first_name']
                user.last_name = data_nueva['last_name']
                user.email = data_nueva['email']
                user.extensionusuario.avatar = data_nueva['avatar']
                
                user.extensionusuario.save()
                user.save()
                return redirect('perfil')

    else:
        formulario = EditarPerfilFormulario(
            initial={
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,
                'avatar': user.extensionusuario.avatar,
            }
        )
        
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})

class CambiarContrasenia(PasswordChangeView):
    template_name = 'usuarios/cambiar_contrasenia.html'
    success_url = '/usuarios/perfil/'


    



