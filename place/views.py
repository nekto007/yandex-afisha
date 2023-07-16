from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from place.models import Place


def start_page(request):
    places = Place.objects.all()
    features = []
    for place in places:
        geo_point = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.longitude, place.latitude]
            },
            'properties': {
                'title': place.title,
                'placeId': place.pk,
                'detailsUrl': reverse('place_detail', kwargs={'place_id': place.pk})
            }
        }
        features.append(geo_point)

    geo_places = {
        'type': 'FeatureCollection',
        'features': features
    }
    print(geo_places)
    context = {
        'geo_places': geo_places
    }
    print(context)
    return render(request, 'index.html', context)


def place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    images = place.images.order_by('position')

    detail = {
        'title': place.title,
        'imgs': [img.image.url for img in images],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude
        }
    }

    return JsonResponse(detail, json_dumps_params={'indent': 4, 'ensure_ascii': False})
