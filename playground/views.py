from django.shortcuts import render
from django.http import HttpResponse
from .models import Reservation

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name' : 'Gian'})

def reservationList(request):
    data = Reservation.objects.all()
    return render(request, 'reservations.html', {'reservations' : data})