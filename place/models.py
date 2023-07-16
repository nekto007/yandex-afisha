from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Place(models.Model):
    title = models.CharField('Title', max_length=200)
    description_short = models.CharField('Short Description', max_length=500)
    description_long = HTMLField('Полное описание', blank=True)
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')

    class Meta:
        verbose_name = 'place'
        verbose_name_plural = 'places'

    def __str__(self):
        return self.title


class Images(models.Model):
    place = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(blank=True, null=True)
    position = models.IntegerField(
        default=1,
        db_index=True
    )

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'
        ordering = ('position',)

    def __str__(self):
        return self.image.name
