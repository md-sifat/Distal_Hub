from django.shortcuts import render , redirect 
from home.models import UserProfile , DoctorProfile
from appointment.models import Appnt_info


# Create your views here.
# this is homepage rendering function
def home(request):
    if request.session.get('loggedIn'):
        return redirect(pdash)
    elif request.session.get('loggedIn_d'):
        return redirect(ddash)
    else:
        return render(request , 'index.html')

# this is patient log in authentication custom 
def psign(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user_profile = UserProfile.objects.get(username = username)
        except UserProfile.DoesNotExist:
            return render(request , 'patient/sign_in.html' , {'error_message': 'Invalid username or password'})
        if user_profile.password == password:
            request.session['loggedIn']=True
            request.session['username']=username
            return redirect('pdash')
        else:
            return render(request , 'patient/sign_in.html' , {'error_message': 'Invalid username or password'})
    else:
        return render(request , 'patient/sign_in.html')

# this is pateint signu method also database entry using custom models 
def psugn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        if(UserProfile.objects.filter(username=username).exists()):
            return render(request , 'patient/sign_up.html' , {'error_message': 'username already exits'})
        else:
            email = request.POST.get('email')
            age = request.POST.get('age')
            blood_group = request.POST.get('blood_group')
            phone_number = request.POST.get('phone_number')
            location = request.POST.get('location')
            password = request.POST.get('password')
            gender = request.POST.get('gender')
            # img = request.FILES.get('image')

            user_profile = UserProfile(username=username,firstname=firstname,lastname=lastname , email=email,age=age,blood_group=blood_group,phone_number=phone_number,location=location,password=password,gender=gender)
            user_profile.save()
            return redirect('psign')
    else:
        return render(request, 'patient/sign_up.html')


# this is patient dahsboard rendering function 

def pdash(request):
    if request.session.get('loggedIn'):
        user_count = UserProfile.objects.count()
        doctor_count = DoctorProfile.objects.count()
        appnt_count = Appnt_info.objects.count()
        
        username = request.session['username']
        try:
            user_profile = UserProfile.objects.get(username = username)
            return render(request , 'patient/dashboard.html' , {'user_profile':user_profile , 'user_count' : user_count , 'doctor_count' : doctor_count , 'appnt_count' : appnt_count})
        except UserProfile.DoesNotExist:
             return render(request, 'patient/dashboard.html', {'error_message': 'User profile not found'})
    else:
        return redirect('psign')

# patient dashboardlogout function 
def logout(request):
    request.session['loggedIn']=False
    request.session['loggedIn_d']=False
    return redirect(home)


# doctor build section 

# this is doctor log in auth for doctor 

def dsign(request):
    if request.method == 'POST':
        serialno = request.POST.get('serialno')
        password = request.POST.get('password')
        try:
            doctor_profile = DoctorProfile.objects.get(serialno = serialno)
        except DoctorProfile.DoesNotExist:
            return render(request , 'doctor/sign_in.html' , {'error_message': 'Invalid serial no or password'})
        if doctor_profile.password == password:
            request.session['loggedIn_d']=True
            request.session['serialno']=serialno
            return redirect('ddash')
        else:
            return render(request , 'doctor/sign_in.html' , {'error_message': 'Invalid serial no or password'})
    else:
        return render(request , 'doctor/sign_in.html')


def dsugn(request):
    if request.method == 'POST':
        serialno = request.POST.get('serialno')
        if(DoctorProfile.objects.filter(serialno=serialno).exists()):
            return render(request , 'doctor/sign_up.html' , {'error_message': 'Invalid username or password'})
        else:
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            specialization = request.POST.get('specialization')
            email = request.POST.get('email')
            age = request.POST.get('age')
            blood_group = request.POST.get('blood_group')
            phone_number = request.POST.get('phone_number')
            location = request.POST.get('location')
            password = request.POST.get('password')
            gender = request.POST.get('gender')

            doctor_profile = DoctorProfile(serialno=serialno,firstname=firstname,lastname=lastname,specialization = specialization,email=email,age=age,blood_group=blood_group,phone_number=phone_number,location=location,password=password,gender=gender)
            doctor_profile.save()
            return redirect('dsign')    
    else:
        return render(request, 'doctor/sign_up.html')

# this is patient dahsboard rendering function 

def ddash(request):
    if request.session.get('loggedIn_d'):
        user_count = UserProfile.objects.count()
        doctor_count = DoctorProfile.objects.count()
        appnt_count = Appnt_info.objects.count()
        serialno = request.session['serialno']
        try:
            doctor_profile = DoctorProfile.objects.get(serialno = serialno)
            return render(request , 'doctor/dashboard.html' , {'doctor_profile':doctor_profile ,  'user_count' : user_count , 'doctor_count' : doctor_count , 'appnt_count' : appnt_count})
        except UserProfile.DoesNotExist:
             return render(request, 'doctor/dashboard.html', {'error_message': 'Doctor profile not found'})
    else:
        return redirect('dsign')