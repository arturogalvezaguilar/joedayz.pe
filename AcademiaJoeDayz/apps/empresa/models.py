from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class DatosEmpresa(models.Model):
    quienesSomos = HTMLField()
    caracteristicas = HTMLField()
    estado = models.IntegerField()

    def __unicode__(self):
        return 'JoeDayz'


class FotoEmpresa(models.Model):
    titulo_foto = models.CharField(max_length=50)
    foto_empresa = models.FileField(upload_to='empresa')
    estado = models.IntegerField()
