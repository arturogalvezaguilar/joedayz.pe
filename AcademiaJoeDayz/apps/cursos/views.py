#coding:UTF-8
from copy import _EmptyClass
from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import first, last
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView
from .models import Curso
from apps.paypal.models import Dolar


class Cursos(TemplateView):
    def get(self, request, *args, **kwargs):
        contexto = self.get_context_data(**kwargs)

        idcurso = contexto['idCurso']
        cursos = Curso.objects.get(id=idcurso)

        tipoCurso = cursos.tipoCurso_id

        dolar = Dolar.objects.all().filter(estado=1).last()
        precio_dolares = round(cursos.detallescurso.costo / dolar.dolar_a_soles, 2)

        if tipoCurso == 2:  #ONLINE A TU PROPIO RITMO
            membresia_anual = round(cursos.detallescurso.membresiaAnual / dolar.dolar_a_soles, 2)
            membresia_mensual = round(cursos.detallescurso.membresiaMensual / dolar.dolar_a_soles, 2)

            return render(request, 'cursos/cursos-self-placed.html',
                      {'cursos': cursos,
                       'detalles': cursos.detallescurso,
                       'datos': cursos.datoscurso,
                       'cambioDolar': precio_dolares,
                       'membresiaAnual': membresia_anual,
                       'membresiaMensual': membresia_mensual, })
        elif tipoCurso == 1:  #PRESENCIAL
            return render(request, 'cursos/cursos.html',
                      {'cursos': cursos,
                       'detalles': cursos.detallescurso,
                       'datos': cursos.datoscurso,
                       'cambioDolar': precio_dolares, })

        elif tipoCurso == 4:  #DIPlOMADOS
            return render(request, 'cursos/diplomados.html',
                      {'cursos': cursos,
                       'detalles': cursos.detallescurso,
                       'datos': cursos.datoscurso,
                       'cambioDolar': precio_dolares, })
        elif tipoCurso == 3:  #MASIVO ONLINE
                return render(request, 'cursos/cursos-mooc.html',
                      {'cursos': cursos,
                       'detalles': cursos.detallescurso,
                       'datos': cursos.datoscurso,
                       'cambioDolar': precio_dolares, })





