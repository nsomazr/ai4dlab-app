from django.urls import path
from .views import ConferenceAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "conference"  

urlpatterns = [path('', ConferenceAPIView.aaiac_23, name="aaiac-23"),
               path('AAIAC/2023/call-for-paper', ConferenceAPIView.aaiac_23_call_for_paper, name="aaiac-23-call-for-paper"),
               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)