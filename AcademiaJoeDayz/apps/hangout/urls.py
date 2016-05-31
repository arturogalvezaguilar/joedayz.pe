from django.conf.urls import patterns, include, url
from .views import Hangout

urlpatterns = patterns('',
                       url(r'^$', Hangout.as_view(), name="Hangout"),
)


