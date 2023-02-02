from django.shortcuts import render

from .models import Mascota
from .serializers import MascotaSerializer
from rest_framework import viewsets

# Create your views here.
class MascotaViewSet(viewsets.ModelViewSet):
    serializer_class = MascotaSerializer
    queryset = Mascota.objects.all()
