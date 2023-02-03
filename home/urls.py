from django.urls import path
from .views import HomeAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "home"  

urlpatterns = [
                path('', HomeAPIView.home, name = 'home'),
                path('api/home/', HomeAPIView.as_view(), name="home-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)