from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from .models import CustomUser
# from django import models

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class AccountDetailView(DetailView):
    model = CustomUser
    template_name = 'dashboard.html'
    context_object_name = 'user_dashboard'

    def get_object(self):
        return get_object_or_404(CustomUser, username=self.kwargs['username'])