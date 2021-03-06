from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.mail import send_mail
from .models import CustomUser, Dog
from django.forms import ModelForm
from django import forms

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role')

class CustomUserChangeForm(UserChangeForm):

    # password = ReadOnlyPasswordHashField(label='Password', help_text="Please enter your password here.")

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('username', 'first_name', 'last_name', 'role', 'number_of_dogs', 'email',)

    # def clean_password(self):
    #     return self.initial["password"]

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        # widgets = {'date_of_birth': DateInput()} # Why won't this work to make the calendar input field?
        fields = ('name', 'breeder', 'date_of_birth', 'gender', 'vaccine_status', 'height', 'weight', 'color', 'coat_type', 'allergies', 'comments', 'photo')
        # add widgets here

class ContactForm(forms.Form):
    name = forms.CharField()
    subject = forms.CharField()
    from_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    recipient_list = ['pupdates.com@gmail.com',]
    # send_mail(name, subject, from_email, message, recipient_list)
