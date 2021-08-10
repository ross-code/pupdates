from django.urls import path
from . import views
from .views import SignUpView, DetailView, AccountDetailView

app_name = "accounts"

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('<slug:slug>/', AccountDetailView.as_view(), name='dashboard'),
    path('<str:username>/', views.AccountDetailView.as_view(), name='dashboard'),
    # path('dashboard', AccountDetailView.as_view(),  name='dashboard'),
]