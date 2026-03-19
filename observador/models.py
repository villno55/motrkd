from django.db import models

class Observacion(models.Model):
    TIPO_CHOICES = [
        ('academica', 'Académica'),
        ('convivencial', 'Convivencial'),
    ]

    SEVERIDAD_CHOICES = [
        ('leve', 'Leve'),
        ('moderada', 'Moderada'),
        ('grave', 'Grave'),
    ]

    aprendiz = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    severidad = models.CharField(max_length=20, choices=SEVERIDAD_CHOICES)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.aprendiz

# Create your models here.
