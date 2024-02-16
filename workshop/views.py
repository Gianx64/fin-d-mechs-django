from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Workshop

# Create your views here.
def workshopList(request):
    #if request.user.isAdmin: return render(request, 'workshop/workshops.html', {'workshops' : data})
    data = Workshop.objects.filter(owner = request.user).first()
    if data:
        if not data.deleted:
            return redirect('/workshop/'+str(data.id))
        else:
            return redirect('/workshop/create')
    #return render(request, 'workshop/workshops.html', {'workshops' : data})

def showWorkshop(request, id):
    workshop = Workshop.objects.get(id = id)
    return render(request, 'es/workshop/workshopshow.html', {'workshop' : workshop})

def createWorkshop(request):
    if request.method == 'POST':
        if not Workshop.objects.all().filter(address = request.POST['address'], deleted = False):
            if not Workshop.objects.all().filter(name = request.POST['name'], deleted = False):
                Workshop.objects.create(
                    owner = request.user.email,
                    name = request.POST['name'],
                    city = request.POST['city'],
                    address = request.POST['address'],
                    open = request.POST['open'],
                    close = request.POST['close'],
                    description = request.POST['description'],
                )
                messages.success(request, "Workshop saved!")
                return redirect('/workshop')
            else:
                messages.error(request, "This name is already taken by another workshop!")
        else:
            messages.error(request, "This address is already taken by another workshop!")
    return render(request, 'es/workshop/workshopcreate.html')

def updateWorkshop(request, id):
    workshop = Workshop.objects.get(id = id)
    if request.method == 'POST':
        workshop.name = request.POST['name']
        workshop.city = request.POST['city']
        workshop.address = request.POST['address']
        workshop.open = request.POST['open']
        workshop.close = request.POST['close']
        workshop.description = request.POST['description']
        workshop.save()
        messages.success(request, "Workshop updated!")
        return redirect('/workshop')
    workshop.open = workshop.open.strftime("%H:%M")
    workshop.close = workshop.close.strftime("%H:%M")
    return render(request, 'es/workshop/workshopupdate.html', {'workshop' : workshop})

def deleteWorkshop(request, id):
    workshop = Workshop.objects.get(id = id)
    workshop.deleted = True
    workshop.save()
    messages.success(request, "Workshop deleted!")
    return redirect('/workshop')