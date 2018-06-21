# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .constants import Activo, STATUS_TYPE

class Persona(models.Model):
    def generate_upload_path(instance, filename):
        return '/'.join(['upload', instance.correo, filename])
        
    # Atributos propios de la Persona
    nombre = models.CharField(_('Nombres'), max_length=80)
    apellido = models.CharField(_('Apellidos'), max_length=80)
    correo = models.EmailField(_('Correo Electrónico'), max_length=150, unique=True)
    estado = models.CharField(_('Estado'), max_length=10, choices=STATUS_TYPE, default=Activo)
    foto = models.ImageField(upload_to=generate_upload_path, blank=True)
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_modificacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

class Usuario(Persona):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
