from django.urls import path
from .views import LearningAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "learning"  

urlpatterns = [
                path('', LearningAPIView.learning, name = 'learning'),
                path('api/learning/', LearningAPIView.as_view(), name="learning-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)