from django.db import models
from tinymce.models import HTMLField


class TipoCurso(models.Model):
    descripcionTipoCurso = models.CharField(max_length=30)
    estadoTipiCurso = models.IntegerField()
    fechaIngreso = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.descripcionTipoCurso


class Curso(models.Model):
    tipoCurso = models.ForeignKey(TipoCurso)
    tituloCurso = models.CharField(max_length=60)
    footerCurso = models.CharField(max_length=20)
    fechaCurso = models.DateField()
    estadoCurso = models.IntegerField()
    destacadoHomeCurso = models.IntegerField()
    codigoMoodle = models.IntegerField(blank=True, null=True)
    
    def __unicode__(self):
        return self.tituloCurso


# Create your models here.
class DatosCurso(models.Model):
    curso = models.OneToOneField(Curso)
    descripcionCurso = HTMLField()
    temasCurso = HTMLField()
    preRequisitosCurso = HTMLField()
    participantesCurso = HTMLField()
    metodologiaCurso = HTMLField()
    sylllabusCurso = models.URLField()
    urlCurso = models.URLField()
    instructorCurso = HTMLField()
    formularioRegistro = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.curso.tituloCurso


class DetallesCurso(models.Model):
    curso = models.OneToOneField(Curso)
    duracionCurso = HTMLField()
    horariosCurso = HTMLField()
    fecInscripcurso = HTMLField()
    numParticpantes = HTMLField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    membresiaAnual = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    membresiaMensual = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    def __unicode__(self):
        return self.curso.tituloCurso



