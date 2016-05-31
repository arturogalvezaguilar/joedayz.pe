from django.conf.urls import patterns, url
from .views import ListadoPreguntas

urlpatterns = patterns('',
                       url(r'^$', ListadoPreguntas.as_view(), name='preguntas'),
                       )
