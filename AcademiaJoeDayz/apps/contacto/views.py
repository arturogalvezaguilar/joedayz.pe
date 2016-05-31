from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from .models import Oficina


class Contacto(TemplateView):
    def get(self, request, *args, **kwargs):
        datos = lista_oficinas()
        return render(request, 'contacto/contacto.html', {'datos': datos, })


def lista_oficinas():
    try:
        lista = Oficina.objects.all().filter(activo=1)
    except ObjectDoesNotExist:
        lista = None
    return lista
