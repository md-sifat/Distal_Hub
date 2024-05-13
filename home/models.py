from django.db import models


# database model for patient data 

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField(default=1)
    blood_group = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    firstname = models.CharField(max_length=100 , default='Firstname')
    lastname = models.CharField(max_length=100 , default='Lastname')
    aboutme = models.TextField(max_length= 200 , default='Your Bio Is Empty')
    img = models.ImageField(upload_to='user_image/' ,  default='user_image/default.jpg')
    
    def __str__(self):
        return self.username


# database model for doctor profile 

class DoctorProfile(models.Model):
    serialno = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    firstname = models.CharField(max_length=100 , default='Firstname')
    lastname = models.CharField(max_length=100 , default='Lastname')
    aboutme = models.TextField(max_length= 200 , default='Your Bio Is Empty')
    img = models.ImageField(upload_to='user_image/' ,  default='user_image/default.jpg')
    
    def __str__(self):
        return self.serialno


