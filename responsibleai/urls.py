from django.urls import path
from .views import ResponsibleaiAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "responsibleai"  

urlpatterns = [
                path('', ResponsibleaiAPIView.responsibleai, name = 'responsibleai'),
                path('api/responsibleai/', ResponsibleaiAPIView.as_view(), name="responsibleai-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)