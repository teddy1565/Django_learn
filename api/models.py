from django.db import models

# Create your models here.

class Libaray(models.Model):
    name = models.TimeField(blank=False,default='Default libaray')
    serial = models.IntegerField(default=-1)