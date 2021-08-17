from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, FormView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render
from .models import CustomUser, Group, Dog
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer
from django import forms
from django.forms import ModelForm
from accounts.forms import ContactForm
from django.contrib.auth.mixins import LoginRequiredMixin
# from accounts.models import Dog

from .forms import CustomUserCreationForm, CustomUserChangeForm, DogForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    # fields = ['groups']

class UpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('dashboard')
    template_name = 'change.html'
    # fields = '__all__'

    def get_object(self, queryset=None):
        return self.request.user

    # def get_queryset(self):
    #     return super().get_queryset()
    

class AccountDetailView(DetailView):
    model = CustomUser
    template_name = 'dashboard.html'
    context_object_name = 'user_dashboard'

    def get_object(self):
        return get_object_or_404(CustomUser, username=self.kwargs['username'])

# def breeder_view(request):
#     return render(request, 'breeders.html')
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# class DogFormView(ModelForm):
#     form_class = DogForm
#     success_url = reverse_lazy('newdog')
#     template_name = 'templates/newdog.html'

class DogCreateView(CreateView):
    model = Dog
    template_name = 'newdog.html'
    fields = '__all__'

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)