from django.urls import path
from .views import SponsorAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "sponsor"  

urlpatterns = [path('', SponsorAPIView.sponsor, name="sponsor"),
               path('sponsors/deactivate-sponsor/<int:id>', SponsorAPIView.deactivate_sponsor, name="deactivate-sponsor"),
               path('sponsors/delete-sponsor/<int:id>', SponsorAPIView.delete_sponsor, name="delete-sponsor"),
               path('add-sponsor/', SponsorAPIView.add_sponsor, name="add-sponsor"),
               path('sponsors/', SponsorAPIView.sponsors, name="sponsors"),
               path('sponsor-api', SponsorAPIView.as_view(), name="sponsor-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if not settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)