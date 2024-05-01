from django.shortcuts import render , redirect
from home.models import UserProfile
# Create your views here.

loggedIn = False
# this is homepage rendering function
def home(request):
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
            loggedIn = True
            return redirect('pdash')
        else:
            return render(request , 'patient/sign_in.html' , {'error_message': 'Invalid username or password'})
    else:
        return render(request , 'patient/sign_in.html')

# this is pateint signu method also database entry using custom models 

def psugn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        age = request.POST.get('age')
        blood_group = request.POST.get('blood_group')
        phone_number = request.POST.get('phone_number')
        location = request.POST.get('location')
        password = request.POST.get('password')
        gender = request.POST.get('gender')

        user_profile = UserProfile(username=username,email=email,age=age,blood_group=blood_group,phone_number=phone_number,location=location,password=password,gender=gender
        )
        user_profile.save()
        return redirect('psign')
    else:
        return render(request, 'patient/sign_up.html')

# this is patient dahsboard rendering function 

def pdash(request):
    return render(request , 'patient/dashboard.html')
