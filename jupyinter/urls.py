from django.urls import path
from .views import JupyinterAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "jupyinter"  

urlpatterns = [path('', JupyinterAPIView.jupyinter, name="jupyinter"),
              path('jupyinter', JupyinterAPIView.as_view(), name="jupyinter-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)