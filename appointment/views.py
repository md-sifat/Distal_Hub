from django.shortcuts import render , redirect , get_object_or_404
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
    
def appnt_d(request):
    if request.session.get('loggedIn_d'):
        pending_appnt = Appnt_info.objects.filter(serialno=request.session['serialno'], status='pending')
        accept_appnt = Appnt_info.objects.filter(serialno=request.session['serialno'], status='accepted')
        reject_appnt = Appnt_info.objects.filter(serialno=request.session['serialno'], status='rejected')
        return render(request , 'appnt/appnt_d.html' , {'pending_appnt' : pending_appnt , 'accept_appnt' : accept_appnt , 'reject_appnt':reject_appnt})

    else:
        return redirect('ddash')


def handle_appointment(request, username, serialno, problem_info, desire_date):
    appointment = get_object_or_404(Appnt_info, username=username, serialno=serialno, problemInfo=problem_info, desireDate=desire_date)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'accept':
            appointment.status = 'accepted'
        elif action == 'reject':
            appointment.status = 'rejected'
        appointment.save()
        return redirect('appnt_d')