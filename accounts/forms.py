from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Dog
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role')

class CustomUserChangeForm(UserChangeForm):

    # password = ReadOnlyPasswordHashField(label='Password', help_text="Please enter your password here.")

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'email', 'password')

    def clean_password(self):
        return self.initial["password"]

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = '__all__'

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        pass