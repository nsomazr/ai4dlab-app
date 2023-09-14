from django.urls import path
from .views import DPortalAPIView,PatientDataAPIView
from django.conf import settings
from django.conf.urls.static import static

app_name = "dportal"  

urlpatterns = [path('', DPortalAPIView.dportal, name="dportal"),
               path('add-data/', DPortalAPIView.add_data, name="add-data"),
               path('dportal/<str:slug>/', DPortalAPIView.read_data, name="read-data"),
               path('data-list/review-data/publish-data/<int:id>', DPortalAPIView.publish_data, name="publish-data"),
               path('data-list/review-data/<int:id>', DPortalAPIView.review_data, name="review-data"),
               path('data-list/view-data/<int:id>', DPortalAPIView.view_data, name="view-data"),
               path('data-list/delete-data/<int:id>', DPortalAPIView.delete_data, name="delete-data"),
               path('data-list/', DPortalAPIView.data_list, name="data-list"),
               path('add-patient-data/', PatientDataAPIView.add_patient_data, name="add-patient-data"),
               path('patient-data-list/', PatientDataAPIView.patient_data_list, name="patient-data-list"),
               path('api/dportal/', DPortalAPIView.as_view(), name="dportal-api"),
               path("<slug:slug>", DPortalAPIView.as_view(), name="data_detail")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)