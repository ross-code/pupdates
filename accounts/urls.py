from django.urls import path
from . import views
from .views import SignUpView, DetailView, AccountDetailView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView


app_name = "accounts"

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<str:username>/', views.AccountDetailView.as_view(), name='dashboard'),
    path('<str:username>/newdog', TemplateView.as_view(template_name='newdog.html'), name='newdog'),
]

urlpatterns += staticfiles_urlpatterns()