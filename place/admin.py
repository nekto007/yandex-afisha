from django.contrib import admin

from .models import Images, Place


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description_short', 'description_short', 'lon', 'lat']


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['place', 'title', 'image']
