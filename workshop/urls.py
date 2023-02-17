from django.urls import path
from .views import WorkshopAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "workshop"  

urlpatterns = [path('', WorkshopAPIView.workshop, name="workshop"),
            #    path('workshops/deactivate-workshop/<int:id>', PartnerAPIView.deactivate_partner, name="deactivate-workshop"),
            #    path('workshops/delete-workshop/<int:id>', PartnerAPIView.delete_partner, name="delete-workshop"),
            #    path('add-workshop/', PartnerAPIView.add_partner, name="add-workshop"),
            #    path('workshops/', PartnerAPIView.partners, name="workshops"),
            #    path('api/workshop/', PartnerAPIView.as_view(), name="workshop-api")
               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)