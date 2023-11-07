from django.shortcuts import render
from .models import Reservation

# Create your views here.
def reservationList(request):
    data = Reservation.objects.all()
    return render(request, 'reservations.html', {'reservations' : data})