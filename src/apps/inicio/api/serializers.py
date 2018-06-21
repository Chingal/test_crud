from rest_framework import serializers
from django.contrib.auth.models import User
from apps.inicio.models import Persona

class PersonaSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Persona
        fields = ('url', 'nombre', 'apellido', 'correo', 'estado', 'foto', )