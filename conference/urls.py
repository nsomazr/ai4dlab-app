from django.urls import path
from .views import ConferenceAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "conference"  

urlpatterns = [path('conferences/', ConferenceAPIView.as_view(), name="conferences")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)