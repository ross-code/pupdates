from django import forms
from django.forms import ModelForm
from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework import permissions
from accounts.forms import ContactForm
from .models import CustomUser, Group, Dog, VACCINES, GENDER
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from .serializers import UserSerializer, GroupSerializer, DogSerializer
from .forms import CustomUserCreationForm, CustomUserChangeForm, DogForm
from django.views.generic.edit import CreateView, FormView, DeleteView, UpdateView

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    # username = User.objects.username
    success_url = reverse_lazy('dashboard') #HttpResponse('Account updated successfully.') 
    # success_url = reverse_lazy('dashboard', kwargs={'username': username}) #HttpResponse('Account updated successfully.') 
    template_name = 'change.html'

    # def success_url(self):
    #     return reverse_lazy(f'/accounts/{self.request.user.username}')

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

class DogDetailView(DetailView):
    model = Dog
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

def DogCreateFormView(request, username):
    context = {
        'Vaccines': VACCINES,
        'Gender': GENDER,
    }
    return render(request, 'newdog.html', context)

def DogCreateView(request, username):
    name = request.POST['name']
    date_of_birth = request.POST['date_of_birth']
    gender = request.POST['gender']
    vaccine_status = request.POST['vaccine_status']
    height = request.POST['height']
    weight = request.POST['weight']
    color = request.POST['color']
    coat_type = request.POST['coat_type']
    allergies = request.POST['allergies']
    comments = request.POST['comments']
    photo = request.POST['photo']
    Dog.objects.create(
        name=name, 
        breeder=request.user, 
        date_of_birth=date_of_birth, 
        gender=gender,
        vaccine_status=vaccine_status,
        height=height,
        weight=weight,
        color=color,
        coat_type=coat_type,
        allergies=allergies,
        comments=comments,
        photo=photo,
    )
    return redirect('accounts:dashboard', request.user.username)

# class DogCreateView(CreateView):
#     model = Dog
#     template_name = 'newdog.html'
#     fields = ('name', 'date_of_birth', 'gender', 'vaccine_status', 'height', 'weight', 'color', 'coat_type', 'allergies', 'comments', 'photo')
#     # success_url = reverse_lazy(f'/accounts/{self.request.user.username}') #How can I get this to redirect to dashboard? How do I pass <str:username> as kwargs

#     def form_valid(self, form):
#         form.instance.breeder = self.request.user
#         return redirect(f'/accounts/{self.request.user.username}')
    # better to use a reverse rther than a redirect

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = 'thanks/'

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)