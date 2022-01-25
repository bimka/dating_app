from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'api'

urlpatterns = [
    path(
        'api/clients/create',
        views.ClientCreateView.as_view(), 
        name="client_create"),
]
if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)