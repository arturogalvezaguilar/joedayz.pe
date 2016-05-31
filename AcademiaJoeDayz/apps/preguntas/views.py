from django.shortcuts import render
from django.views.generic import ListView
from .models import PreguntaRespuesta

# Create your views here.

class ListadoPreguntas(ListView):
    def get(self, request, *args, **kwargs):
        preguntas = PreguntaRespuesta.objects.all().filter(estado_pregunta=1)
        template_name = 'preguntas/preguntas.html'
        return render(request, template_name, {'preguntas': preguntas, })



