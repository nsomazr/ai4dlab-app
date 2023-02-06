from django.urls import path
from .views import BlogAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "blog"  

urlpatterns = [path('', BlogAPIView.blog, name="blog"),
               path('add-blog/', BlogAPIView.add_blog, name="add-blog"),
               path('blogs/', BlogAPIView.blogs, name="blogs"),
              path('api/blog/', BlogAPIView.as_view(), name="blog-api"),
              path("<slug:slug>", BlogAPIView.as_view(), name="blog_detail")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)