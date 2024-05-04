from django.contrib import admin
from django.urls import path , include
from home import views

urlpatterns = [
    path('' , views.home , name = 'home'),
    path('psign/' , views.psign , name = 'psign'),
    path('psugn/' , views.psugn , name = 'psugn'),
    path('pdash/' , include('dashboard_p.urls')),
    path('dsign/' , views.home , name = 'dsign'),

]
