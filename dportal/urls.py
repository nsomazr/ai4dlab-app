from django.urls import path
from .views import DPortalAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "dportal"  

urlpatterns = [path('', DPortalAPIView.dportal, name="dportal"),
               path('api/dportal/', DPortalAPIView.as_view(), name="dportal-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)