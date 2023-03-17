from django.urls import path
from .views import PublicationAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "publication"  

urlpatterns = [path('', PublicationAPIView.publication, name="publication"),
               path('add-publication/', PublicationAPIView.add_publication, name="add-publication"),
               path('add-publication/', PublicationAPIView.add_publication, name="add-publication"),
               # path('<str:slug>/', PublicationAPIView.read_publication, name="index-read-publication"),
               path('publication/<str:slug>/', PublicationAPIView.read_publication, name="read-publication"),
               path('publication-list/review-publication/publish-publication/<int:id>', PublicationAPIView.publish_publication, name="publish-publication"),
               path('publication-list/review-publication/<int:id>', PublicationAPIView.review_publication, name="review-publication"),
               path('publication-list/view-publication/<int:id>', PublicationAPIView.view_publication, name="view-publication"),
               path('publication-list/delete-publication/<int:id>', PublicationAPIView.delete_publication, name="delete-publication"),
               path('publication-list/', PublicationAPIView.publication_list, name="publication-list"),
               path('api/publication/', PublicationAPIView.as_view(), name="publication-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)