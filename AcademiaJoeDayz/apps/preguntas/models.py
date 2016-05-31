from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class PreguntaRespuesta(models.Model):
    pregunta = HTMLField()
    respuesta = HTMLField()
    estado_pregunta = models.IntegerField()
    create_to = models.DateField(auto_now_add=True)
    update_to = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.pregunta
