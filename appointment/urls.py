from django.contrib import admin
from django.urls import path , include
from dashboard_p import views
from appointment import views
urlpatterns = [
    path('appnt/' ,  views.appnt , name = 'appnt'),
    path('appnt_d/' ,  views.appnt_d , name = 'appnt_d'),
    path('handle_appointment/<str:username>/<str:serialno>/<str:problem_info>/<str:desire_date>/', views.handle_appointment, name='handle_appointment'),
]
