from django.conf.urls import patterns, include, url
from .views import Empresa

urlpatterns = patterns('',
                       url(r'^$', Empresa.as_view(), name="Empresa"),
)

