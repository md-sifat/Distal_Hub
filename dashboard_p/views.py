from django.shortcuts import render , redirect
from home.models import UserProfile
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
