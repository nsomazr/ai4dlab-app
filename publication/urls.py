from django.urls import path
from .views import PublicationAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "publication"  

urlpatterns = [path('', PublicationAPIView.publication, name="publication"),
               path('api/publication/', PublicationAPIView.as_view(), name="publication-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)