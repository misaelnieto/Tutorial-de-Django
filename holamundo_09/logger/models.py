from django.db import models

# Create your models here.
class Log(models.Model):
    fecha = models.DateField()
    tipo = models.CharField(max_length=30)
    mensaje = models.TextField()
    
    def __repr__(self):
        return u'Este es un log de tipo %s' % self.tipo

