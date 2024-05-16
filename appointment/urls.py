from django.contrib import admin
from django.urls import path , include
from dashboard_p import views
from appointment import views
urlpatterns = [
    path('appnt/' ,  views.appnt , name = 'appnt'),
]
