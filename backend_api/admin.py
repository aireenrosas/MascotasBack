from django.contrib import admin
from .models import Mascota
# Register your models here.

class MascotaAdmin(admin.ModelAdmin):
    list = ('name', 'raza', 'descripcion')

    admin.site.register(Mascota)
