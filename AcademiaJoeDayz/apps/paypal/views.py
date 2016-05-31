from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView
from apps.cursos.models import Curso
from apps.paypal.models import ModeloPaypal



# Create your views here.
@csrf_protect
def pagar(request):
    if request.method == 'POST':
        id_curso = int(request.GET['idCurso'])
        curso = Curso.objects.get(id=id_curso)
        ModeloPaypal.item_name = curso.tituloCurso
        ModeloPaypal.item_number = curso.id
        ModeloPaypal.amount = curso.detallescurso.costo
        # print request
        pass


class Gracias(TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'paypal/graciasPaypal.html'
        return render(request, template_name)