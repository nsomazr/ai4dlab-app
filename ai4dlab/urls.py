"""ai4dlab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views 
from users import urls as user_urls
from team import urls as team_urls
from home import urls as home_urls
from news import urls as news_urls
from blog import urls as blog_urls
from call import urls as call_urls
from colab import urls as colab_urls
from conference import urls as conference_urls
from dportal import urls as dportal_urls
from event import urls as event_urls
from jupyinter import urls as jupyinter_urls
from partner import urls as partner_urls
from project import urls as project_urls
from publication import urls as publication_urls
from lab import urls as lab_urls
from contact import urls as contact_urls
from sponsor import urls as sponsor_urls
from community import urls as community_urls
from learning import urls as learning_urls
from package import urls as package_urls
from users.forms import ConfirmResetForm
urlpatterns = [
    path('admin/', admin.site.urls),
    # include django browserable 
    path("auth-api/", include("rest_framework.urls", namespace="rest_framework")),
    # include django authentication 
    # path('accounts/', include('django.contrib.auth.urls'))
    path('', include(home_urls)),
    path('users/', include(user_urls)),
    path('team/', include(team_urls)),
    path('news/', include(news_urls)),
    path('blog/', include(blog_urls)),
    path('call/', include(call_urls)),
    path('colab/', include(colab_urls)),
    path('conference/', include(conference_urls)),
    path('dportal/', include(dportal_urls)),
    path('event/', include(event_urls)),
    path('jupyinter/', include(jupyinter_urls)),
    path('partner/', include(partner_urls)),
    path('project/', include(project_urls)),
    path('publication/', include(publication_urls)),
    path('lab/', include(lab_urls)),
    path('contact/', include(contact_urls)),
    path('sponsor/', include(sponsor_urls)),
    path('community/', include(community_urls)),
    path('learning/', include(learning_urls)),
    path('package/', include(package_urls)),
    # we can mention them this way
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(form_class=ConfirmResetForm, template_name="users/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password/password_reset_complete.html'), name='password_reset_complete'),   
    # for social media authentication
    path('accounts/', include('allauth.urls')),   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
