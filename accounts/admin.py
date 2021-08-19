from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm, DogForm
from .models import CustomUser, Dog

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'role', 'first_name', 'last_name', 'last_login',]

class DogAdmin(admin.ModelAdmin):
    add_form = DogForm
    form = DogForm
    model = Dog
    list_display = ['name', 'color',]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Dog, DogAdmin)