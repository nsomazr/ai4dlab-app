from django.urls import path
from .views import CommunityAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "community"  

urlpatterns = [
                path('', CommunityAPIView.community, name = 'community'),
                path('ai4d-members/', CommunityAPIView.ai4d_members, name="ai4d-members"),
                path('girlsinai-members/', CommunityAPIView.girslinai_members, name="girlsinai-members"),
                path('api/community/', CommunityAPIView.as_view(), name="commnunity-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)