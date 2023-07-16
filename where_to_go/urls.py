from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from place import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.start_page),
    path('places/<int:place_id>/', views.place_detail, name='place_detail'),
    path('tinymce/', include('tinymce.urls')),
    path('', RedirectView.as_view(url='/place/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
