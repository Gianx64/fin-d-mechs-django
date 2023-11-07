from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html', {'name' : 'World'})

def signup(request):
    if request.method == "POST":
        if User.objects.filter(email = request.POST['email']):
            messages.error(request, "This email is taken! Please try another email.")
        user = User.objects.create_user(request.POST['name'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        messages.success(request, "Your account has been successfully created.")
        return redirect('home')
    return render(request, 'authentication/signup.html')

def signin(request):
    if request.method == "POST":
        #TODO: login by email instead of username
        #user = authenticate(User.objects.get(email=request.POST['email'].lower()).username, password = request.POST['password'])
        user = authenticate(username = request.POST['email'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return render(request, "home.html", {'name': user.username})
        else:
            messages.error(request, "Bad credentials.")
    return render(request, 'authentication/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "You have successfully signed out!")
    return redirect('/')