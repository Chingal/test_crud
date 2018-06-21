# -*- coding: utf-8 -*-
from django.urls import reverse
import os

def MenuPrincipal(request):
    menu = {
        'menu_principal': [
            {'name': 'Inicio', 'url': reverse('home'), 'icon': 'dashboardd',},
            {'name': 'Usuarios', 'url': reverse('listar_usuarios'), 'icon': 'person',},
        ]
    }
    active = False
    for obj in menu['menu_principal']:
        if request.path == obj['url']:
            obj['active'] = True        
    return menu