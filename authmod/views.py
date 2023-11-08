from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from authmod.models import User

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        if User.objects.filter(email = request.POST['email']):
            messages.error(request, "This email is taken! Please try another email.")
        user = User.objects.create_user(email = request.POST['email'], password = request.POST['password'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        messages.success(request, "Your account has been successfully created.")
        return signin(request)
    return render(request, 'auth/signup.html')

def signin(request):
    if request.method == "POST":
        #TODO: login by email instead of username
        #user = authenticate(User.objects.get(email=request.POST['email'].lower()).username, password = request.POST['password'])
        user = authenticate(email = request.POST['email'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return render(request, "home.html", {'name': user.first_name})
        else:
            messages.error(request, "Bad credentials.")
    return render(request, 'auth/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "You have successfully signed out!")
    return redirect('/')