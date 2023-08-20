from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Place(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    description_short = models.TextField(verbose_name='Короткое описание', max_length=500)
    description_long = HTMLField(verbose_name='Полное описание', blank=True)
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')

    class Meta:
        verbose_name = 'place'
        verbose_name_plural = 'places'

    def __str__(self):
        return self.title


class Images(models.Model):
    place = models.ForeignKey('Place', verbose_name='Место', on_delete=models.CASCADE, related_name='images', blank=False)
    image = models.ImageField(verbose_name='Изображение', blank=True)
    position = models.IntegerField(
        default=1,
        db_index=True,
        blank=True
    )

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'
        ordering = ('position',)

    def __str__(self):
        return self.image.name
