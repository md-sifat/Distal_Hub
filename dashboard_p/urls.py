from django.contrib import admin
from django.urls import path 
from home import views

urlpatterns = [
    path('pdash/' , views.pdash , name = 'pdash'),
    path('logout/' , views.logout , name = 'logout'),

]
