from django.urls import path
from .views import InitiativeAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "initiative"  

urlpatterns = [
                path('', InitiativeAPIView.initiative, name = 'initiative'),
                path('api/initiative/', InitiativeAPIView.as_view(), name="initiative-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)