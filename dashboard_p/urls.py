from django.contrib import admin
from django.urls import path 
from dashboard_p import views
urlpatterns = [
    path('pdash/' , views.pdash , name = 'pdash'),
    path('logout/' , views.logout , name = 'logout'),
    path('pprofile/' , views.pprofile , name = 'pprofile')

]
