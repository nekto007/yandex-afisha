from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from where_to_go import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.start_page),
    path('place/', include('place.urls')),
    path('', RedirectView.as_view(url='/place/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
