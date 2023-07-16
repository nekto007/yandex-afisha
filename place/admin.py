from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableStackedInline, SortableAdminBase
from .models import Images, Place


def format_preview_image(image, height='200px'):
    return format_html(
        '<img src="{url}" height="{height}"/>',
        url=image.image.url,
        height=height,
    )


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['place', 'position', 'image']


class ImageInline(SortableStackedInline):
    model = Images
    extra = 0
    readonly_fields = [format_preview_image]
    list_display = ('images', format_preview_image, 'position',)
    ordering = ['position']


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    list_display = ['title', 'description_short', 'description_short', 'longitude', 'latitude']
