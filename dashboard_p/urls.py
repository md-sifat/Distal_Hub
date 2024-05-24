from django.contrib import admin
from django.urls import path , include
from dashboard_p import views
urlpatterns = [
    path('pdash/' , views.pdash , name = 'pdash'),
    path('logout/' , views.logout , name = 'logout'),
    path('pprofile/' , views.pprofile , name = 'pprofile'),
    path('dprofile/' , views.dprofile , name = 'dprofile'),
    path('appnt/' ,  include('appointment.urls')),
    path('appnt_d/' ,  include('appointment.urls')),
    path('pdoctors/' , views.pdoctor , name='pdoctor'),
    path('precords/' , views.precords , name='precords'),
    path('drecords/' , views.drecords , name='drecords'),
    path('dupcoming/' , views.dupcoming , name='dupcoming'),
    path('dcontact/' , views.dcontact , name='dcontact'),
    path('pcontact/' , views.pcontact , name='pcontact'),

]
