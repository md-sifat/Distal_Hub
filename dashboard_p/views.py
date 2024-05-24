from django.shortcuts import render , redirect
from home.models import UserProfile , DoctorProfile
from home.views import pdash , logout
from appointment.models import Appnt_info
from django.utils import timezone

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
    doctors = DoctorProfile.objects.all()
    return render(request , 'appnt/doctor_list.html', {'doctors' : doctors})
def precords(request):
    if request.session.get('loggedIn'):
        current_time = timezone.now()
        upcoming = Appnt_info.objects.filter(desireDate__gt=current_time , username=request.session['username'])
        previous = Appnt_info.objects.filter(desireDate__lt=current_time , username=request.session['username'])
        return render(request , 'patient/records.html' , {'upcoming' : upcoming , 'previous' : previous})
    else:
        return redirect('pdash')
    
def drecords(request):
    if request.session.get('loggedIn_d'):
        current_time = timezone.now()
        upcoming = Appnt_info.objects.filter(desireDate__gt=current_time , serialno=request.session['serialno'])
        previous = Appnt_info.objects.filter(desireDate__lt=current_time , serialno=request.session['serialno'])
        return render(request , 'doctor/records.html' , {'upcoming' : upcoming , 'previous' : previous})
    else:
        return redirect('pdash')


def appnt_d(request):
    if request.session.get('loggedIn_d'):
        pending_appnt = []
        tmp = Appnt_info.objects.get(serialno = "hidden")
        pending_appnt.append(tmp)
        pending_appnt += Appnt_info.objects.filter(serialno=request.session['serialno'], status='pending')
        accept_appnt = Appnt_info.objects.filter(serialno=request.session['serialno'], status='accepted')
        reject_appnt = Appnt_info.objects.filter(serialno=request.session['serialno'], status='rejected')
        return render(request , 'appnt/appnt_d.html' , {'pending_appnt' : pending_appnt , 'accept_appnt' : accept_appnt , 'reject_appnt':reject_appnt})
    else:
        return redirect('ddash')

def dupcoming(request):
    if request.session.get('loggedIn_d'):
        current_time = timezone.now()
        upcoming = Appnt_info.objects.filter(desireDate__gt=current_time , serialno=request.session['serialno'] , status='accepted').order_by('desireDate')
        return render(request , 'doctor/upcoming_appnt.html' , {'upcoming' : upcoming})
    else:
        return redirect('ddash')
def dcontact(request):
    return render(request , 'doctor/contact.html')
def pcontact(request):
    return render(request , 'patient/contact.html')