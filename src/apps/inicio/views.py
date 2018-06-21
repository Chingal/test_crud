from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Persona, Usuario
from .forms import PersonaForm

# Metodo que redirige a la pagina principal
def home(request):
    if request.user.is_authenticated:
        obj = Usuario.objects.get(user=request.user)
        personas = Persona.objects.all()
    return render(request, 'inicio/index.html', locals())


# Metodo que lista los usuarios
@login_required
def ListarUsuarios(request):
    if request.user.is_authenticated:
        try:
            nombre_vista = "Listar Usuarios"
            obj = Usuario.objects.get(user=request.user)
            personas = Persona.objects.all().order_by('-id')
        except Persona.DoesNotExist:
            personas = None        
    return render(request, 'inicio/usuarios/listar.html', locals())

@login_required
def GestionarUsuario(request, id=None):
    obj = Usuario.objects.get(user=request.user)        
    if id:
        nombre_vista = "EDITAR USUARIO"
        persona = Persona.objects.get(id=id)
        form = PersonaForm(request.POST or None, instance=persona)
    else:
        nombre_vista = "AGREGAR USUARIO"
        form = PersonaForm(request.POST or None, request.FILES or None)
    return render(request, 'inicio/usuarios/gestionar.html', locals())