from django.shortcuts import render , redirect
from home.models import DoctorProfile
from home.models import UserProfile
from home.views import pdash , logout
from appointment.models import Appnt_info

# Create your views here.


def appnt(request):
    if request.session.get('loggedIn'):
        if(request.method == 'POST'):
            serialno = request.POST.get('selected_card')
            username = request.session['username']
            problemInfo = request.POST.get('problemInfo')
            desireDate = request.POST.get('desireDate')
            new_appnt = Appnt_info(serialno = serialno , username=username , problemInfo = problemInfo , desireDate = desireDate)
            new_appnt.save()
            return redirect('pdash')
        else:
            doctors = DoctorProfile.objects.all()
            return render(request , 'appnt/appnt.html' , {'doctors' : doctors})
    else:
        return redirect('pdash')
    