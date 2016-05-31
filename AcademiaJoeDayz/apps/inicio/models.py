from django.db import models


class Multimedia(models.Model):
    titulo_video = models.CharField(max_length=50)
    url_video = models.URLField()
    fecha_video = models.DateField(auto_now_add=True)
    estado_video = models.IntegerField()


class Portada(models.Model):
    titulo_foto = models.CharField(max_length=100)
    descripcion_foto = models.CharField(max_length=150)
    url_foto = models.FileField(upload_to='portada')
    estado_foto = models.IntegerField()