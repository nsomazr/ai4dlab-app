from django.urls import path
from .views import CallAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "call"  

urlpatterns = [path('', CallAPIView.call, name="call"),
               path('add-call/', CallAPIView.add_call, name="add-call"),
               path('calls/', CallAPIView.calls, name="calls"),
              path('api/call/', CallAPIView.as_view(), name="call-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)