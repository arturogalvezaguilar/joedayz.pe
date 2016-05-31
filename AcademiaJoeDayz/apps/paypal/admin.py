from django.contrib import admin
from .models import Dolar

# Register your models here.
class DolarAdmin(admin.ModelAdmin):
    list_display = ('dolar_a_soles', 'estado',)


admin.site.register(Dolar, DolarAdmin)