from django.contrib.auth.models import AbstractUser
from django.db import models
# from django import forms

GENDER = [
    ('male', 'male'),
    ('female', 'female'),
]

# A user model should have the default fields PLUS be able to determine
# whether it is a breeder account or puppy parent.
class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username

# Puppy model defines the information to build out profiles on 
# each adoptable Puppy
class Puppy(models.Model):
    name = models.CharField(max_length=40)
    breeder = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)
    date_of_birth = models.DateField(auto_now=False)
    gender = models.CharField(max_length=6, null=True, choices=GENDER)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    color = models.CharField(max_length=40)
    coat_type = models.CharField(max_length=40)
    comments = models.CharField(max_length=400)
    photo = models.ImageField()

    def __str__(self):
        return self.name

# Dog model defines the information to build out profiles on 
# each Dog who is being bred so breeders can introduce them
class Dog(models.Model):
    name = models.CharField(max_length=40)
    breeder = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)
    date_of_birth = models.DateField(auto_now=False)
    gender = models.CharField(max_length=6, null=True, choices=GENDER)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    color = models.CharField(max_length=40)
    coat_type = models.CharField(max_length=40)
    comments = models.CharField(max_length=400)
    photo = models.ImageField()

    def __str__(self):
        return self.name
