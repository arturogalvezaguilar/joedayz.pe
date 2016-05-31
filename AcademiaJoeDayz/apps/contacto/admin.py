from django.contrib import admin
from .models import Oficina
# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('distrito',)

admin.site.register(Oficina, ContactoAdmin)