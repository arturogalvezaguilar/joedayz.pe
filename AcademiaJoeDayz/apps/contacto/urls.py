from django.conf.urls import patterns, include, url
from .views import Contacto

urlpatterns = patterns('',
                       url(r'^$', Contacto.as_view(), name="Contacto"),
)


