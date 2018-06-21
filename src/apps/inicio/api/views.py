import os
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from apps.inicio.models import Persona
from django.contrib.auth.models import User
from .serializers import PersonaSerializer
from .pagination import PersonaLimitOffsetPagination, PersonaPageNumberPagination

class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    name = 'persona-list'
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    pagination_class = PersonaPageNumberPagination
    
    def perform_create(self, serializer):
        serializer.save()

class PersonaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    name = 'persona-detail'
    lookup_field = 'pk'
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        return Response({
            'personas': reverse(PersonaList.name, request=request),
        })