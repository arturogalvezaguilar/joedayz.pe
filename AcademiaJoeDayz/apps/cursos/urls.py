from django.conf.urls import patterns, url
from .views import Cursos

urlpatterns = patterns('',
                       url(r'^(?P<idCurso>[\d]+)/$', Cursos.as_view(), name='Cursos'),
)


