from django.urls import path
from . import views
from .views import SignUpView, DetailView, AccountDetailView, ContactFormView, UpdateView, DogCreateView #,DogCreateFormView #, 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings

app_name = "accounts"

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('settings/',  UpdateView.as_view(), name='update'),
    path('<str:username>/', AccountDetailView.as_view(), name='dashboard'),
    path('<str:username>/newdog/', DogCreateView.as_view(), name='newdog'),
    # path('<str:username>/addnewdog/', views.DogCreateFormView, name='newdogform'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)