from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50, unique=True)#,# editable=False#)
    short_name = models.CharField('Nombre Corto', max_length=20, blank=True)
    active = models.BooleanField('Activo', default=True)

    class Meta: #Estos son decoradores
        # verbose_name = 'Mi Departamento'
        # verbose_name_plural = 'Areas de la empresa'
        ordering = ['-name', 'active']
        unique_together = ['name', 'short_name'] #No permite la creacion de registros repetidos entre name y short name

    def __str__(self):
        return str(self.id) + ' - ' + self.name

