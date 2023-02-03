from django.urls import path
from .views import EventAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "event"  

urlpatterns = [path('', EventAPIView.event, name="event"),
              path('api/event/', EventAPIView.as_view(), name="event-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)