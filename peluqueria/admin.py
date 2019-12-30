from django.contrib import admin
from .models import *

class ServiciosAdmin(admin.ModelAdmin):
	list_display = ('nombre',)

class BarberoAdmin(admin.ModelAdmin):
	list_display = ('nombre','apellido','cedula','telefono')
	

admin.site.register(Servicios,ServiciosAdmin)
admin.site.register(ImgCarrucel)
admin.site.register(diseñoGeneral)
admin.site.register(Barbero)
