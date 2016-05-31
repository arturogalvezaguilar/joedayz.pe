from django.conf.urls import patterns, include, url
from .views import Video

urlpatterns = patterns('',
                       url(r'^$', Video.as_view(), name="Video"),
)


