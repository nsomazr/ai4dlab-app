from django.urls import path
from .views import ProjectAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "project"  
urlpatterns = [path('', ProjectAPIView.project, name="project"),
               path('add-project/', ProjectAPIView.add_project, name="add-project"),
               path('add-project/', ProjectAPIView.add_project, name="add-project"),
               # path('<str:slug>/', ProjectAPIView.read_project, name="index-read-project"),
               path('project/<str:slug>/', ProjectAPIView.read_project, name="read-project"),
               path('project-list/review-project/publish-project/<int:id>', ProjectAPIView.publish_project, name="publish-project"),
               path('project-list/review-project/<int:id>', ProjectAPIView.review_project, name="review-project"),
               path('project-list/view-project/<int:id>', ProjectAPIView.view_project, name="view-project"),
               path('project-list/delete-project/<int:id>', ProjectAPIView.delete_project, name="delete-project"),
               path('project-list/', ProjectAPIView.project_list, name="project-list"),
               path('api/project/', ProjectAPIView.as_view(), name="project-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
