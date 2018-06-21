from django.urls import path
from .views import ApiRoot, PersonaList, PersonaDetail

urlpatterns = [
    path('personas/', PersonaList.as_view(), name=PersonaList.name),
    path('personas/<int:pk>/', PersonaDetail.as_view(), name=PersonaDetail.name),
    path('', ApiRoot.as_view(), name=ApiRoot.name),
]