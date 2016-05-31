from django.contrib import admin
from .models import DatosEmpresa, FotoEmpresa

# Register your models here.

class DatosEmpresaAdmin(admin.ModelAdmin):
    list_display = ['quienesSomos']


class FotoEmpresaAdmin(admin.ModelAdmin):
    list_display = ('titulo_foto', 'estado')


admin.site.register(DatosEmpresa)
admin.site.register(FotoEmpresa, FotoEmpresaAdmin)