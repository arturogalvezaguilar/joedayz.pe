from django.contrib import admin
from .models import Multimedia, Portada

# Register your models here.
class MultimediaAdmin(admin.ModelAdmin):
    list_display = ('titulo_video', 'fecha_video')

class PortadaAdmin(admin.ModelAdmin):
	list_display = ('titulo_foto', 'descripcion_foto')

admin.site.register(Multimedia, MultimediaAdmin)
admin.site.register(Portada, PortadaAdmin)