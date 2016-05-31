from django.shortcuts import render
from django.views.generic import TemplateView
from apps.cursos.models import Curso
from .models import Multimedia, Portada


class Home(TemplateView):
    def get(self, request, *args, **kwargs):
        videos_disponibles = listando_videos_disponibles()
        fotos_disponibles = listado_fotos()
        cursos_datos = listado_curso_datos()
        online_datos = listado_curso_online()
        presenciales_datos = listado_curso_presencial()
        return render(request, 'inicio/home.html',
                      {'listado_datos': cursos_datos, 
                       'online_datos' : online_datos,
                       'presenciales_datos': presenciales_datos,
                       'videos_disponibles': videos_disponibles,
                       'fotos_disponibles': fotos_disponibles[0],
                       'contador': range(fotos_disponibles[1])})
#Procedimientos

def listando_videos_disponibles():
    videos = Multimedia.objects.all().filter(estado_video=1)
    return videos

def listado_curso_online():
    listado_online = Curso.objects.all().filter(estadoCurso=1).filter(destacadoHomeCurso=1).filter(tipoCurso_id=4)
    return listado_online

def listado_curso_presencial():
    listado_presencial = Curso.objects.all().filter(estadoCurso=1).filter(destacadoHomeCurso=1).filter(tipoCurso_id=1)
    return listado_presencial

def listado_curso_datos():
    listado_datos = Curso.objects.all().filter(estadoCurso=1).filter(destacadoHomeCurso=1)
    return listado_datos


def listado_fotos():
    fotos = Portada.objects.all().filter(estado_foto=1)
    cantidad = len(fotos)
    return fotos, cantidad 