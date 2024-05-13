from django.shortcuts import render , redirect 
from home.models import UserProfile , DoctorProfile

# Create your views here.
# this is homepage rendering function
def home(request):
    if request.session.get('loggedIn'):
        return redirect(pdash)
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
        if(UserProfile.objects.filter(username=username).exists()):
            return render(request , 'patient/sign_up.html' , {'error_message': 'Invalid username or password'})
        else:
            email = request.POST.get('email')
            age = request.POST.get('age')
            blood_group = request.POST.get('blood_group')
            phone_number = request.POST.get('phone_number')
            location = request.POST.get('location')
            password = request.POST.get('password')
            gender = request.POST.get('gender')

            user_profile = UserProfile(username=username,email=email,age=age,blood_group=blood_group,phone_number=phone_number,location=location,password=password,gender=gender)
            user_profile.save()
            return redirect('psign')
    else:
        return render(request, 'patient/sign_up.html')

# this is patient dahsboard rendering function 



def pdash(request):
    if request.session.get('loggedIn'):
        username = request.session['username']
        try:
            user_profile = UserProfile.objects.get(username = username)
            return render(request , 'patient/dashboard.html' , {'user_profile':user_profile})
        except UserProfile.DoesNotExist:
             return render(request, 'patient/dashboard.html', {'error_message': 'User profile not found'})
    else:
        return redirect('psign')

# patient dashboardlogout function 
def logout(request):
    request.session['loggedIn']=False
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
            request.session['loggedIn']=True
            request.session['serialno']=serialno
            return redirect('pdash')
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
            email = request.POST.get('email')
            age = request.POST.get('age')
            blood_group = request.POST.get('blood_group')
            phone_number = request.POST.get('phone_number')
            location = request.POST.get('location')
            password = request.POST.get('password')
            gender = request.POST.get('gender')

            doctor_profile = DoctorProfile(serialno=serialno,email=email,age=age,blood_group=blood_group,phone_number=phone_number,location=location,password=password,gender=gender)
            doctor_profile.save()
            return redirect('dsign')



        
    else:
        return render(request, 'doctor/sign_up.html')