from django.urls import path
from .views import TeamAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "team"  

urlpatterns = [path('', TeamAPIView.team, name="team"),
               path('members/deactivate-member/<int:id>', TeamAPIView.deactivate_member, name="deactivate-member"),
               path('members/delete-member/<int:id>', TeamAPIView.delete_member, name="delete-member"),
               path('team-member/<int:id>', TeamAPIView.team_member, name="team-member"),
               path('api/team/', TeamAPIView.as_view(), name="team-api"),
               path('add-member/', TeamAPIView.add_member, name="add-member"),
               path('members/', TeamAPIView.members, name="members")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if  not settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)