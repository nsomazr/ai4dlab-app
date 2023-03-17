from django.urls import path
from .views import CommunityAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "community"  

urlpatterns = [
                path('ai4d-community', CommunityAPIView.ai4d_community, name = 'ai4d-community'),
                path('ai4d-members/', CommunityAPIView.ai4d_members, name="ai4d-members"),
                path('members/deactivate-ai4d-member/<int:id>', CommunityAPIView.deactivate_ai4d_member, name="deactivate-ai4d-member"),
                path('members/delete-ai4d-member/<int:id>', CommunityAPIView.delete_ai4d_member, name="delete-ai4d-member"),
                path('ai4d-member/<int:id>', CommunityAPIView.ai4d_member, name="ai4d-member"),
                path('register-ai4d-member/', CommunityAPIView.register_ai4d_member, name="register-ai4d-member"),
                #end ai4d
                path('udomai-community', CommunityAPIView.udomai_community, name = 'udomai-community'),
                path('udomai-members/', CommunityAPIView.udomai_members, name="udomai-members"),
                path('members/deactivate-udomai-member/<int:id>', CommunityAPIView.deactivate_udomai_member, name="deactivate-udomai-member"),
                path('members/delete-udomai-member/<int:id>', CommunityAPIView.delete_udomai_member, name="delete-udomai-member"),
                path('udomai-member/<int:id>', CommunityAPIView.udomai_member, name="udomai-member"),
                path('register-udomai-member/', CommunityAPIView.register_udomai_member, name="register-udomai-member"),
                #end udomai
                path('girlsinai-community', CommunityAPIView.girlsinai_community, name = 'girlsinai-community'),
                path('girlsinai-members/', CommunityAPIView.girlsinai_members, name="girlsinai-members"),
                path('members/deactivate-girlsinai-member/<int:id>', CommunityAPIView.deactivate_girlsinai_member, name="deactivate-girlsinai-member"),
                path('members/delete-girlsinai-member/<int:id>', CommunityAPIView.delete_girlsinai_member, name="delete-girlsinai-member"),
                path('girlsinai-member/<int:id>', CommunityAPIView.ai4d_member, name="girlsinai-member"),
                path('register-girlsinai-member/', CommunityAPIView.register_girlsinai_member, name="register-girlsinai-member"),
                path('api/community/', CommunityAPIView.as_view(), name="commnunity-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)