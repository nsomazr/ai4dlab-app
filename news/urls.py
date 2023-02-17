from django.urls import path
from .views import NewsAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "news"  

urlpatterns = [path('', NewsAPIView.news, name="news"),
               path('add-news/', NewsAPIView.add_news, name="add-news"),
               path('news_list/', NewsAPIView.news_list, name="news_list"),
               path('api/news', NewsAPIView.as_view(), name="news-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)