from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.urls import reverse
# from django.db.models import Models
# from django import forms

GENDER = [
    ('male', 'male'),
    ('female', 'female'),
]

VACCINES = [
    ('Rabies', 'Rabies'),
    ('Parvo', 'Parvo'),
    ('Distemper', 'Distemper'),
    ('Bordetella', 'Bordetella'),
    ('Hepatitis', 'Hepatitis'),
    ('Influenza', 'Influenza'),
    ('Heartworm', 'Heartworm'),
    ('Leptospirosis', 'Leptospirosis'),
    ('Lyme Disease', 'Lyme Disease'),
]

# A user model should have the default fields PLUS be able to determine
# whether it is a breeder account or puppy parent.
class CustomUser(AbstractUser):
    BREEDER = 1
    PUPPY_PARENT = 2

    ROLE_CHOICES = (
        (BREEDER, 'Breeder'),
        (PUPPY_PARENT, 'Puppy Parent (Adopter)'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    number_of_dogs = models.PositiveSmallIntegerField(blank=True, null=True)
    # groups = groups.set(models.CharField(max_length=13, null=True, choices=ROLE_CHOICES))
    # add additional fields in here
    def create_user(self, email, first_name, last_name, groups):
        pass

    def __str__(self):
        return self.username

# Dog model defines the information needed for each dog/puppy
class Dog(models.Model):
    name = models.CharField(max_length=40)
    breeder = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    date_of_birth = models.DateField(auto_now=False)
    gender = models.CharField(max_length=6, null=True, choices=GENDER)
    vaccine_status = models.CharField(max_length=20, null=True, choices=VACCINES)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    color = models.CharField(max_length=40)
    coat_type = models.CharField(max_length=40)
    allergies = models.CharField(max_length=100)
    comments = models.CharField(max_length=400)
    photo = models.ImageField(upload_to='', height_field=None, width_field=None, blank=True)

    def get_absolute_url(self):
        return reverse("dashboard", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name