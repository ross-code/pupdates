from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, FormView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render, redirect
from .models import CustomUser, Group, Dog
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, DogSerializer
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

class UpdateView(LoginRequiredMixin, UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('dashboard')
    template_name = 'change.html'

    def get_absolute_url(self):
        return reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        return self.request.user    

class AccountDetailView(DetailView):
    model = CustomUser
    template_name = 'dashboard.html'
    context_object_name = 'user_dashboard'

    def get_object(self):
        return get_object_or_404(CustomUser, username=self.kwargs['username'])

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all() # .order_by('-date_joined')
    serializer_class = DogSerializer
    permission_classes = [permissions.IsAuthenticated]

def dog_image_view(request):
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DogForm()
    return render(request, 'dashboard.html', {'form': form})

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class DogCreateView(CreateView):
    model = Dog
    template_name = 'newdog.html'
    fields = '__all__'
    success_url = 'home/'

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = 'thanks/'

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)