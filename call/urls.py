from django.urls import path
from .views import CallAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "call"  

urlpatterns = [path('', CallAPIView.call, name="call"),
               path('add-call/', CallAPIView.add_call, name="add-call"),
               path('call/<str:slug>/', CallAPIView.read_call, name="read-call"),
               path('call-list/review-call/publish-call/<int:id>', CallAPIView.publish_call, name="publish-call"),
               path('call-list/review-call/<int:id>', CallAPIView.review_call, name="review-call"),
               path('call-list/view-call/<int:id>', CallAPIView.view_call, name="view-call"),
               path('call-list/delete-call/<int:id>', CallAPIView.delete_call, name="delete-call"),
               path('call-list/', CallAPIView.call_list, name="call-list"),
               path('api/call/', CallAPIView.as_view(), name="call-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)