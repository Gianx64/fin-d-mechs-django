from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Appointment
from datetime import datetime, timedelta

# Create your views here.
def appointmentList(request):
    if request.user.mech_verified:
        data = Appointment.objects.all().filter(mech = request.user)
    else:
        data = Appointment.objects.all().filter(user = request.user)
    return render(request, 'agenda/appointments.html', {'appointments' : data})

def showAppointment(request, id):
    appointment = Appointment.objects.get(id = id)
    return render(request, 'agenda/showappointment.html', {'appointment' : appointment})

def createAppointment(request):
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    maxDate = deltatime.strftime('%Y-%m-%d')

    if request.method == 'POST':
        if request.POST['date'] >= minDate and request.POST['date'] <= maxDate:
            Appointment.objects.create(
                user = request.POST['user'],
                commune = request.POST['commune'],
                address = request.POST['address'],
                date = request.POST['date'],
                time = request.POST['time'],
                car_brand = request.POST['car_brand'],
                car_model = request.POST['car_model'],
                description = request.POST['description'],
                mech = request.POST['mech'],
            )
            messages.success(request, "Appointment Saved!")
            return redirect('/agenda')
        else:
            messages.success(request, "The Selected Date Isn't In The Correct Time Period!")

    return render(request, 'agenda/createappointment.html', {'maxDate': maxDate})

def updateAppointment(request, id, action):
    appointment = Appointment.objects.get(id = id)
    if action == '1':
        if appointment.completed:
            messages.error(request, "Error. Appointment is completed.")
        elif appointment.canceled:
            messages.error(request, "Error. Appointment is cancelled.")
        else:
            appointment.confirmed = True
            messages.success(request, "Appointment Confirmed!")
    elif action == '2':
        if appointment.completed:
            messages.error(request, "Error. Appointment is completed.")
        elif appointment.canceled:
            messages.error(request, "Error. Appointment is already cancelled!")
        else:
            appointment.canceled = True
            messages.success(request, "Appointment Canceled!")
    elif action == '3':
        appointment.completed = True
        messages.success(request, "Appointment Completed!")
    appointment.save()
    return redirect('/agenda')

def deleteAppointment(request, id):
    appointment = Appointment.objects.get(id = id)
    appointment.delete()
    messages.success(request, "Appointment Deleted!")
    return redirect('/agenda')