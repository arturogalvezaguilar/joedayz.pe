from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from .models import DatosEmpresa, FotoEmpresa


class Empresa(TemplateView):
    def get(self, request, *args, **kwargs):
        datos = lista_datos_empresa()
        foto = lista_foto_empresa()
        return render(request, 'empresa/empresa.html',
                      {'datos': datos,
                       'foto': foto, })


def lista_datos_empresa():
    try:
        lista = DatosEmpresa.objects.all().filter(estado=1)
    except ObjectDoesNotExist:
        lista = None
    return lista


def lista_foto_empresa():
    try:
        lista = FotoEmpresa.objects.all().filter(estado=1)
    except ObjectDoesNotExist:
        lista = None
    return lista