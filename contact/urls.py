from django.urls import path
from .views import ContactAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "contact"  

urlpatterns = [path('', ContactAPIView.contact, name="contact"),
               path('api/contact/', ContactAPIView.as_view(), name="contact-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)