from django.urls import path
from .views import WorkshopAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "workshop"  

urlpatterns = [path('', WorkshopAPIView.workshop, name="workshop"),
               path('workshop-list/review-workshop/publish-workshop/<int:id>', WorkshopAPIView.publish_workshop, name="publish-workshop"),
               path('workshop-list/review-workshop/<int:id>', WorkshopAPIView.review_workshop, name="review-workshop"),
               path('workshop-list/view-workshop/<int:id>', WorkshopAPIView.view_workshop, name="view-workshop"),
               path('workshop-list/deactivate-workshop/<int:id>', WorkshopAPIView.deactivate_workshop, name="deactivate-workshop"),
               path('workshop-list/delete-workshop/<int:id>', WorkshopAPIView.delete_workshop, name="delete-workshop"),
               path('add-workshop/', WorkshopAPIView.add_workshop, name="add-workshop"),
               path('workshop-list/', WorkshopAPIView.workshop_list, name="workshop-list"),
               path('api/workshop/', WorkshopAPIView.as_view(), name="workshop-api")
               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)