from django.urls import path
from .views import ColabAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "colab"  

urlpatterns = [path('', ColabAPIView.colab, name="colab"),
               path('add-colab/', ColabAPIView.add_colab, name="add-colab"),
               path('colabs/', ColabAPIView.colabs, name="colabs"),
              path('api/colabs/', ColabAPIView.as_view(), name="colab-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)