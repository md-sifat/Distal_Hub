from django.contrib import admin
from django.urls import path 
from home import views

urlpatterns = [
    path('' , views.home , name = 'home'),
    path('psign/' , views.psign , name = 'psign'),
    path('psugn/' , views.psugn , name = 'psugn'),
    path('pdash/' , views.pdash , name = 'pdash'),
    path('dsign/' , views.home , name = 'dsign'),

]
