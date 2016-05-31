from django.db import models

# Create your models here.
class Oficina(models.Model):
    distrito = models.TextField()
    direccion = models.TextField()
    horario = models.TextField()
    telefono = models.TextField()
    correo = models.EmailField()
    activo = models.IntegerField()

    def __unicode__(self):
        return self.distrito