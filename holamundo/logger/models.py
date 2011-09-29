from django.db import models

class Log(models.Model):
    fecha = models.DateField()
    tipo = models.CharField(max_length=30)
    mensaje = models.TextField()

    def __repr__(self):
        return u'Log record of type %s' % self.tipo

