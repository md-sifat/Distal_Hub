from django.contrib import admin
from home.models import UserProfile , DoctorProfile
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(DoctorProfile)
