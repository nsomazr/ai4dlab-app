from django.urls import path
from .views import SponsorAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "sponsor"  

urlpatterns = [path('', SponsorAPIView.sponsor, name="sponsor"),
              path('sponsor-api', SponsorAPIView.as_view(), name="sponsor-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)