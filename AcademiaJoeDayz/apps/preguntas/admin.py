from django.contrib import admin
from .models import PreguntaRespuesta

# Register your models here.
class PreguntaRespuestaAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'respuesta')


admin.site.register(PreguntaRespuesta, PreguntaRespuestaAdmin)