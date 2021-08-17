from django.urls import path
from . import views
from .views import SignUpView, DetailView, AccountDetailView, DogCreateView, ContactFormView, UpdateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView


app_name = "accounts"

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('settings/', views.UpdateView.as_view(), name='update'),
    path('<str:username>/', views.AccountDetailView.as_view(), name='dashboard'),
    # path('<str:username>/', views.AccountDetailView.as_view(), name='dashboard'),
    path('<str:username>/newdog/', DogCreateView.as_view(), name='newdog'),
]

urlpatterns += staticfiles_urlpatterns()