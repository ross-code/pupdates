from django.urls import path
from . import views
from .views import SignUpView, DetailView, AccountDetailView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "accounts"

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('login/', SignUpView.as_view(), name='login'),
    # path('logout/', views.logout_request, name='logout'),
    # path('logout/', SignUpView.as_view(), name='logout'),
    path('<str:username>/', views.AccountDetailView.as_view(), name='dashboard'),
    # path('breeders/', breeder_view, name='breeders'),
]

urlpatterns += staticfiles_urlpatterns()