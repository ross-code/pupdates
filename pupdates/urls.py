"""pupdates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from accounts.views import ContactFormView
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.contrib import admin
from accounts import views
# from chat import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'dogs', views.DogViewSet)

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('breeders/', TemplateView.as_view(template_name='breeders.html'), name='breeders'),
    path('blog/', TemplateView.as_view(template_name='blog.html'), name='blog'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', ContactFormView.as_view(template_name='contact.html'), name='contact'),
    path('thanks/', TemplateView.as_view(template_name='thanks.html'), name='thanks'),
    path('pricing/', TemplateView.as_view(template_name='pricing.html'), name='pricing'),
    # path('messages/', TemplateView.as_view(template_name='inbox.html'), name='inbox'),
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# when deploying beware that DEBUG will break this if DEBUG changed to FALSE
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)