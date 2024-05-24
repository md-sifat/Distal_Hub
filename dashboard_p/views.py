from django.shortcuts import render , redirect
from home.models import UserProfile , DoctorProfile
from home.views import pdash , logout

# Create your views here.


def pprofile(request):
    if request.session.get('loggedIn'):
        username = request.session['username']
        try:
            user_profile = UserProfile.objects.get(username = username)
            return render(request , 'patient/profile.html' , {'user_profile':user_profile})
        except UserProfile.DoesNotExist:
             return render(request, 'patient/profile.html', {'error_message': 'User profile not found'})
    else:
        return redirect('pdash')
    
def dprofile(request):
    if request.session.get('loggedIn_d'):
        serialno = request.session['serialno']
        try:
            doctor_profile = DoctorProfile.objects.get(serialno = serialno)
            return render(request , 'doctor/profile.html' , {'doctor_profile':doctor_profile})
        except UserProfile.DoesNotExist:
             return render(request, 'doctor/profile.html', {'error_message': 'User profile not found'})
    else:
        return redirect('ddash')


def pdoctor(request):
    return render(request , 'appnt/doctor_list.html')