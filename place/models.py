from django.db import models


# Create your models here.
class Place(models.Model):
    title = models.CharField('Title', max_length=200)
    description_short = models.CharField('Short Description', max_length=500)
    description_long = models.CharField('Long Description', max_length=3000, blank=True)
    lon = models.FloatField(null=True, verbose_name='Долгота', blank=True)
    lat = models.FloatField(null=True, verbose_name='Широта', blank=True)
