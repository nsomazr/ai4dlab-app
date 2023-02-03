from django.urls import path
from .views import PartnerAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "partner"  

urlpatterns = [path('', PartnerAPIView.partner, name="partner"),
              path('api/partner/', PartnerAPIView.as_view(), name="partner-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)