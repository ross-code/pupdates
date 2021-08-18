from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Dog
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.mail import send_mail

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
        fields = ('name', 'date_of_birth', 'gender', 'vaccine_status', 'height', 'weight', 'color', 'coat_type', 'allergies', 'comments', 'photo')

class ContactForm(forms.Form):
    name = forms.CharField()
    subject = forms.CharField()
    from_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    recipient_list = ['rosszeiger1@gmail.com',]
    # send_mail(name, subject, from_email, message, recipient_list)

    def send_mail(self):
        pass