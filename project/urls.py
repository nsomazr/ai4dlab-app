from django.urls import path
from .views import ProjectAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "project"  

urlpatterns = [path('', ProjectAPIView.project, name="project"),
              path('api/project/', ProjectAPIView.as_view(), name="project-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)