from django.urls import path
from .views import NewsAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "news"  

urlpatterns = [path('', NewsAPIView.news, name="news"),
               path('add-news/', NewsAPIView.add_news, name="add-news"),
               path('<str:slug>/', NewsAPIView.read_news, name="read-news"),
               path('news/<str:slug>/', NewsAPIView.read_news, name="read-news"),
               path('news_list/review-news/publish-news/<int:id>', NewsAPIView.publish_news, name="publish-news"),
               path('news_list/review-news/<int:id>', NewsAPIView.review_news, name="review-news"),
               path('news_list/view-news/<int:id>', NewsAPIView.view_news, name="view-news"),
               path('news_list/', NewsAPIView.news_list, name="news-list"),
               path('api/news', NewsAPIView.as_view(), name="news-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)