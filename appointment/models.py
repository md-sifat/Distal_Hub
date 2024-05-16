from django.db import models

# Create your models here.


class Appnt_info(models.Model):
    username = models.CharField(max_length=100)
    serialno = models.CharField(max_length=100)

    problemInfo = models.CharField(max_length=1000)
    desireDate = models.DateTimeField()    
    def __str__(self):
        return self.username+self.serialno
