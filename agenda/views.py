from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Appointment
from datetime import datetime, timedelta

# Create your views here.
def createAppointment(request):
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    maxDate = deltatime.strftime('%Y-%m-%d')

    if request.method == 'POST':
        if request.POST['date'] >= minDate and request.POST['date'] <= maxDate:
            Appointment.objects.create(
                user = request.POST['user'],
                date = request.POST['date'],
                time = request.POST['time'],
                car_brand = request.POST['car_brand'],
                car_model = request.POST['car_model'],
                description = request.POST['description'],
                mech = request.POST['mech'],
            )
            messages.success(request, "Appointment Saved!")
            return redirect('/')
        else:
            messages.success(request, "The Selected Date Isn't In The Correct Time Period!")

    return render(request, 'agenda/createappointment.html', {'maxDate': maxDate})

def appointmentList(request):
    data = Appointment.objects.all()
    return render(request, 'agenda/appointments.html', {'reservations' : data})