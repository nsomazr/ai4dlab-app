from django.urls import path
from .views import TeamAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "team"  

urlpatterns = [path('', TeamAPIView.team, name="team"),
               path('api/team/', TeamAPIView.as_view(), name="team-api"),
               path('add-member/', TeamAPIView.add_member, name="add-member"),
               path('members/', TeamAPIView.members, name="members")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)