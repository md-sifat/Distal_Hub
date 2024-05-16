from django.shortcuts import render

# Create your views here.


def appnt(request):
    return render(request , 'appnt/appnt.html')