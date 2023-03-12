from django.urls import path
from .views import BlogAPIView
from django.conf import settings
from django.conf.urls.static import static

app_name = "blog"  

urlpatterns = [path('', BlogAPIView.blog, name="blog"),
               path('add-blog/', BlogAPIView.add_blog, name="add-blog"),
               path('blogs/<str:slug>/', BlogAPIView.read_blog, name="read-blog"),
               path('blog-list/review-blog/publish-blog/<int:id>', BlogAPIView.publish_blog, name="publish-blog"),
               path('blog-list/review-blog/<int:id>', BlogAPIView.review_blog, name="review-blog"),
               path('blog-list/view-blog/<int:id>', BlogAPIView.view_blog, name="view-blog"),
               path('blog-list/delete-blog/<int:id>', BlogAPIView.delete_blog, name="delete-blog"),
               path('blog-list/', BlogAPIView.blog_list, name="blog-list"),
               path('api/blog/', BlogAPIView.as_view(), name="blog-api"),
               path("<slug:slug>", BlogAPIView.as_view(), name="blog_detail")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)