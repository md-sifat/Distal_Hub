from django.db import models
from django.utils import timezone

# Create your models here.


class Appnt_info(models.Model):
    username = models.CharField(max_length=100 , default="Empty")
    serialno = models.CharField(max_length=100 , default="Empty")

    problemInfo = models.CharField(max_length=1000 , default="Empty")
    desireDate = models.DateTimeField(default=timezone.now)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')


    def __str__(self):
        return self.username+self.serialno
