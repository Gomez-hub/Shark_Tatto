from django.db import models


class contacto(models.Model):
    name = models.CharField(max_length=50)
    Email = models.EmailField()
    Message = models.TextField()









