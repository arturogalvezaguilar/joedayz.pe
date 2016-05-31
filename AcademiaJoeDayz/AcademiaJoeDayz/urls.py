from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.http import HttpResponse

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^google7f563fec75c24555\.html$',
                           lambda r: HttpResponse("google-site-verification: google7f563fec75c24555.html",
                                                  mimetype="text/plain")),
                       url(r'^cms/admin/', include(admin.site.urls)),
                       url(r'^tinymce/', include('tinymce.urls')),
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT,}),
                       url(r'^', include('apps.inicio.urls')),
                       url(r'^cursos/', include('apps.cursos.urls')),
                       url(r'^empresa/', include('apps.empresa.urls')),
                       url(r'^contacto/', include('apps.contacto.urls')),
                       url(r'^preguntas/', include('apps.preguntas.urls')),
                       url(r'^paypal/', include('apps.paypal.urls')),
                       url(r'^multimedia/', include('apps.multimedia.urls')),
                       url(r'^joehangout/', include('apps.hangout.urls')),
                        url(r'^videos/', include('apps.videos.urls')),
                       )

handler500 = 'AcademiaJoeDayz.views.handler500'
handler404 = 'AcademiaJoeDayz.views.handler404'
