from django.db import models
from django.db.models.fields.related import ForeignKey
#
from applications.departamento.models import Departamento # No se pone punto pues es otra columna
#
from ckeditor.fields import RichTextField


class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return str(self.id) + ' - ' + self.habilidad


# Create your models here.
class Empleado(models.Model):
    """ Modelo para tabla empleado"""

    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )
    
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length= 60)
    full_name = models.CharField(
        'Nombres Completos',
        max_length=120,
        blank=True,
    )
    job = models.CharField('Trabajo', max_length=1, choices= JOB_CHOICES)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)

    # ForeignKey: relación de uno a muchos
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null = True, blank=True)
    
    # ManyToManyField: relación de muchos a muchos
    habilidades = models.ManyToManyField(Habilidades)

    # con apps de terceros
    hoja_vida = RichTextField()


    class Meta:
        verbose_name = 'Mi empleado'
        verbose_name_plural = 'Plantilla de empleados'
        ordering = ['-first_name', 'last_name']
        unique_together = ('first_name', 'departamento')

    def __str__(self):
        return str(self.id) + ' - ' + self.first_name + ' - ' + self.last_name
