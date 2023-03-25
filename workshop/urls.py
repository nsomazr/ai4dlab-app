from django.urls import path
from .views import WorkshopAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "workshop"  

urlpatterns = [path('', WorkshopAPIView.workshop_22, name="workshop-22"),
               path('workshop/22/sessions', WorkshopAPIView.workshop_22_sessions, name="workshop-22-sessions"),
               path('workshop/22/speakers', WorkshopAPIView.workshop_22_sessions, name="workshop-22-speakers"),
               path('workshop/22/organizers', WorkshopAPIView.workshop_22_organizers, name="workshop-22-organizers"),
               path('api/workshop/', WorkshopAPIView.as_view(), name="workshop-api")
               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)