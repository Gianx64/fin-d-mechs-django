from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from authmod.models import User

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', {'name': request.user.first_name})
    else:
        return render(request, 'home.html')

def profile(request):
    data = User.objects.get(email = request.user)
    if request.method == "POST":
        if data.email != request.POST['email'] and User.objects.filter(email = request.POST['email']):
            messages.error(request, "This email is taken! Please try another email.")
        elif request.POST['password'] != request.POST['password-confirm']:
            messages.error(request, "Passwords do not match, please try again.")
        else:
            data.first_name = request.POST['first_name']
            data.last_name = request.POST['last_name']
            data.city = request.POST['city']
            data.address = request.POST['address']
            data.mech = True if request.POST.get('mech') == 'on' else False
            data.save()
            messages.success(request, "Your account has been successfully updated!")
            return redirect(home)
    return render(request, 'auth/profile.html', {'user': data})

def signup(request):
    if request.method == "POST":
        if User.objects.filter(email = request.POST['email']):
            messages.error(request, "This email is taken! Please try another email.")
        elif request.POST['password'] != request.POST['password-confirm']:
            messages.error(request, "Passwords do not match, please try again.")
        else:
            data = User.objects.create_user(email = request.POST['email'], password = request.POST['password'])
            data.first_name = request.POST['first_name']
            data.last_name = request.POST['last_name']
            data.city = request.POST['city']
            data.address = request.POST['address']
            data.mech = True if request.POST.get('mech') == 'on' else False
            data.save()
            messages.success(request, "Your account has been successfully created!")
            return signin(request)
    return render(request, 'auth/signup.html')

def signin(request):
    if request.method == "POST":
        #TODO: login by email instead of username
        #user = authenticate(User.objects.get(email=request.POST['email'].lower()).username, password = request.POST['password'])
        user = authenticate(email = request.POST['email'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            messages.error(request, "Bad credentials.")
    return render(request, 'auth/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "You have successfully signed out!")
    return redirect('/')