from django.urls import path
from .views import ColabAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "colab"  

urlpatterns = [path('', ColabAPIView.colab, name="colab"),
              path('api/colabs/', ColabAPIView.as_view(), name="colab-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)