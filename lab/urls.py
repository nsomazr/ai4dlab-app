from django.urls import path
from .views import LabAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "lab"  

urlpatterns = [
                path('', LabAPIView.lab, name = 'lab'),
                path('lab/api/', LabAPIView.as_view(), name="lab-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)