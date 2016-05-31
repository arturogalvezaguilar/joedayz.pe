from _csv import list_dialects
from django.contrib import admin
from .models import Curso, DatosCurso, DetallesCurso, TipoCurso

# Register your models here.
class TipoCursoAdmin(admin.ModelAdmin):
    list_display = ('descripcionTipoCurso',)


class CursoAdmin(admin.ModelAdmin):
    list_display = ('tituloCurso',)


class DatosCursoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'descripcionCurso',)


class DetallesCursoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'duracionCurso',)

#Register your models here.
admin.site.register(TipoCurso, TipoCursoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(DatosCurso, DatosCursoAdmin)
admin.site.register(DetallesCurso, DetallesCursoAdmin)
