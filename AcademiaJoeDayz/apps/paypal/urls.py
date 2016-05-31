from django.conf.urls import patterns, url
from .views import Gracias

urlpatterns = patterns('',
                       url(r'^pagar/$', 'apps.paypal.views.pagar', name='PagarConPaypal'),
                       url(r'^gracias/$', Gracias.as_view(), name='GraciasConPaypal'),
)


