from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    password = models.CharField(max_length=100)  # Add password field
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)


