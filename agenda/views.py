from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Appointment, Workshop
from authmod.models import User
from datetime import datetime, timedelta

# Create your views here.
def appointmentList(request):
    if request.user.mech_verified:
        data = Appointment.objects.all().filter(mech = request.user).order_by('-id')
    else:
        data = Appointment.objects.all().filter(user = request.user).order_by('-id')
    return render(request, 'agenda/appointments.html', {'appointments' : data})

def showAppointment(request, id):
    appointment = Appointment.objects.get(id = id)
    confirmable = True if ( datetime.now().date() <= appointment.date and datetime.now().time() > appointment.time ) else False
    if request.user.mech_verified and ( appointment.completed or appointment.canceled ) and appointment.mechcomment == None:
        commentable = True
    elif not request.user.mech and appointment.completed and appointment.usercomment == None:
        commentable = True
    else:
        commentable = False
    if request.user.mech_verified:
        data = Appointment.objects.all().filter(mech = request.user, date = appointment.date)
    else:
        data = Appointment.objects.all().filter(user = request.user, mech = appointment.mech)
    return render(request, 'agenda/appointmentshow.html', {'appointment' : appointment, 'appointments' : data, 'confirmable': confirmable, 'commentable': commentable})

def createAppointment(request):
    tomorrow = datetime.now() + timedelta(days=1)
    minDate = tomorrow.strftime('%Y-%m-%d')
    deltatime = tomorrow + timedelta(days=21)
    maxDate = deltatime.strftime('%Y-%m-%d')

    if request.method == 'POST':
        if request.POST['date'] >= minDate and request.POST['date'] <= maxDate:
            if not Appointment.objects.all().filter(date = request.POST['date']):
                Appointment.objects.create(
                    user = request.user.email,
                    city = request.user.city,
                    address = request.user.address,
                    date = request.POST['date'],
                    time = request.POST['time'],
                    car_brand = request.POST['car_brand'],
                    car_model = request.POST['car_model'],
                    description = request.POST['description'],
                    service = request.POST['service'],
                    mech = request.POST['mech'],
                )
                messages.success(request, "Appointment Saved!")
                return redirect('/agenda')
            else:
                messages.success(request, "You already made an appointment for this day! You can cancel said appointment to make another one.")
        else:
            messages.success(request, "The time period is from tomorrow to the next three weeks!")
    elif request.method == 'GET':
        if request.GET['service'] == 'None':
            #workshops = Workshop.objects.all().filter(city = request.user.city)
            workshops = Workshop.objects.all()
            return render(request, 'agenda/appointmentworkshop.html', {'minDate': minDate, 'maxDate': maxDate, 'workshops': workshops})
        else:
            mechs = User.objects.all().filter(mech_verified = True, city = request.user.city)
            #mechs = User.objects.all().filter(mech_verified = True)
            return render(request, 'agenda/appointmentcreate.html', {'minDate': minDate, 'maxDate': maxDate, 'mechs': mechs})

def updateAppointment(request, id):
    if request.method == 'POST':
        appointment = Appointment.objects.get(id = id)
        if request.POST['action'] == '1' and appointment.mech == request.user.email:  #Confirm appointment
            if appointment.completed:
                messages.error(request, "Error. Appointment is completed.")
            elif appointment.canceled:
                messages.error(request, "Error. Appointment is cancelled.")
            else:
                appointment.confirmed = True
                appointment.confirmtime = datetime.now()
                messages.success(request, "Appointment Confirmed!")
        elif request.POST['action'] == '2' and (appointment.mech == request.user.email or appointment.user == request.user.email):    #Cancel appointment
            if appointment.completed:
                messages.error(request, "Error. Appointment is completed.")
            elif appointment.canceled:
                messages.error(request, "Error. Appointment is already cancelled!")
            else:
                appointment.canceled = True
                appointment.canceledby = request.user.email
                appointment.canceltime = datetime.now()
                if request.user.mech_verified:
                    appointment.mechcommenttime = datetime.now()
                    appointment.mechcomment = request.POST['reason']
                elif not request.user.mech:
                    appointment.usercommenttime = datetime.now()
                    appointment.usercomment = request.POST['reason']
                messages.success(request, "Appointment canceled!")
        elif request.POST['action'] == '3' and (appointment.mech == request.user.email or appointment.user == request.user.email):    #Mark appointment as completed
            appointment.completed = True
            appointment.completedtime = datetime.now()
            messages.success(request, "Appointment completed!")
        elif request.POST['action'] == '4' and (appointment.mech == request.user.email or appointment.user == request.user.email):    #Comment appointment
            if appointment.user == request.user.email:
                appointment.usercommenttime = datetime.now()
                appointment.usercomment = request.POST['comment']
                messages.success(request, "Comment posted!")
            elif appointment.mech == request.user.email:
                appointment.mechcommenttime = datetime.now()
                appointment.mechcomment = request.POST['comment']
                messages.success(request, "Comment posted!")
            else:
                messages.error(request, "Error. You are not this appointments user or mech!")
        appointment.save()
    return redirect('/agenda')

def deleteAppointment(request, id):
    appointment = Appointment.objects.get(id = id)
    appointment.delete()
    messages.success(request, "Appointment Deleted!")
    return redirect('/agenda')