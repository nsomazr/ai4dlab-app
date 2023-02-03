from django.urls import path
from .views import PackageAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "package"  

urlpatterns = [
                path('', PackageAPIView.package, name = 'package'),
                path('api/package/', PackageAPIView.as_view(), name="package-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)