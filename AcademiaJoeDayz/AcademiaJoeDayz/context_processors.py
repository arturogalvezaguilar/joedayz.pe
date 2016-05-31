
from apps.cursos.models import Curso
from django.db.models import Q

def cursos_menu(request):
    cursos = Curso.objects.all().filter(estadoCurso=1)

    presenciales = cursos.filter(tipoCurso_id=1)
    online = cursos.filter(tipoCurso_id=2)
    masivos = cursos.filter(tipoCurso_id=3)
    diplomados = cursos.filter(tipoCurso_id=4)
    presenciales_footer = cursos.filter(tipoCurso_id=1, destacadoHomeCurso=1)
    online_footer = cursos.filter(tipoCurso_id=2, destacadoHomeCurso=1)
    masivos_footer = cursos.filter(tipoCurso_id=3, destacadoHomeCurso=1)
    diplomados_footer = cursos.filter(tipoCurso_id=4, destacadoHomeCurso=1)
    return {
        'presenciales': presenciales,
        'online': online,
        'masivos': masivos,
        'diplomados': diplomados,
        'presenciales_footer': presenciales_footer,
        'online_footer': online_footer,
        'masivos_footer': masivos_footer,
        'diplomados_footer': diplomados_footer,
    }