from django.urls import path
from .views import home, ListarUsuarios, GestionarUsuario

urlpatterns = [
    path('home/', home , name='home'),
    path('usuarios/listar', ListarUsuarios , name='listar_usuarios'),
    path('usuarios/agregar', GestionarUsuario , name='agregar_usuario'),
    path('usuarios/editar/<int:id>/', GestionarUsuario , name='editar_usuario'),
]